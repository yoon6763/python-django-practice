let BASE_URL = "http://43.201.124.44:8000/";
let token = localStorage.getItem('token');

console.log(token);

fetch(BASE_URL + 'posts/', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'authorization': 'Token ' + token,
    }
})
    .then(r => r.json())
    .then(data => {
        console.log(data);
        let boardList = document.getElementById('boardList');
        boardList.innerHTML = '';

        for (let i = 0; i < data.count; i++) {
            let post = data.results[i];
            let title = post.title;
            let author = post.author.username;
            let date = post.published_date;

            let li = document.createElement('li');
            li.innerHTML = title + '\t' + author + '\t' + date;
            boardList.appendChild(li);

        }
    })
    .catch(error => console.log(error));