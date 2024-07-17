import unittest
import sqlite3
import main
from unittest.mock import patch


class TestFunction(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Create the tables and add some test data
        cls.conn = sqlite3.connect('database.db')
        cls.cursor = cls.conn.cursor()
        main.create_COURSE_table()
        main.create_STUDENT_COURSE_table()

        # Clear existing data to avoid unique constraint violation
        cls.cursor.execute("DELETE FROM COURSE")
        cls.cursor.execute("DELETE FROM STUDENT_COURSE")

        # Add test data
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES"
                            " (10001, 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4)")
        cls.cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES"
                            " (10002, 'Intro to Walking', 'BSEE', '0800', 'TTH', 'Summer', 2024, 4)")
        cls.cursor.execute("INSERT INTO STUDENT_COURSE (WENTWORTHID, CRN) VALUES ('W00409648', 10001)")

        cls.conn.commit()

        # Create a student object
        cls.student = main.Student('Jon', 'Binder', 'W00409648', 'password', major='BSCE', grad_year=2025)

    @classmethod
    def tearDownClass(cls):
        # Drop the COURSE table after tests
        cls.cursor.execute("DROP TABLE IF EXISTS COURSE")
        cls.cursor.execute("DROP TABLE IF EXISTS STUDENT_COURSE")

        cls.conn.commit()
        cls.conn.close()

    @patch('main.is_crn_unique',
           return_value=(('10002', 'Intro to Walking', 'BSEE', '0800', 'TTH', 'Summer', 2024, 4), '10002'))
    def test_student_add_course(self, mock_is_crn_unique):
        # Run the drop course method
        self.student.add_course()

        # Verify the course was added to the database
        self.cursor.execute("SELECT CRN FROM STUDENT_COURSE WHERE WENTWORTHID = 'W00409648' AND CRN = 10002")
        course = self.cursor.fetchone()
        self.assertIsNotNone(course)

    @patch('main.is_crn_unique',
           return_value=(('10001', 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4), '10001'))
    def test_student_drop_course(self, mock_is_crn_unique):
        # Run the drop course method
        self.student.drop_course()

        # Verify the course was removed from the database
        self.cursor.execute("SELECT CRN FROM STUDENT_COURSE WHERE WENTWORTHID = 'W00409648' AND CRN = 10001")
        course = self.cursor.fetchone()
        self.assertIsNone(course)


if __name__ == '__main__':
    unittest.main(verbosity=2)
