import unittest
# Author - Carson Mershon
import sqlite3
from main import create_COURSE_table, show_all_courses, search_course
import io
import sys
from contextlib import redirect_stdout
from unittest.mock import patch

class TestCourseSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create the COURSE table and add some test data
        cls.conn = sqlite3.connect('database.db')
        cls.cursor = cls.conn.cursor()
        create_COURSE_table()

        # Clear existing data to avoid unique constraint violation
        cls.cursor.execute("DELETE FROM COURSE")
        cls.conn.commit()

        # Add test data
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (1001, 'Math 101', 'MATH', '0900', 'MWF', 'Fall', 2023, 3)")
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (1002, 'History 101', 'HIST', '1000', 'TTh', 'Fall', 2023, 3)")
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (1003, 'Biology 101', 'BIOL', '1100', 'MWF', 'Fall', 2023, 4)")
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Drop the COURSE table after tests
        cls.cursor.execute("DROP TABLE IF EXISTS COURSE")
        cls.conn.commit()
        cls.conn.close()

    def test_show_all_courses(self):
        # Capture the output of show_all_courses
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            show_all_courses()
        output = captured_output.getvalue()

        # Check if all courses are in the output
        self.assertIn('Math 101', output)
        self.assertIn('History 101', output)
        self.assertIn('Biology 101', output)

    @patch('builtins.input', side_effect=['', 'Math 101', '', ''])
    def test_search_course_by_title(self, mock_input):
        # Test searching by title
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            search_course()
        output = captured_output.getvalue()

        # Check if the correct course is found
        self.assertIn('Math 101', output)
        self.assertNotIn('History 101', output)
        self.assertNotIn('Biology 101', output)

    @patch('builtins.input', side_effect=['', '', 'MWF', ''])
    def test_search_course_by_day(self, mock_input):
        # Test searching by day
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            search_course()
        output = captured_output.getvalue()

        # Check if the correct courses are found
        self.assertIn('Math 101', output)
        self.assertNotIn('History 101', output)
        self.assertIn('Biology 101', output)

    @patch('builtins.input', side_effect=['', '', '', '1000'])
    def test_search_course_by_time(self, mock_input):
        # Test searching by time
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            search_course()
        output = captured_output.getvalue()

        # Check if the correct course is found
        self.assertNotIn('Math 101', output)
        self.assertIn('History 101', output)
        self.assertNotIn('Biology 101', output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
