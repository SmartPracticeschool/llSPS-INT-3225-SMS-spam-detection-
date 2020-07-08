
const text = document.querySelector('text');
const button = document.querySelector('button');
const result = document.getElementById('result');
submit.addEventListener('click',(event) => {
	const value =  text.value;
	if(value != ''){
		axios.post('http://localhost:5000/predict',{
			tweet : value
		}).then(response => {
			resultdiv.innerHTML = `<p>${response.data}</p>`
			resultdiv.classList.remove('positive','negative');
			resultdiv.classList.add(response.data == 'Positive' ? 'positive' : 'negative');
		}).catch(err =>{
			console.log(err);
		})
	}
})





<form action='/predict' method="post">