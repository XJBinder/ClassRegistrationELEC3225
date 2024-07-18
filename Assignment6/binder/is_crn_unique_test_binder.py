import unittest
import sqlite3
from main import is_crn_unique, create_COURSE_table
from unittest.mock import patch
from io import StringIO


class TestFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create the tables and add some test data
        cls.conn = sqlite3.connect('database.db')
        cls.cursor = cls.conn.cursor()
        create_COURSE_table()

        # Clear existing data to avoid unique constraint violation
        cls.cursor.execute("DELETE FROM COURSE")

        # Add test data to database
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES ("
                           "'10001', 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4)")

        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Drop the COURSE table after tests
        cls.cursor.execute("DROP TABLE IF EXISTS COURSE")

        cls.conn.commit()
        cls.conn.close()

    # Test is_crn_unique function if user enters 'EXIT' (All caps)
    @patch('builtins.input', return_value='EXIT')
    def test_is_crn_unique_AllCaps(self, mock_input):
        # Call the function and get the actual return value
        actual_value = is_crn_unique()

        # Assert that the actual return value matches the expected value
        self.assertEqual(actual_value, (0, None))

    # Test is_crn_unique function if user enters 'eXiT' (Mixed caps)
    @patch('builtins.input', return_value='eXiT')
    def test_is_crn_unique_mixedCaps(self, mock_input):
        # Call the function and get the actual return value
        actual_value = is_crn_unique()

        # Assert that the actual return value matches the expected value
        self.assertEqual(actual_value, (0, None))

    # Test is_crn_unique function if user enters 'exit' (All lowercase)
    @patch('builtins.input', return_value='exit')
    def test_is_crn_unique_lower(self, mock_input):
        # Call the function and get the actual return value
        actual_value = is_crn_unique()

        # Assert that the actual return value matches the expected value
        self.assertEqual(actual_value, (0, None))

    # Test is_crn_unique function if user enters a course not in the database
    @patch('builtins.input', return_value='69')
    def test_is_crn_unique_course_nonexistent(self, mock_input):
        # Call the function and get the actual return value
        actual_value = is_crn_unique()

        # Assert that the actual return value matches the expected value
        self.assertEqual(actual_value, (None, '69'))

    # Test is_crn_unique function if user enters a course in the database
    @patch('builtins.input', return_value='10001')
    def test_is_crn_unique_course_existent(self, mock_input):
        expected_value = ((10001, 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4), '10001')

        # Call the function and get the actual return value
        actual_value = is_crn_unique()

        # Assert that the actual return value matches the expected value
        self.assertEqual(actual_value, expected_value)

    # Test is_crn_unique function if user enters 'fifty-two' (Not an integer)
    @patch('builtins.input', side_effect=['fifty-two', 'exit'])
    def test_is_crn_unique_non_integer_input(self, mock_input):
        # Capture the output of the print statements
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = is_crn_unique()
            output = mock_stdout.getvalue()

        # Check that the function prints the correct message for non-integer input
        self.assertIn("CRN must be a number.", output)

        # Check that the function returns the correct value when 'exit' is entered
        self.assertEqual(result, (0, None))


if __name__ == '__main__':
    unittest.main(verbosity=2)
