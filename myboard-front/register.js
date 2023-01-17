let BASE_URL = "http://43.201.124.44:8000/";

document.getElementById('btnRegister')
    .addEventListener('click', function () {
        let userId = document.getElementById('tfRegisterId').value;
        let password = document.getElementById('tfRegisterPw').value;
        let passwordCheck = document.getElementById('tfRegisterPwCheck').value;
        let email = document.getElementById('tfRegisterEmail').value;

        if (password !== passwordCheck) {
            alert('비밀번호가 일치하지 않습니다.');
            return;
        }

        // BASE_URL 은 constants.js 에서 가져옴
        fetch(BASE_URL + 'users/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: userId,
                password: password,
                password2: passwordCheck,
                email: email,
            }),
        })
            .then(r => r.json())
            .then(data => {
                console.log(data);
                window.open('index.html')
            })
            .catch(error => console.log(error));
    });
