const api = axios.create({
    baseURL: 'http://localhost:8000'
})

let logged = localStorage.getItem('token') ? true : false;
console.warn(`Czy zalogowany: ${logged}`);
console.log(`Token: ${localStorage.getItem('token')}`);

let token = localStorage.getItem('token');
let userData = [];

async function getUserData() {
    try {
        let res = await api.get(`/api/users/me/`, {
            headers: {
                'Authorization': `Token ${token}`
            }
        })
        userData = res.data;
        console.log(userData);
    } catch (error) {
        console.log(error)
    }
}

if (logged) {
    getUserData()
}

//Register
const formRegister = document.querySelector('#formRegister');
formRegister.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const uName = document.querySelector('#name').value;
        const uPass = document.querySelector('#password').value;
        const uMail = document.querySelector('#email').value;
        let res = await api.post(`/api/users/`, {
            username: uName,
            password: uPass,
            email: uMail
        });
        console.log(`zarejestrowano nowego usera ${uName} ${uMail}`);
    } catch (error) {
        console.log(error)
    }
});

//Login
const formLogin = document.querySelector('#formLogin');
formLogin.addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
        const uName = document.querySelector('#username').value;
        const uPass = document.querySelector('#user-password').value;
        let res = await api.post(`/api-token-auth/`, {
            username: uName,
            password: uPass
        });
        localStorage.setItem('token', res.data.token);
        logged = true;
        console.log(res.data);
        console.log('zalogowano');
        location.reload();
    } catch (error) {
        console.log(error);
    }
});

//Logout
const btnLogout = document.querySelector('#btn-logout');
btnLogout.addEventListener('click', () => {
    localStorage.removeItem('token')
    logged = false;
    console.log('Wylogowano!')
    location.reload();
});
