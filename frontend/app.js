async function getGithubData() {
    let res = await axios.get('https://api.github.com/users/Qwizi');
    console.log(res.data.login);
}
getGithubData();