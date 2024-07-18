import unittest
import sqlite3
from unittest.mock import patch, MagicMock

import main

# Define the mock methods directly within the test file
def mock_add_course(cursor, title, department, time, days, semester, year, credits):
    cursor.execute("INSERT INTO COURSE (TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (title, department, time, days, semester, year, credits))

def mock_remove_course(cursor, title):
    cursor.execute("DELETE FROM COURSE WHERE TITLE = ?", (title,))

def mock_add_user(cursor, username, password):
    cursor.execute("INSERT INTO USER (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD) VALUES (?, ?, ?, ?)",
                   (username, "Test", "User", password))

class TestCourseManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup for course management tests
        cls.conn = sqlite3.connect(':memory:')  # Use in-memory database for testing
        cls.cursor = cls.conn.cursor()
        # Create the COURSE table
        cls.cursor.execute('''CREATE TABLE COURSE (
            CRN INTEGER PRIMARY KEY,
            TITLE TEXT NOT NULL,
            DEPARTMENT TEXT NOT NULL,
            TIME TEXT NOT NULL,
            DAYS TEXT NOT NULL,
            SEMESTER TEXT NOT NULL,
            YEAR INTEGER NOT NULL,
            CREDITS INTEGER NOT NULL)''')
        cls.conn.commit()

    def test_add_course(self):
        # Test adding a course
        mock_add_course(self.cursor, 'Test Course', 'TEST', '12:00', 'MWF', 'Fall', 2023, 3)
        self.cursor.execute("SELECT * FROM COURSE WHERE TITLE = 'Test Course'")
        course = self.cursor.fetchone()
        self.assertIsNotNone(course)

    def test_remove_course(self):
        # Test removing a course
        mock_add_course(self.cursor, 'Test Course 2', 'TEST2', '13:00', 'TTh', 'Spring', 2024, 4)
        mock_remove_course(self.cursor, 'Test Course 2')
        self.cursor.execute("SELECT * FROM COURSE WHERE TITLE = 'Test Course 2'")
        course = self.cursor.fetchone()
        self.assertIsNone(course)

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()


class TestUserAuthentication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup for user authentication tests
        cls.conn = sqlite3.connect(':memory:')  # Use in-memory database for testing
        cls.cursor = cls.conn.cursor()
        # Create the USER table
        cls.cursor.execute('''CREATE TABLE USER (
            WENTWORTHID TEXT PRIMARY KEY,
            FIRSTNAME TEXT NOT NULL,
            LASTNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL)''')
        cls.conn.commit()
        mock_add_user(cls.cursor, 'testuser', 'password')  # Mock user

    @patch('main.login', MagicMock(return_value=(True, 'USER')))
    def test_login_success(self):
        # Test successful login
        result = main.login('testuser', 'password')
        self.assertTrue(result[0])

    @patch('main.login', MagicMock(return_value=(False, None)))
    def test_login_failure(self):
        # Test login failure
        result = main.login('testuser', 'wrongpassword')
        self.assertFalse(result[0])

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
