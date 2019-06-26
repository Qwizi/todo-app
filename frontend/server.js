var express = require('express');
var app = express();
var path = require('path');

app.use('/static', express.static(path.join(__dirname, 'static')))
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(3000);

console.log('Application listen on port 3000');