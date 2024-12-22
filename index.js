const express = require('express');
const app = express();


//this is a handler that processes the request and tells the server about which response to send
app.get('/', (req, res) => {
    res.send('cf paula');
});


//server expects calls made to 3000.
//the client makes the get request and the server send the response
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
