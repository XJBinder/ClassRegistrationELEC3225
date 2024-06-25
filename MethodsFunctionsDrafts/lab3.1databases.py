import sqlite3

# database file connection 
database = sqlite3.connect("assignment3.db")
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
# SQL command to insert the data in the table, must be done one at a time 
# Add two students
sql_command = """INSERT INTO STUDENT VALUES(10015, 'Ayush', 'Sharma', 2025, 'BSCO', 'sharmaa');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10016, 'James', 'Bond', 2026, 'BSEE', 'bondj');"""
cursor.execute(sql_command) 

sql_command = """DELETE FROM INSTRUCTOR WHERE ID = 20006;"""
cursor.execute(sql_command)

sql_command = """UPDATE ADMIN SET TITLE = 'Vice-President' WHERE NAME = 'Vera';"""
cursor.execute(sql_command)

# SQL command to create a table in the database 
sql_command = ("""
CREATE TABLE COURSES (
    CRN INTEGER PRIMARY KEY NOT NULL,
    TITLE TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    TIME TEXT NOT NULL,
    DAYS TEXT NOT NULL,
    SEMESTER TEXT NOT NULL,
    YEAR INTEGER NOT NULL,
    CREDITS INTEGER NOT NULL
);
""")
cursor.execute(sql_command)

# Populate the COURSE table with 5 courses
sql_command = ("INSERT INTO COURSES (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (30002, 'Art and Technology', 'HUSS', '12:00-13:30', 'TR', 'Fall', 2024, 3);")
cursor.execute(sql_command)

sql_command = ("INSERT INTO COURSES (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (30003, 'Physics II', 'BSAS', '14:00-15:30', 'MW', 'Fall', 2024, 3);")
cursor.execute(sql_command)

sql_command = ("INSERT INTO COURSES (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (30004, 'Applied Programming Concepts', 'BSCO', '09:00-10:30', 'TR', 'Fall', 2024, 3);")
cursor.execute(sql_command)

sql_command = ("INSERT INTO COURSES (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (30005, 'Operating Systems', 'BCOS', '15:00-16:30', 'MW', 'Fall', 2024, 4);")
cursor.execute(sql_command)

sql_command = ("INSERT INTO COURSES (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (30001, 'Network Theory II', 'BCEE', '17:00-18:30', 'MW', 'Fall', 2024, 4);")
cursor.execute(sql_command)


# # Query the database to match instructors with courses
cursor.execute("SELECT TITLE, DEPARTMENT FROM COURSES;")
COURSES = cursor.fetchall()

for COURSE in COURSES:
    TITLE, DEPT = COURSE
    cursor.execute("SELECT NAME, SURNAME FROM INSTRUCTOR WHERE DEPT = ?;", (DEPT,))
    INSTRUCTOR = cursor.fetchall()
    if INSTRUCTOR:
        print(f"INSTRUCTOR for {TITLE} ({DEPT}):")
        for INSTRUCTOR in INSTRUCTOR:
            print(f" - {INSTRUCTOR[0]} {INSTRUCTOR[1]}")
    else:
        print(f"No INSTRUCTOR available for {TITLE} ({DEPT})")

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 

database.commit() 
  
# close the connection 
database.close() 
