import unittest
import sqlite3
import main
import io
from contextlib import redirect_stdout
from unittest.mock import patch


class TestFunction(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Create the COURSE table and add some test data
        cls.conn = sqlite3.connect('database.db')
        cls.cursor = cls.conn.cursor()
        main.create_COURSE_table()
        main.create_STUDENT_table()
        main.create_STUDENT_COURSE_table()
        main.create_INSTRUCTOR_table()

        # Clear existing data to avoid unique constraint violation
        cls.cursor.execute("DELETE FROM COURSE")
        cls.cursor.execute("DELETE FROM STUDENT")
        cls.cursor.execute("DELETE FROM STUDENT_COURSE")
        cls.cursor.execute("DELETE FROM INSTRUCTOR")
        cls.conn.commit()

        # Add test data
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES"
                           " (10001, 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4)")
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES"
                           " (10002, 'Intro to Walking', 'BSEE', '0800', 'TTH', 'Summer', 2024, 4)")
        cls.cursor.execute("INSERT INTO STUDENT_COURSE (WENTWORTHID, CRN) VALUES ('W00409648', 10001)")

        # Create test objects
        cls.student = main.Student('W00409648', 'Jon', 'Binder', 'password', 'N/A', 2025, 'BSCE')
        cls.instructor = main.Instructor('W60606060', 'Douglas', 'Dow', 'password', 'BSCE', 2005,
                                         'Professor', 'ddow@wit.edu')
        cls.conn.commit()

    @classmethod
    def tearDown(cls):
        # Drop the COURSE table after tests
        cls.cursor.execute("DROP TABLE IF EXISTS COURSE")
        cls.cursor.execute("DROP TABLE IF EXISTS STUDENT_COURSE")
        cls.conn.commit()
        cls.conn.close()

    def test_student_add_course(self):
        # Capture the output of the add_course Method
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            self.student.add_course()
        output = captured_output.getvalue()

        # Check if Add Course is in the output
        self.assertIn('\n--Add Course--', output)

    def test_student_drop_course(self):
        # Capture the output of the drop_course Method
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            self.student.drop_course()
        output = captured_output.getvalue()

        # Check if Drop Course is in the output
        self.assertIn('\n--Drop Course--', output)

    # @patch('builtins.input', side_effect=['', 'Math 101', '', ''])
    # def test_search_roster(self, mock_input):
    #     # Test searching by title
    #     captured_output = io.StringIO()
    #     with redirect_stdout(captured_output):
    #         main.search_roster()
    #     output = captured_output.getvalue()
    #
    #     # Check if the correct course is found
    #     self.assertIn('Math 101', output)
    #     self.assertNotIn('History 101', output)
    #     self.assertNotIn('Biology 101', output)
    #
    # @patch('builtins.input', side_effect=['', '', 'MWF', ''])
    # def test_show_roster(self, mock_input):
    #     # Test searching by day
    #     captured_output = io.StringIO()
    #     with redirect_stdout(captured_output):
    #         main.show_roster()
    #     output = captured_output.getvalue()
    #
    #     # Check if the correct courses are found
    #     self.assertIn('Math 101', output)
    #     self.assertNotIn('History 101', output)
    #     self.assertIn('Biology 101', output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
