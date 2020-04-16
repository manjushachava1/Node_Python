/* eslint-disable linebreak-style */
/* eslint-disable no-console */
const express = require('express');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  // let dataToSend;
  const largeDataSet = [];
  // spawn new child process to call the python script
  // const python = spawn('python', ['script3.py']);

  // Putting two parameters into the fricken script
  // const python = spawn('python', ['script2.py', 'first', 'second']);
  const python = spawn('python', ['my_test.py']);

  // collect data from script
  python.stdout.on('data', (data) => {
    console.log('Pipe data from python script ...');
    // dataToSend =  data;
    largeDataSet.push(data);
  });
  // in close event we are sure that stream is from child process is closed
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.send(largeDataSet.join(''));
  });
});
app.listen(port, () => console.log(`Example app listening on port 
${port}!`));
