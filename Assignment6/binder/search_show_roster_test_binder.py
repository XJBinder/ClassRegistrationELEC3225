import unittest
import sqlite3
import main
from unittest.mock import patch
from io import StringIO


class TestFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create the tables and add some test data
        cls.conn = sqlite3.connect('database.db')
        cls.cursor = cls.conn.cursor()
        main.create_COURSE_table()
        main.create_INSTRUCTOR_table()
        main.create_STUDENT_COURSE_table()
        main.create_STUDENT_table()

        # Clear existing data to avoid unique constraint violation
        cls.cursor.execute("DELETE FROM COURSE")
        cls.cursor.execute("DELETE FROM STUDENT")
        cls.cursor.execute("DELETE FROM INSTRUCTOR")
        cls.cursor.execute("DELETE FROM STUDENT_COURSE")

        # Add test data to database
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES ("
                           "'10001', 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4)")
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES ("
                           "'10002', 'Intro to Walking', 'BSEE', '0800', 'TTH', 'Summer', 2024, 4)")
        cls.cursor.execute("INSERT INTO STUDENT (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, GRADYEAR, MAJOR, "
                           "EMAIL) VALUES ('W00409648', 'Jon', 'Binder', 'password', '2025', 'BSEE', "
                           "'binderj@wit.edu')")
        cls.cursor.execute("INSERT INTO STUDENT (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, GRADYEAR, MAJOR, "
                           "EMAIL) VALUES ('W84690400', 'Carson', 'Mershon', 'password', '2037', 'BSCE', "
                           "'cpmershon@wit.edu')")
        cls.cursor.execute("INSERT INTO INSTRUCTOR (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, DEPARTMENT, HIREYEAR, "
                           "TITLE, EMAIL) VALUES ('W69696969', 'Professor', 'Bean', 'password', 'BSEE', 1940, "
                           "'Professor', 'beanp@wit.edu')")
        cls.cursor.execute("INSERT INTO INSTRUCTOR (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, DEPARTMENT, HIREYEAR, "
                           "TITLE, EMAIL) VALUES ('W12345678', 'Uneducated', 'Man', 'password', 'BSCE', 1875, "
                           "'Professor', 'uneducatedm@wit.edu')")
        cls.cursor.execute("INSERT INTO STUDENT_COURSE (WENTWORTHID, CRN) VALUES ('W00409648', 10001)")
        cls.cursor.execute("INSERT INTO STUDENT_COURSE (WENTWORTHID, CRN) VALUES ('W00409648', 10002)")
        cls.cursor.execute("INSERT INTO STUDENT_COURSE (WENTWORTHID, CRN) VALUES ('W84690400', 10001)")

        cls.conn.commit()

        # Create instructor object to access instructor methods
        cls.instructor = main.Instructor('Instructor', 'Object', 'W00000000', 'password', None, None, None, None)

    @classmethod
    def tearDownClass(cls):
        # Drop the COURSE table after tests
        cls.cursor.execute("DROP TABLE IF EXISTS COURSE")
        cls.cursor.execute("DROP TABLE IF EXISTS STUDENT")
        cls.cursor.execute("DROP TABLE IF EXISTS INSTRUCTOR")
        cls.cursor.execute("DROP TABLE IF EXISTS STUDENT_COURSE")

        cls.conn.commit()
        cls.conn.close()

    @patch('main.is_crn_unique',
           return_value=(('10001', 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4), '10001'))
    def test_instructor_show_roster(self, mock_is_crn_unique):
        # Capture the output of the print statements
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.instructor.show_roster()
            output = mock_stdout.getvalue()

        expected_output = (
            "Roster for How to Breathe:\n"
            "\nInstructors that can teach this course:\n"
            "Professor Uneducated Man, Email:uneducatedm@wit.edu\n"
            "\nStudents taking How to Breathe:\n"
            "Jon Binder, Email:binderj@wit.edu\n"
            "Carson Mershon, Email:cpmershon@wit.edu\n"
        )
        self.assertEqual(output, expected_output)

    @patch('main.is_crn_unique',
           return_value=(('10002', 'Intro to Walking', 'BSEE', '0800', 'TTH', 'Summer', 2024, 4), '10002'))
    @patch('builtins.input', return_value='W00409648')
    def test_instructor_search_roster(self, mock_input, mock_is_crn_unique):
        # Capture the output of the print statements
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.instructor.search_roster()
            output = mock_stdout.getvalue()

        expected_output = (
            "Firstname: Jon, Lastname: Binder, Wentworth ID: W00409648\n"
        )
        self.assertIn(expected_output, output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
