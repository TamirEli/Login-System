const myModule = require('./data manager.js');
const net = require('net');

const server = net.createServer((socket) => {
  console.log('Client connected');

  // Handle data received from the client
  socket.on('data', (data) => {
    console.log(`Received from client: ${data}`);
    // Send a response back to the client
    socket.write('Hello from server!');
  });

  // Handle client disconnection
  socket.on('end', () => {
    console.log('Client disconnected');
  });
});

// Listen on a specific port
const PORT = 334;
server.listen(PORT, () => {
});