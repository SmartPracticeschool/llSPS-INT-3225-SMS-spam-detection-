from flask import render_template, Flask, request,url_for
from keras.models import load_model
import pickle 
import tensorflow as tf
graph = tf.get_default_graph()
with open(r'CountVectorizer','rb') as file:
    cv=pickle.load(file)
cla = load_model('spam.h5')
cla.compile(optimizer='adam',loss='binary_crossentropy')
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('project.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
        topic = request.form['tweet']
        print(topic)
        topic=cv.transform([topic])
        print(topic)
        with graph.as_default():
            ypred = cla.predict(topic)
            print("pred is "+str(ypred))
            if(ypred>0.5):
            
                topic = "Spam message"
        
            elif(ypred<0.5):
                topic = "Not a Spam (It is a Ham) message"
            return render_template('project.html',y_pred = topic)
        



if __name__ == '__main__':
    app.run(host = 'localhost', debug = True , threaded = False)