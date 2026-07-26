import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.trim().split('\n').slice(1);
    const students = {};

    lines.forEach((line) => {
      const parts = line.split(',');
      const firstname = parts[0];
      const field = parts[3];

      if (!students[field]) {
        students[field] = [];
      }

      students[field].push(firstname);
    });

    resolve(students);
  });
});

export default readDatabase;
