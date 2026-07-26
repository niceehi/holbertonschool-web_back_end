const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.status(200).type('text').send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const originalLog = console.log;
  let output = '';

  console.log = (msg) => {
    output += `${msg}\n`;
  };

  countStudents(database)
    .then(() => {
      console.log = originalLog;
      res
        .status(200)
        .type('text')
        .send(`This is the list of our students\n${output.trim()}`);
    })
    .catch(() => {
      console.log = originalLog;
      res
        .status(200)
        .type('text')
        .send('This is the list of our students\nCannot load the database');
    });
});

app.listen(1245);

module.exports = app;
