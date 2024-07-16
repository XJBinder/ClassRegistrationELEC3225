import unittest
import sqlite3
from main import create_COURSE_table, create_STUDENT_table, create_STUDENT_COURSE_table, Student


class TestCourseManagement(unittest.TestCase):

    def setUp(self):
        # Use an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        create_COURSE_table(self.cursor)
        create_STUDENT_table(self.cursor)
        create_STUDENT_COURSE_table(self.cursor)

        # Dynamically add a test student and a test course
        self.test_student_id = '123'
        self.test_course_crn = 101
        self.cursor.execute(
            "INSERT INTO STUDENT (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD) VALUES (?, 'John', 'Doe', 'password')",
            (self.test_student_id,))
        self.cursor.execute(
            "INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (?, 'Math 101', "
            "'MATH', '09:00', 'MWF', 'Fall', 2024, 3)",
            (self.test_course_crn,))

        self.conn.commit()

    def tearDown(self):
        # Close the in-memory database connection
        self.conn.close()

    def test_add_course(self):
        student = Student('John', 'Doe', self.test_student_id, 'password')
        student.add_course()

        self.cursor.execute("SELECT * FROM STUDENT_COURSE WHERE WENTWORTHID = ? AND CRN = ?",
                            (self.test_student_id, self.test_course_crn))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], self.test_student_id)
        self.assertEqual(result[1], self.test_course_crn)

    def test_remove_course(self):
        student = Student('John', 'Doe', self.test_student_id, 'password')
        student.add_course()
        student.drop_course()

        self.cursor.execute("SELECT * FROM STUDENT_COURSE WHERE WENTWORTHID = ? AND CRN = ?",
                            (self.test_student_id, self.test_course_crn))
        result = self.cursor.fetchone()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
