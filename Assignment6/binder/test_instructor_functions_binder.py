import unittest
from unittest.mock import patch
import sqlite3
from main import create_COURSE_table, create_STUDENT_table, create_STUDENT_COURSE_table, create_INSTRUCTOR_table, Instructor


class TestInstructorFunctions(unittest.TestCase):

    def setUp(self):
        # Setup database and tables
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        create_COURSE_table(self.cursor)
        create_STUDENT_table(self.cursor)
        create_STUDENT_COURSE_table(self.cursor)
        create_INSTRUCTOR_table(self.cursor)

        # Add a test instructor, a test student, and a test course
        self.cursor.execute(
            "INSERT INTO INSTRUCTOR (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, DEPARTMENT) VALUES ('456', 'Jane', "
            "'Smith', 'password', 'MATH')")
        self.cursor.execute(
            "INSERT INTO STUDENT (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD) VALUES ('123', 'John', 'Doe', 'password')")
        self.cursor.execute(
            "INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (101, "
            "'Math 101', 'MATH', '09:00', 'MWF', 'Fall', 2024, 3)")
        self.cursor.execute("INSERT INTO STUDENT_COURSE (WENTWORTHID, CRN) VALUES ('123', 101)")

    def tearDown(self):
        self.conn.close()

    @patch('builtins.input', side_effect=['101'])
    def test_show_roster(self, mock_input):
        instructor = Instructor('Jane', 'Smith', '456', 'password')
        roster = instructor.show_roster()

        expected_output = "John Doe"
        self.assertIn(expected_output, roster)


if __name__ == '__main__':
    unittest.main()
