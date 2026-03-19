const net = require('net');

// Connect to the server
const client = net.createConnection({ port: 334 }, () => {
  console.log('Connected to server');
  
  // Send data to the server
  client.write('Hello from Eyal!');
});

// Handle data received from the server
client.on('data', (data) => {
  console.log(`Received from server: ${data}`);
  
  // Close the connection after receiving a response
  client.end(); 
});

// Handle connection closure
client.on('end', () => {
  console.log('Disconnected from server');
});
