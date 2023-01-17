let BASE_URL = "http://43.201.124.44:8000/";

// id 로 버튼 찾기
let btnLogin = document.getElementById('btnLogin');

// 버튼에 클릭 이벤트 추가
btnLogin.addEventListener('click', function () {
    console.log("Login button clicked");

    // textField 값 갖고오기
    let val_username = document.getElementById('tfUsername').value;
    let val_password = document.getElementById('tfPassword').value;

    console.log(val_username);
    console.log(val_password);
    console.log(BASE_URL);

    // fetch 로 서버와 http 통신
    fetch(BASE_URL + 'users/login/', {
        method: 'POST',
        headers: {
            // TODO 헤더 - Content-Type 은 디폴트로 넣어두고, 필요에 따라 추가
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            // TODO 바디 - 키 : 값 매칭 (hashMap 을 떠올리면 쉬움)
            username: val_username,
            password: val_password
        }),
    })
        // response 를 json 으로 파싱
        .then((response) => response.json())
        // data <= response.json() 으로 파싱된 값
        .then((data) => {
            console.log(data)
            // TODO token을 쿠키/캐시에 저장

            // TODO token을 localStorage에 저장
            localStorage.setItem('token', data.token);
            // 페이지 이동
            location.href = "board.html";
        })
        .catch((error) => {
            // 에러 시 로그에 출력하는 부분
            console.log(error);
        });
});