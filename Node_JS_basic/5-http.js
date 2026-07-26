const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    const originalLog = console.log;
    let output = '';

    console.log = (message) => {
      output += `${message}\n`;
    };

    countStudents(database)
      .then(() => {
        console.log = originalLog;
        res.end(output.trim());
      })
      .catch(() => {
        console.log = originalLog;
        res.end('Cannot load the database');
      });

    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('Not Found');
});

app.listen(1245);

module.exports = app;
