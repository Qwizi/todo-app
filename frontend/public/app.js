
let logged = localStorage.getItem('token') ? true : false;
console.log(logged);
console.log(localStorage.getItem('token'));

let token = localStorage.getItem('token');
let userData = [];

async function getUserData() {
    try {
        res = await axios.get('http://localhost:8000/api/users/me/', {
            headers: {'Authorization': `Token ${token}`}
        })
        userData = res.data;
        console.log("Dane dodane");
        console.log(userData);
    } catch (error) {
        console.log(error)
    }
}

if (logged) {
    getUserData()
}

document.getElementById('login').addEventListener('click', async () => {
    try {
        res = await axios.post('http://localhost:8000/api-token-auth/', {
            username: "admin",
            password: "admin123"
        });
        localStorage.setItem('token', res.data.token);
        logged = true;
        console.log(res.data);
        console.log('zalogowano');
        location.reload();
    } catch (error) {
        console.log(error)
    }
});

document.getElementById('logout').addEventListener('click', () => {
    localStorage.removeItem('token')
    logged = false;
    console.log('Wylogowano!')
    location.reload();
});

async function getTodosWithForEach() {
    let res = await axios.get('http://localhost:8000/api/todos/');
    let todosUL = document.getElementById('todos');
    res.data.forEach((item, index) => {
        todosUL.innerHTML += "<li id=" + index + ">" + item['title'] + "</li>";
    })
}
getTodosWithForEach();