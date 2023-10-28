// Include the express module
var express = require('express');

// Create a new express application
var app = express();

// Define the port number
var port = 3000;

app.use(express.static('public'));

// Define a route for your API
app.get('/api', function(req, res){
    // Your API logic will go here
    res.json({ message: 'Welcome to our API!' });
});

// Start the express application
app.listen(port, function(){
    console.log('Spotify App listening on port ' + port);
});