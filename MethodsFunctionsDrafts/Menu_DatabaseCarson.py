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


def add_student(student_id, first_name, last_name, grad_year, major, email):
    conn = sqlite3.connect('assignment3.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?)",
                   (student_id, first_name, last_name, grad_year, major, email))
    conn.commit()
    conn.close()


def remove_instructor(instructor_id):
    conn = sqlite3.connect('assignment3.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = ?", (instructor_id,))
    conn.commit()
    conn.close()
    print(f"Instructor with ID {instructor_id} removed.")


def update_admin():
    admin_id = int(input("Enter Admin ID: "))
    new_title = input("Enter the new title: ")

    conn = sqlite3.connect('assignment3.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE ADMIN SET TITLE = ? WHERE ID = ?", (new_title, admin_id))
    conn.commit()
    conn.close()
    print(f"Admin with ID {admin_id} updated to {new_title}.")


def add_course(crn, title, department, time, days, semester, year, credits):
    db = sqlite3.connect('assignment3.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO COURSE VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (crn, title, department, time, days, semester, year, credits))
    db.commit()
    db.close()
    print(f"Course {title} added.")


def query_courses():
    conn = sqlite3.connect('assignment3.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM COURSE")
    courses = cursor.fetchall()
    for course in courses:
        print(f"Course: {course[1]}")
        cursor.execute("SELECT * FROM INSTRUCTOR WHERE DEPT = ?", (course[2],))
        instructors = cursor.fetchall()
        if instructors:
            print("Instructors who can teach this course:")
            for instructor in instructors:
                print(f"  - {instructor[1]} {instructor[2]}, {instructor[3]}")
        else:
            print("  No instructors available for this course's department.")
    conn.close()


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


def main_menu():
    create_tables()
    while True:
        try:
            print("\nMain Menu:")
            print("1. Add Student")
            print("2. Remove Instructor")
            print("3. Update Admin")
            print("4. Add Course")
            print("5. Query Courses")
            print("6. Query Students")
            print("7. Query Instructors")
            print("8. Query Admins")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Add Student
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                grad_year = int(input("Enter Graduation Year: "))
                major = input("Enter Major: ")
                email = input("Enter Email: ")
                add_student(student_id, first_name, last_name, grad_year, major, email)
            elif choice == '2':
                # Remove Instructor
                instructor_id = int(input("Enter Instructor ID to remove: "))
                remove_instructor(instructor_id)
            elif choice == '3':
                # Update Admin
                update_admin()
            elif choice == '4':
                # Add Course
                crn = int(input("Enter Course CRN: "))
                title = input("Enter Course Title: ")
                department = input("Enter Course Department: ")
                time = input("Enter Course Time: ")
                days = input("Enter Course Days: ")
                semester = input("Enter Course Semester: ")
                year = int(input("Enter Course Year: "))
                credits = int(input("Enter Course Credits: "))
                add_course(crn, title, department, time, days, semester, year, credits)
            elif choice == '5':
                # Query Courses
                query_courses()
            elif choice == '6':
                # Query Students
                query_students()
            elif choice == '7':
                # Query Instructors
                query_instructors()
            elif choice == '8':
                # Query Admins
                query_admins()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            input("Press Enter to continue...")


# Run the main menu
main_menu()
