import sqlite3


def create_COURSE_table():
    conn = sqlite3.connect('database.db')
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
        CREDITS INTEGER NOT NULL)''')

    conn.commit()
    conn.close()


def create_USER_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "USER"
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
        WENTWORTHID TEXT PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL)''')

    conn.commit()
    conn.close()


def create_STUDENT_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "STUDENT"
    cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT (
        WENTWORTHID TEXT PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        COURSES INTEGER,
        GRADYEAR INTEGER,
        MAJOR TEXT,
        EMAIL TEXT)''')

    conn.commit()
    conn.close()


def create_STUDENT_COURSE_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "STUDENT_COURSE"
    cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT_COURSE (
        WENTWORTHID TEXT NOT NULL,
        CRN INTEGER NOT NULL,
        PRIMARY KEY(WENTWORTHID, CRN),
        FOREIGN KEY(WENTWORTHID) REFERENCES STUDENT(WENTWORTHID),
        FOREIGN KEY(CRN) REFERENCES COURSE(CRN))''')

    conn.commit()
    conn.close()


def create_INSTRUCTOR_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "INSTRUCTOR"
    cursor.execute('''CREATE TABLE IF NOT EXISTS INSTRUCTOR (
        WENTWORTHID TEXT PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        DEPARTMENT TEXT,
        HIREYEAR INTEGER,
        TITLE TEXT,
        EMAIL TEXT)''')

    conn.commit()
    conn.close()


def create_ADMIN_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create new table called "ADMIN"
    cursor.execute('''CREATE TABLE IF NOT EXISTS ADMIN (
        WENTWORTHID TEXT PRIMARY KEY,
        FIRSTNAME TEXT NOT NULL,
        LASTNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        TITLE TEXT,
        OFFICE TEXT,
        EMAIL TEXT)''')

    conn.commit()
    conn.close()


def login(wentworth_id, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # List of tables to check
    tables = ['USER', 'STUDENT', 'INSTRUCTOR', 'ADMIN']
    account_exists = False

    for table in tables:
        cursor.execute(f"SELECT * FROM {table} WHERE WENTWORTHID = ?", (wentworth_id,))
        account = cursor.fetchone()

        if account is not None:
            account_exists = True
            if account[3] != password:
                print("Password Incorrect")
                return None, None
            else:
                print(f"Logged in as {account[1]}")
                return account, table

    if not account_exists:
        print("Account does not exist")

    conn.close()
    return None, None


def get_user_input(max_choice):
    while True:
        try:
            user_input = int(input("Select an Option: "))
            if not 1 <= user_input <= max_choice:
                print("Invalid Entry")
                continue
            else:
                return user_input
        except ValueError:
            print("Invalid Entry")


def search_course():
    crn = input("Enter CRN (or press Enter to skip): ")
    title = input("Enter Title (or press Enter to skip): ")
    day = input("Enter Day (or press Enter to skip): ")
    time = input("Enter Time (or press Enter to skip): ")

    crn = None if crn == "" else crn
    title = None if title == "" else title
    day = None if day == "" else day
    time = None if time == "" else time

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM COURSE WHERE 1"
    params = []

    if crn is not None:
        query += " AND CRN LIKE ?"
        params.append('%' + crn + '%')

    if title is not None:
        query += " AND TITLE LIKE ?"
        params.append('%' + str(title) + '%')

    if day is not None:
        query += " AND DAYS LIKE ?"
        params.append('%' + day + '%')

    if time is not None:
        query += " AND TIME LIKE ?"
        params.append('%' + time + '%')

    cursor.execute(query, params)

    courses = cursor.fetchall()
    for course in courses:
        print(course)

    conn.close()


def show_all_courses():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM COURSE")
    courses = cursor.fetchall()
    for course in courses:
        print(course)

    conn.close()


def is_crn_unique():
    while True:
        crn = input("Enter CRN (or 'exit' to cancel): ")
        if crn.lower() == 'exit':
            return 0, None

        if not crn.isdigit():
            print("CRN must be a number.")
            continue

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (crn,))
        course = cursor.fetchone()

        conn.close()

        return course, crn


def main_menu():
    print("\n---Welcome to Leopard Web Class Registration Software---")
    print("1. Login")
    print("2. Create Account")

    choice = get_user_input(2)

    if choice == 1:
        print("\n---Login---")
        wentworth_id = input("Enter your Wentworth ID: ")
        password = input("Enter your Password: ")
        fetched_account, fetched_account_type = login(wentworth_id, password)

        if fetched_account is None:
            print("Login failed. Please try again.")
            return main_menu()

        if fetched_account_type == 'USER':
            user = 0
            user_object = User(fetched_account[1], fetched_account[2], fetched_account[0], fetched_account[3])
            return user, user_object

        elif fetched_account_type == 'STUDENT':
            user = 1
            user_object = Student(fetched_account[1], fetched_account[2], fetched_account[0],
                                  fetched_account[3], fetched_account[4], fetched_account[5],
                                  fetched_account[6], fetched_account[7])
            return user, user_object

        elif fetched_account_type == 'INSTRUCTOR':
            user = 2
            user_object = Instructor(fetched_account[1], fetched_account[2], fetched_account[0],
                                     fetched_account[3], fetched_account[4], fetched_account[5],
                                     fetched_account[6], fetched_account[7])
            return user, user_object

        elif fetched_account_type == 'ADMIN':
            user = 3
            user_object = Admin(fetched_account[1], fetched_account[2], fetched_account[0],
                                fetched_account[3], fetched_account[4], fetched_account[5],
                                fetched_account[6])
            return user, user_object

    elif choice == 2:
        print("\n---Account Type---")
        print("1. Student")
        print("2. Instructor")
        print("3. Admin")
        print("4. Parent/Other (User)")
        account_type = get_user_input(4)

        # If User is Selected
        if account_type == 4:
            print('\n--Create User Account--')
            user = 0
            first_name = input("Enter your First Name: ")
            last_name = input("Enter your Last Name: ")
            wentworth_id = input("Enter your Wentworth ID: ")
            password = input("Enter your Password: ")

            user_object = User(first_name, last_name, wentworth_id, password)
            user_object.add_to_database()

            return user, user_object

        # If Student is Selected
        elif account_type == 1:
            print('\n--Create Student Account--')
            user = 1
            first_name = input("Enter your First Name: ")
            last_name = input("Enter your Last Name: ")
            wentworth_id = input("Enter your Wentworth ID: ")
            password = input("Enter your Password: ")
            grad_year = input("Enter your Graduation Year: ")
            major = input("Enter your Major: ")
            email = input("Enter your Email: ")

            user_object = Student(first_name, last_name, wentworth_id, password, None, grad_year, major, email)
            user_object.add_to_database()

            return user, user_object

        # If Instructor is Selected
        elif account_type == 2:
            print('\n--Create Instructor Account--')
            user = 2
            first_name = input("Enter your First Name: ")
            last_name = input("Enter your Last Name: ")
            wentworth_id = input("Enter your Wentworth ID: ")
            password = input("Enter your Password: ")
            department = input("Enter your Department: ")
            hire_year = input("Enter your Hire Year: ")
            title = input("Enter your Title: ")
            email = input("Enter your Email: ")

            user_object = Instructor(first_name, last_name, wentworth_id, password, department, hire_year, title,
                                     email)
            user_object.add_to_database()

            return user, user_object

        # If Admin is Selected
        elif account_type == 3:
            print('\n--Create Admin Account--')
            user = 3
            first_name = input("Enter your First Name: ")
            last_name = input("Enter your Last Name: ")
            wentworth_id = input("Enter your Wentworth ID: ")
            password = input("Enter your Password: ")
            title = input("Enter your Title: ")
            office = input("Enter your Office: ")
            email = input("Enter your Email: ")

            user_object = Admin(first_name, last_name, wentworth_id, password, title, office, email)
            user_object.add_to_database()

            return user, user_object


def user_functions(user_object, user_choice):
    if user_choice == 1:
        search_course()

    elif user_choice == 2:
        show_all_courses()

    elif user_choice == 3:
        user_object.show_all_info()

    elif user_choice == 4:
        new_password = input("Enter New Password: ")
        user_object.set_password(new_password)


def student_functions(user_object, user_choice):
    if user_choice == 1:
        search_course()

    elif user_choice == 2:
        show_all_courses()

    elif user_choice == 3:
        user_object.add_course()

    elif user_choice == 4:
        user_object.drop_course()

    elif user_choice == 5:
        user_object.show_schedule()

    elif user_choice == 6:
        user_object.show_all_info()

    elif user_choice == 7:
        new_password = input("Enter New Password: ")
        user_object.set_password(new_password)


def instructor_functions(user_object, user_choice):
    if user_choice == 1:
        search_course()

    elif user_choice == 2:
        show_all_courses()

    elif user_choice == 3:
        user_object.search_roster()

    elif user_choice == 4:
        user_object.show_roster()

    elif user_choice == 5:
        user_object.show_all_info()

    elif user_choice == 6:
        new_password = input("Enter New Password: ")
        user_object.set_password(new_password)


def admin_functions(user_object, user_choice):
    if user_choice == 1:
        search_course()

    elif user_choice == 2:
        show_all_courses()

    elif user_choice == 3:
        user_object.search_roster()

    elif user_choice == 4:
        user_object.show_roster()

    elif user_choice == 5:
        user_object.add_course()

    elif user_choice == 6:
        user_object.remove_course()

    elif user_choice == 7:
        user_object.add_user()

    elif user_choice == 8:
        user_object.remove_user()

    elif user_choice == 9:
        user_object.add_student()

    elif user_choice == 10:
        user_object.remove_student()

    elif user_choice == 11:
        user_object.add_instructor()

    elif user_choice == 12:
        user_object.remove_instructor()

    elif user_choice == 13:
        user_object.add_admin()

    elif user_choice == 14:
        user_object.remove_admin()

    elif user_choice == 15:
        user_object.query_users()

    elif user_choice == 16:
        user_object.query_students()

    elif user_choice == 17:
        user_object.query_instructors()

    elif user_choice == 18:
        user_object.query_admins()

    elif user_choice == 19:
        user_object.update_admin()

    elif user_choice == 20:
        user_object.show_all_info()

    elif user_choice == 21:
        new_password = input("Enter New Password: ")
        user_object.set_password(new_password)


def sub_menu(user, user_object):
    while True:
        try:
            if user == 0:  # USER
                print("\n--User Menu--")
                print("1. Search Course")
                print("2. Show All Courses")
                print("3. Show My Info")
                print("4. Change Password")
                print("5. Exit")
                user_choice = get_user_input(5)
                if user_choice == 5:
                    break

                user_functions(user_object, user_choice)

            elif user == 1:  # STUDENT
                print("\n--Student Menu--")
                print("1. Search Course")
                print("2. Show All Courses")
                print("3. Add Course")
                print("4. Drop Course")
                print("5. Show Schedule")
                print("6. Show My Info")
                print("7. Change Password")
                print("8. Exit")
                user_choice = get_user_input(8)
                if user_choice == 8:
                    break

                student_functions(user_object, user_choice)

            elif user == 2:  # INSTRUCTOR
                print("\n--Instructor Menu--")
                print("1. Search Course")
                print("2. Show All Courses")
                print("3. Search Roster")
                print("4. Show Roster")
                print("5. Show My Info")
                print("6. Change Password")
                print("7. Exit")
                user_choice = get_user_input(7)
                if user_choice == 7:
                    break

                instructor_functions(user_object, user_choice)

            elif user == 3:  # ADMIN
                print("\n--Admin Menu--")
                print("1. Search Course")
                print("2. Show All Courses")
                print("3. Search Roster")
                print("4. Show Roster")
                print("5. Add Course")
                print("6, Remove Course")
                print("7. Add User")
                print("8. Remove User")
                print("9. Add Student")
                print("10. Remove Student")
                print("11. Add Instructor")
                print("12. Remove Instructor")
                print("13. Add Admin")
                print("14. Remove Admin")
                print("15. Query Users")
                print("16. Query Students")
                print("17. Query Instructors")
                print("18. Query Admins")
                print("19. Update Admin")
                print("20. Show My Info")
                print("21. Change Password")
                print("22. Exit")
                user_choice = get_user_input(22)
                if user_choice == 22:
                    break

                admin_functions(user_object, user_choice)

        except Exception as e:
            print(f"An Error Occurred: {e}")
        finally:
            input("Press Enter to Exit")


# Creating User Class
class User:
    def __init__(self, first_name, last_name, wentworth_id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.wentworth_id = wentworth_id
        self.password = password

    def set_first_name(self, first_name):
        self.first_name = first_name

        # Update first name in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE USER SET FIRSTNAME = ? WHERE WENTWORTHID = ?", (first_name, self.wentworth_id))

        conn.commit()
        conn.close()

    def set_last_name(self, last_name):
        self.last_name = last_name

        # Update last name in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE USER SET LASTNAME = ? WHERE WENTWORTHID = ?", (last_name, self.wentworth_id))

        conn.commit()
        conn.close()

    def set_wentworth_id(self, wentworth_id):
        self.wentworth_id = wentworth_id

        # Update Wentworth ID in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE USER SET WENTWORTHID = ? WHERE WENTWORTHID = ?", (wentworth_id, self.wentworth_id))

        conn.commit()
        conn.close()

    def set_password(self, password):
        self.password = password

        # Update password in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE USER SET PASSWORD = ? WHERE WENTWORTHID = ?", (password, self.wentworth_id))

        conn.commit()
        conn.close()

    def show_all_info(self):
        return 'Firstname:{}, Lastname:{}, Wentworth ID:{},'.format(self.first_name, self.last_name, self.wentworth_id)

    def add_to_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?)",
                       (self.wentworth_id, self.first_name, self.last_name, self.password))

        conn.commit()
        conn.close()


# Creating Student Class
class Student(User):
    def __init__(self, first_name, last_name, wentworth_id, password, courses=None, grad_year=None, major=None,
                 email=None):
        super().__init__(first_name, last_name, wentworth_id, password)
        self.courses = courses
        self.grad_year = grad_year
        self.major = major
        self.email = email

        if courses is None:
            self.courses = 'N/A'

        if grad_year is None:
            self.grad_year = 'N/A'

        if major is None:
            self.major = 'N/A'

        if email is None:
            self.email = 'N/A'

    def add_course(self):
        print("\n--Add Course--")
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Add the course to the STUDENT_COURSE table
            cursor.execute("INSERT INTO STUDENT_COURSE (WENTWORTHID, CRN) VALUES (?, ?)",
                           (self.wentworth_id, crn))

            conn.commit()
            conn.close()

            print(f"Course {crn} added.")
            break

    def drop_course(self):
        print("\n--Drop Course--")
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Remove the course from the STUDENT_COURSE table
            cursor.execute("DELETE FROM STUDENT_COURSE WHERE WENTWORTHID = ? AND CRN = ?",
                           (self.wentworth_id, crn))

            conn.commit()
            conn.close()

            print(f"Course {crn} dropped.")
            break

    def show_schedule(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Get all the courses for the student
        cursor.execute("SELECT CRN FROM STUDENT_COURSE WHERE WENTWORTHID = ?", (self.wentworth_id,))
        course_ids = cursor.fetchall()

        # Fetch and print the details for each course
        for course_id in course_ids:
            cursor.execute("SELECT TITLE, TIME, DAYS FROM COURSE WHERE CRN = ?", (course_id[0],))
            course = cursor.fetchone()
            if course is not None:
                print(f"Course Name: {course[0]}, Course Time: {course[1]}, Course Days: {course[2]}")

        conn.close()

    def add_to_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (self.wentworth_id, self.first_name, self.last_name, self.password, self.courses, self.grad_year,
                        self.major, self.email))
        conn.commit()
        conn.close()


# Creating Instructor Class
class Instructor(User):
    def __init__(self, first_name, last_name, wentworth_id, password, department=None, hire_year=None, title=None,
                 email=None):
        super().__init__(first_name, last_name, wentworth_id, password)
        self.department = department
        self.hire_year = hire_year
        self.title = title
        self.email = email

        if department is None:
            self.department = 'N/A'

        if hire_year is None:
            self.hire_year = 'N/A'

        if title is None:
            self.title = 'N/A'

        if email is None:
            self.email = 'N/A'

    def search_roster(self):
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            print(f"{course[1]} Roster Search:")
            wentworth_id = input("Enter Wentworth ID:")

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Find the student with the given Wentworth ID who is in the course with the given CRN
            cursor.execute("""
                SELECT STUDENT.* 
                FROM STUDENT 
                JOIN STUDENT_COURSE ON STUDENT.WENTWORTHID = STUDENT_COURSE.WENTWORTHID 
                WHERE STUDENT.WENTWORTHID = ? AND STUDENT_COURSE.CRN = ?
            """, (wentworth_id, crn))
            student = cursor.fetchone()
            if student is not None:
                student_obj = Student(student[1], student[2], student[0], student[3], student[4], student[5],
                                      student[6], student[7])
                print(student_obj.show_all_info())
                return

            # Find the instructor with the given Wentworth ID who is in the course with the given CRN
            cursor.execute("""
                SELECT INSTRUCTOR.* 
                FROM INSTRUCTOR 
                JOIN COURSE ON INSTRUCTOR.DEPARTMENT = COURSE.DEPARTMENT 
                WHERE INSTRUCTOR.WENTWORTHID = ? AND COURSE.CRN = ?
            """, (wentworth_id, crn))
            instructor = cursor.fetchone()
            if instructor is not None:
                instructor_obj = Instructor(instructor[1], instructor[2], instructor[0], instructor[3], instructor[4],
                                            instructor[5], instructor[6], instructor[7])
                print(instructor_obj.show_all_info())
                return

            print(f"No user found with Wentworth ID {wentworth_id} in the course with CRN {crn}")

            conn.close()
            break

    def show_roster(self):
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            print(f"Roster for {course[1]}:")

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Query to find all instructors that have the inputted course
            cursor.execute("""
                        SELECT INSTRUCTOR.*, COURSE.*
                        FROM INSTRUCTOR
                        JOIN COURSE ON INSTRUCTOR.DEPARTMENT = COURSE.DEPARTMENT
                        WHERE COURSE.DEPARTMENT = ?
                    """, (course[2],))
            instructors_with_course = cursor.fetchall()
            print("Instructors that can teach this course:")
            for instructor in instructors_with_course:
                print(instructor)

            # Query to find all students that have the inputted course
            cursor.execute("""
                SELECT STUDENT.*, COURSE.*
                FROM STUDENT
                JOIN COURSE ON STUDENT.COURSES = COURSE.CRN
                WHERE COURSE.CRN = ?
            """, (crn,))
            students_with_course = cursor.fetchall()
            print(f"Students taking {course[1]}:")
            for student in students_with_course:
                print(student)

            conn.close()
            break

    def add_to_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO INSTRUCTOR VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (self.wentworth_id, self.first_name, self.last_name, self.password, self.department,
                        self.hire_year, self.title, self.email))
        conn.commit()
        conn.close()


# Creating Admin Class
class Admin(User):
    def __init__(self, first_name, last_name, wentworth_id, password, title=None, office=None, email=None):
        super().__init__(first_name, last_name, wentworth_id, password)
        self.title = title
        self.office = office
        self.email = email

        if title is None:
            self.title = 'N/A'

        if office is None:
            self.office = 'N/A'

        if email is None:
            self.email = 'N/A'

    def add_course(self):
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            title = input("Enter Title: ")
            department = input("Enter Department: ")
            time = input("Enter Time (ex: 8AM -> 0800, 5:30PM -> 1730) : ")
            days = input("Enter Days (ex: Mon, Wed, Fri -> mwf): ")
            semester = input("Enter Semester: ")
            year = input("Enter Year: ")

            if not year.isdigit():
                print("Year must be a number.")
                break

            credit = input("Enter Credit: ")

            if not credit.isdigit():
                print("Credit must be a number.")
                break

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO COURSE VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (crn, title, department, time, days, semester, year, credit))

            conn.commit()
            conn.close()
            print(f"Course {title} added.")
            break

    def remove_course(self):
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute("DELETE FROM COURSE WHERE CRN = ?", (crn,))

            conn.commit()
            conn.close()

            print(f"Course with CRN {crn} removed.")
            break

    def add_user(self):
        print("\n--Add User--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USER WHERE WENTWORTHID = ?", (wentworth_id,))
        user = cursor.fetchone()

        if user is not None:
            print("User already exists.")
            conn.close()
            return

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        password = input(f"Enter Password for {first_name}: ")

        cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?)",(wentworth_id, first_name, last_name, password))

        conn.commit()
        conn.close()

        print(f"User with Wentworth ID: {wentworth_id} added.")

    def remove_user(self):
        print("\n--Remove User--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USER WHERE WENTWORTHID = ?", (wentworth_id,))
        user = cursor.fetchone()

        if user is None:
            print("User does not exist.")
            conn.close()
            return

        cursor.execute("DELETE FROM USER WHERE WENTWORTHID = ?", (wentworth_id,))

        conn.commit()
        conn.close()

        print(f"User with Wentworth ID: {wentworth_id} removed.")

    def add_student(self):
        print("\n--Add Student--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM STUDENT WHERE WENTWORTHID = ?", (wentworth_id,))
        student = cursor.fetchone()

        if student is not None:
            print("Student already exists.")
            conn.close()
            return

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        password = input(f"Enter Password for {first_name}: ")
        courses = None
        grad_year = input("Enter Graduation Year: ")
        major = input("Enter Major: ")
        email = input("Enter Email: ")

        cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (wentworth_id, first_name, last_name, password, courses, grad_year, major, email))

        conn.commit()
        conn.close()

        print(f"Student with Wentworth ID: {wentworth_id} added.")

    def remove_student(self):
        print("\n--Remove Student--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM STUDENT WHERE WENTWORTHID = ?", (wentworth_id,))
        student = cursor.fetchone()

        if student is None:
            print("Student does not exist.")
            conn.close()
            return

        cursor.execute("DELETE FROM STUDENT WHERE WENTWORTHID = ?", (wentworth_id,))

        conn.commit()
        conn.close()

        print(f"Student with Wentworth ID: {wentworth_id} removed.")

    def add_instructor(self):
        print("\n--Add Instructor--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM INSTRUCTOR WHERE WENTWORTHID = ?", (wentworth_id,))
        instructor = cursor.fetchone()

        if instructor is not None:
            print("Instructor already exists.")
            conn.close()
            return

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        password = input(f"Enter Password for {first_name}: ")
        department = input("Enter Department: ")
        hire_year = input("Enter Hire Year: ")
        title = input("Enter Title: ")
        email = input("Enter Email: ")

        cursor.execute("INSERT INTO INSTRUCTOR VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (wentworth_id, first_name, last_name, password, department, hire_year, title, email))

        conn.commit()
        conn.close()

        print(f"Instructor with Wentworth ID: {wentworth_id} added.")

    def remove_instructor(self):
        print("\n--Remove Instructor--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM INSTRUCTOR WHERE WENTWORTHID = ?", (wentworth_id,))
        instructor = cursor.fetchone()

        if instructor is None:
            print("Instructor does not exist.")
            conn.close()
            return

        cursor.execute("DELETE FROM INSTRUCTOR WHERE WENTWORTHID = ?", (wentworth_id,))

        conn.commit()
        conn.close()

        print(f"Instructor with Wentworth ID: {wentworth_id} removed.")

    def add_admin(self):
        print("\n--Add Admin--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ADMIN WHERE WENTWORTHID = ?", (wentworth_id,))
        admin = cursor.fetchone()

        if admin is not None:
            print("Admin already exists.")
            conn.close()
            return

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        password = input(f"Enter Password for {first_name}: ")
        title = input("Enter Title: ")
        office = input("Enter Office: ")
        email = input("Enter Email: ")

        cursor.execute("INSERT INTO ADMIN VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (wentworth_id, first_name, last_name, password, title, office, email))

        conn.commit()
        conn.close()

        print(f"Admin with Wentworth ID: {wentworth_id} added.")

    def remove_admin(self):
        print("\n--Remove Admin--")
        wentworth_id = input("Enter Wentworth ID: ")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ADMIN WHERE WENTWORTHID = ?", (wentworth_id,))
        admin = cursor.fetchone()

        if admin is None:
            print("Admin does not exist.")
            conn.close()
            return

        cursor.execute("DELETE FROM ADMIN WHERE WENTWORTHID = ?", (wentworth_id,))

        conn.commit()
        conn.close()

        print(f"Admin with Wentworth ID: {wentworth_id} removed.")

    def query_users(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER")
        users = cursor.fetchall()
        for user in users:
            print(user)
        conn.close()

    def query_students(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENT")
        students = cursor.fetchall()
        for student in students:
            print(student)
        conn.close()

    def query_instructors(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM INSTRUCTOR")
        instructors = cursor.fetchall()
        for instructor in instructors:
            print(instructor)
        conn.close()

    def query_admins(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ADMIN")
        admins = cursor.fetchall()
        for admin in admins:
            print(admin)
        conn.close()

    def search_roster(self):
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            print(f"{course[1]} Roster Search:")
            wentworth_id = input("Enter Wentworth ID:")

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Find the student with the given Wentworth ID who is in the course with the given CRN
            cursor.execute("""
                SELECT STUDENT.* 
                FROM STUDENT 
                JOIN STUDENT_COURSE ON STUDENT.WENTWORTHID = STUDENT_COURSE.WENTWORTHID 
                WHERE STUDENT.WENTWORTHID = ? AND STUDENT_COURSE.CRN = ?
            """, (wentworth_id, crn))
            student = cursor.fetchone()
            if student is not None:
                student_obj = Student(student[1], student[2], student[0], student[3], student[4], student[5],
                                      student[6], student[7])
                print(student_obj.show_all_info())
                return

            # Find the instructor with the given Wentworth ID who is in the course with the given CRN
            cursor.execute("""
                SELECT INSTRUCTOR.* 
                FROM INSTRUCTOR 
                JOIN COURSE ON INSTRUCTOR.DEPARTMENT = COURSE.DEPARTMENT 
                WHERE INSTRUCTOR.WENTWORTHID = ? AND COURSE.CRN = ?
            """, (wentworth_id, crn))
            instructor = cursor.fetchone()
            if instructor is not None:
                instructor_obj = Instructor(instructor[1], instructor[2], instructor[0], instructor[3], instructor[4],
                                            instructor[5], instructor[6], instructor[7])
                print(instructor_obj.show_all_info())
                return

            print(f"No user found with Wentworth ID {wentworth_id} in the course with CRN {crn}")

            conn.close()

    def show_roster(self):
        while True:
            course, crn = is_crn_unique()

            if course == 0:
                break

            if course is None:
                print(f"Course with CRN {crn} does not exist.")
                continue

            print(f"Roster for {course[1]}:")

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Query to find all instructors that have the inputted course
            cursor.execute("""
                        SELECT INSTRUCTOR.*, COURSE.*
                        FROM INSTRUCTOR
                        JOIN COURSE ON INSTRUCTOR.DEPARTMENT = COURSE.DEPARTMENT
                        WHERE COURSE.DEPARTMENT = ?
                    """, (course[2],))
            instructors_with_course = cursor.fetchall()
            print("Instructors that can teach this course:")
            for instructor in instructors_with_course:
                print(instructor)

            # Query to find all students that have the inputted course
            cursor.execute("""
                SELECT STUDENT.*, COURSE.*
                FROM STUDENT
                JOIN COURSE ON STUDENT.COURSES = COURSE.CRN
                WHERE COURSE.CRN = ?
            """, (crn,))
            students_with_course = cursor.fetchall()
            print(f"Students taking {course[1]}:")
            for student in students_with_course:
                print(student)

            conn.close()
            break

    def update_admin(self, wentworth_id, new_title):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE ADMIN SET TITLE = ? WHERE WENTWORTHID = ?", (new_title, wentworth_id))
        conn.commit()
        conn.close()
        print(f"Admin with ID {wentworth_id} updated to {new_title}.")

        conn.commit()
        conn.close()

    def add_to_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO ADMIN VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (self.wentworth_id, self.first_name, self.last_name, self.password, self.title,
                        self.office, self.email))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    create_COURSE_table()
    create_USER_table()
    create_STUDENT_table()
    create_STUDENT_COURSE_table()
    create_INSTRUCTOR_table()
    create_ADMIN_table()

    user_type, active_user_object = main_menu()
    sub_menu(user_type, active_user_object)
