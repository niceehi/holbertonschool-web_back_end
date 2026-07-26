import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2];

    readDatabase(database)
      .then((students) => {
        let response = 'This is the list of our students';

        Object.keys(students)
          .sort((a, b) => a.localeCompare(b))
          .forEach((field) => {
            response += `\nNumber of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`;
          });

        res.status(200).send(response);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((students) => {
        res.status(200).send(`List: ${students[major].join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
