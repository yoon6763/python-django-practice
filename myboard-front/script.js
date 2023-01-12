let btnLogin = document.getElementById('btnLogin');
btnLogin.addEventListener('click', function () {

    // fetch('http://localhost:8000/users/register/', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({
    //         "username": "testuser7",
    //         "password": "qwerty!!",
    //         "password2": "qwerty!!",
    //         "email": "adf@sadt.com"
    //     }),
    // })
    //     .then(response => response.json())
    //     .then(data => console.log(data))
    //     .catch((error) => {
    //         console.log(error)
    //     });

    fetch('http://localhost:8000/users/profile/5/', {
        method: 'GET',
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            alert(data);
        })
        .catch((error) => console.log(error));


    // // let val_username = document.getElementById('tfUsername').value;
    // // let val_password = document.getElementById('tfPassword').value;
    // let val_username = "testuser1";
    // let val_password = "qwerty!!";
    //
    // console.log(val_username);
    // console.log(val_password);
    //
    // fetch('http://localhost:8000/users/login/', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({
    //         username: val_username,
    //         password: val_password
    //     }),
    // })
    //     .then((response) => response.json())
    //     .then((data) => {
    //         console.log(data)
    //     }).catch((error) => console.log(error));


});