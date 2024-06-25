import sqlite3

def create_tables():
    conn = sqlite3.connect('assignment3.db')
    cursor = conn.cursor()
# Create new table called "COURSE"
    cursor.execute('''CREATE TABLE IF NOT EXISTS COURSE (
        CRN INTEGER PRIMARY KEY,
        TITLE TEXT NOT NULL,
        DEPARTMENT TEXT NOT NULL,
        TIME TEXT NOT NULL,
        DAYS TEXT NOT NULL,
        SEMESTER TEXT NOT NULL,
        YEAR INTEGER NOT NULL,
        CREDITS INTEGER NOT NULL
    )''')

    conn.commit()
    conn.close()

# Creating User Class
class User:
    def __init__(self, first_name, last_name, wentworthID):
        self.first_name = first_name
        self.last_name = last_name
        self.wentworthID = wentworthID

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_wentworthID(self, wentworthID):
        self.wentworthID = wentworthID

    def show_all_info(self):
        return 'Firstname:{}, Lastname:{}, Wentworth ID:{},'.format(self.first_name, self.last_name, self.wentworthID)


# Creating Student Class
class Student(User):
    def search_course(self):
        print('\nStudent Search Course Method')

    def add_drop_course(self):
        print('\nStudent Add/Drop Course Method')

    def show_schedule(self):
        print('\nStudent Print Schedule Method')


# Creating Instructor Class
class Instructor(User):
    # Overwriting User Classes Wentworth ID Attribute
    def __init__(self, first_name, last_name, wentworthID=None):
        super().__init__(first_name, last_name, wentworthID)

        # Sets wentworthID to "N/A" if no wentworthID is given as parameter
        if wentworthID is None:
            self.wentworthID = 'N/A'

    def show_schedule(self):
        print('\nInstructor Print Schedule Method')

    def show_class_list(self):
        print('\nInstructor Print Class List Method')

    def search_course(self):
        print('\nInstructor Search Course Method')


# Creating Admin Class
class Admin(User):
    # Overwriting User Classes Wentworth ID Attribute
    def __init__(self, first_name, last_name, wentworthID=None):
        super().__init__(first_name, last_name, wentworthID)

        # Sets wentworthID to "N/A" if no wentworthID is given as parameter
        if wentworthID is None:
            self.wentworthID = 'N/A'

    def add_course(crn, title, department, time, days, semester, year, credits):
        db = sqlite3.connect('assignment3.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO COURSE VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (crn, title, department, time, days, semester, year, credits))
        db.commit()
        db.close()
        print(f"Course {title} added.")

    def remove_course(self):
        print('\nAdmin Remove Course Method')

    def add_user(first_name, last_name, wentworthID):
        conn = sqlite3.connect('assignment3.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USER VALUES (?, ?, ?)",
                       (first_name, last_name, wentworthID))
        conn.commit()
        conn.close()

    def remove_user(self):
        print('\nAdmin Remove User Method')

    def add_student(student_id, first_name, last_name, grad_year, major, email):
        conn = sqlite3.connect('assignment3.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?)",
                       (student_id, first_name, last_name, grad_year, major, email))
        conn.commit()
        conn.close()

    def remove_student(self):
        print('\nAdmin Remove Student Method') # From Course

    def query_students():
        conn = sqlite3.connect('assignment3.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENT")
        students = cursor.fetchall()
        for student in students:
            print(student)
        conn.close()

    def query_instructors():
        conn = sqlite3.connect('assignment3.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM INSTRUCTOR")
        instructors = cursor.fetchall()
        for instructor in instructors:
            print(instructor)
        conn.close()

    def query_admins():
        conn = sqlite3.connect('assignment3.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ADMIN")
        admins = cursor.fetchall()
        for admin in admins:
            print(admin)
        conn.close()

    def search_roster(self):
        print('\nAdmin Search Roster Method')

    def show_roster(self):
        print('\nAdmin Print Roster Method')

    def search_course(self):
        print('\nAdmin Search Course Method')

    def show_course(self):
        print('\nAdmin Print Course Method')

    def update_admin():
        admin_id = int(input("Enter Admin ID: "))
        new_title = input("Enter the new title: ")

        conn = sqlite3.connect('assignment3.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE ADMIN SET TITLE = ? WHERE ID = ?", (new_title, admin_id))
        conn.commit()
        conn.close()
        print(f"Admin with ID {admin_id} updated to {new_title}.")

    def remove_instructor(instructor_id):
        conn = sqlite3.connect('assignment3.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = ?", (instructor_id,))
        conn.commit()
        conn.close()
        print(f"Instructor with ID {instructor_id} removed.")