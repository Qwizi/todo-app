async function getTodos() {
    let res = await axios.get('http://localhost:8000/api/todos/');
    console.log(res.data);
}
getTodos();