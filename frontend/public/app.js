async function getTodos() {
    let res = await axios.get('http://localhost:8000/api/todos/');
    let todosDiv = document.getElementById('todos');
    let todos = '<ul>';
    for (var i = 0; i < res.data.length; i++) {
        todos += "<li>" + res.data[i]['title'] + "</li>"
    };
    todos += '</ul>';
    todosDiv.innerHTML = todos
    console.log(res.data);
}
getTodos();