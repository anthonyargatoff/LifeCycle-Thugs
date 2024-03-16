const url = 'http://127.0.0.1:5000/send_data';

fetch(url).then(response => response.json()).then(json => console.log(JSON.stringify(json)));