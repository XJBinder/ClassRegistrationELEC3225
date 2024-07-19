# A little shortcut for making the database file, feel free to add your own data to the add_data() function - Jon
import sqlite3


# Creates tables needed for class registration database
def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create table called "COURSE"
    cursor.execute('''CREATE TABLE IF NOT EXISTS COURSE (
            CRN INTEGER PRIMARY KEY,
            TITLE TEXT NOT NULL,
            DEPARTMENT TEXT NOT NULL,
            TIME TEXT NOT NULL,
            DAYS TEXT NOT NULL,
            SEMESTER TEXT NOT NULL,
            YEAR INTEGER NOT NULL,
            CREDITS INTEGER NOT NULL)''')

    # Create new table called "USER"
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
            WENTWORTHID TEXT PRIMARY KEY,
            FIRSTNAME TEXT NOT NULL,
            LASTNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL)''')

    # Create new table called "STUDENT"
    cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT (
            WENTWORTHID TEXT PRIMARY KEY,
            FIRSTNAME TEXT NOT NULL,
            LASTNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL,
            GRADYEAR INTEGER,
            MAJOR TEXT,
            EMAIL TEXT)''')

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


# Adds test data to the database
def add_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Course data
    courses = [
        ('10000', 'Intro to Walking', 'BSEE', '1530', 'MWF', 'Summer', 2024, 4),
        ('10001', 'How to Breathe', 'BSCE', '1530', 'MWF', 'Summer', 2024, 4),
        ('10002', 'Advanced Procrastination', 'BSCE', '0900', 'MWF', 'Fall', 2024, 3),
        ('10003', 'History of Memes', 'BSEE', '1100', 'TTH', 'Spring', 2025, 3),
        ('10004', 'Philosophy of Pizza', 'BSCE', '1300', 'MWF', 'Summer', 2024, 2),
        ('10005', 'Quantum Physics for Dogs', 'BSEE', '0800', 'TTH', 'Fall', 2024, 4),
        ('10006', 'Basket Weaving Underwater', 'BSCE', '1400', 'MWF', 'Spring', 2025, 3),
        ('10007', 'Introduction to Nap Taking', 'BSEE', '1200', 'TTH', 'Fall', 2024, 3),
        ('10008', 'The Art of Staying Awake', 'BSCE', '1000', 'MWF', 'Spring', 2025, 2),
        ('10009', 'Zombie Survival Tactics', 'BSEE', '1500', 'TTH', 'Summer', 2024, 3),
        ('10010', 'Rocket Science for Dummies', 'BSCE', '1600', 'MWF', 'Fall', 2024, 4),
        ('10011', 'Introduction to Sarcasm', 'BSEE', '0900', 'TTH', 'Spring', 2025, 2),
        ('10012', 'The History of Dinosaurs', 'BSCE', '1100', 'MWF', 'Summer', 2024, 3),
        ('10013', 'Magic Tricks 101', 'BSEE', '1300', 'TTH', 'Fall', 2024, 3),
        ('10014', 'Clown College', 'BSCE', '0800', 'MWF', 'Spring', 2025, 2),
        ('10015', 'The Science of Bubble Wrap', 'BSEE', '1400', 'TTH', 'Summer', 2024, 3),
        ('10016', 'How to Speak Cat', 'BSCE', '1200', 'MWF', 'Fall', 2024, 2),
        ('10017', 'Alien Communication', 'BSEE', '1000', 'TTH', 'Spring', 2025, 3),
        ('10018', 'The Physics of Superheroes', 'BSCE', '1500', 'MWF', 'Summer', 2024, 4),
        ('10019', 'Pirate Studies', 'BSEE', '1600', 'TTH', 'Fall', 2024, 3),
        ('10020', 'Viking Culture and History', 'BSCE', '0800', 'MWF', 'Spring', 2025, 3),
        ('10021', 'Introduction to Wizardry', 'BSEE', '1400', 'TTH', 'Summer', 2024, 4),
    ]

    for course in courses:
        cursor.execute(
            "INSERT INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS) VALUES (?, ?, ?, ?, ?, "
            "?, ?, ?)", course)

    # User data
    users = [
        ('00', 'Angry', 'Mom', 'password'),
        ('01', 'Karen', 'Smith', 'password'),
        ('02', 'Kyle', 'Smith', 'password'),
        ('03', 'Frustrated', 'Dad', 'password'),
    ]

    for user in users:
        cursor.execute("INSERT INTO USER (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD) VALUES (?, ?, ?, ?)", user)

    # Student data
    students = [
        ('W00409648', 'Jon', 'Binder', 'password', 2025, 'BSCE', 'binderj@wit.edu'),
        ('W00000000', 'Carson', 'Mershon', 'password', 3046, 'BSCE', 'cpmershon@wit.edu'),
        ('W00000001', 'Ayush', 'Sharma', 'password', 2025, 'BSCE', 'sharmaa7@wit.edu'),
        ('W00000002', 'Albert', 'Einstein', 'password', 2026, 'BSEE', 'einsteina@wit.edu'),
        ('W00000003', 'Marie', 'Curie', 'password', 2025, 'BSCE', 'curiem@wit.edu'),
        ('W00000004', 'Isaac', 'Newton', 'password', 2024, 'BSEE', 'newtoni@wit.edu'),
        ('W00000005', 'Nikola', 'Tesla', 'password', 2025, 'BSCE', 'teslan@wit.edu'),
        ('W00000006', 'Leonardo', 'da Vinci', 'password', 2026, 'BSEE', 'davincil@wit.edu'),
        ('W00000007', 'Charles', 'Darwin', 'password', 2025, 'BSCE', 'darwinc@wit.edu'),
        ('W00000008', 'Galileo', 'Galilei', 'password', 2024, 'BSEE', 'galileig@wit.edu'),
        ('W00000009', 'Ada', 'Lovelace', 'password', 2026, 'BSCE', 'lovelacea@wit.edu'),
        ('W00000010', 'Thomas', 'Edison', 'password', 2025, 'BSEE', 'edisont@wit.edu'),
        ('W00000011', 'Alan', 'Turing', 'password', 2024, 'BSCE', 'turinga@wit.edu'),
        ('W00000012', 'Stephen', 'Hawking', 'password', 2025, 'BSEE', 'hawkings@wit.edu'),
        ('W00000013', 'Rosalind', 'Franklin', 'password', 2024, 'BSCE', 'franklinr@wit.edu'),
        ('W00000014', 'Neil', 'Armstrong', 'password', 2026, 'BSEE', 'armstrongn@wit.edu'),
        ('W00000015', 'Buzz', 'Aldrin', 'password', 2025, 'BSCE', 'aldrinb@wit.edu'),
        ('W00000016', 'Sally', 'Ride', 'password', 2024, 'BSEE', 'rides@wit.edu'),
        ('W00000017', 'Grace', 'Hopper', 'password', 2026, 'BSCE', 'hopperg@wit.edu'),
        ('W00000018', 'Katherine', 'Johnson', 'password', 2025, 'BSEE', 'johnsonk@wit.edu'),
        ('W00000019', 'Carl', 'Sagan', 'password', 2024, 'BSCE', 'saganc@wit.edu'),
        ('W00000020', 'Richard', 'Feynman', 'password', 2026, 'BSEE', 'feynmanr@wit.edu'),
        ('W00000021', 'Jane', 'Goodall', 'password', 2025, 'BSCE', 'goodallj@wit.edu'),
        ('W00000022', 'Edwin', 'Hubble', 'password', 2024, 'BSEE', 'hubblee@wit.edu'),
        ('W00000023', 'Tim', 'Berners-Lee', 'password', 2026, 'BSCE', 'bernersleet@wit.edu'),
        ('W00000024', 'Elon', 'Musk', 'password', 2025, 'BSEE', 'muske@wit.edu'),
        ('W00000025', 'Steve', 'Jobs', 'password', 2024, 'BSCE', 'jobss@wit.edu'),
        ('W00000026', 'Bill', 'Gates', 'password', 2026, 'BSEE', 'gatesb@wit.edu'),
        ('W00000027', 'Mark', 'Zuckerberg', 'password', 2025, 'BSCE', 'zuckerbergm@wit.edu'),
        ('W00000028', 'Larry', 'Page', 'password', 2024, 'BSEE', 'pagel@wit.edu'),
        ('W00000029', 'Sergey', 'Brin', 'password', 2026, 'BSCE', 'brins@wit.edu'),
        ('W00000030', 'Jeff', 'Bezos', 'password', 2025, 'BSEE', 'bezosj@wit.edu'),
        ('W00000031', 'Jack', 'Dorsey', 'password', 2024, 'BSCE', 'dorseyj@wit.edu'),
        ('W00000032', 'Sundar', 'Pichai', 'password', 2026, 'BSEE', 'pichais@wit.edu'),
        ('W00000033', 'Satya', 'Nadella', 'password', 2025, 'BSCE', 'nadellas@wit.edu'),
        ('W00000034', 'Sheryl', 'Sandberg', 'password', 2024, 'BSEE', 'sandbergs@wit.edu'),
        ('W00000035', 'Marissa', 'Mayer', 'password', 2026, 'BSCE', 'mayerm@wit.edu'),
        ('W00000036', 'Susan', 'Wojcicki', 'password', 2025, 'BSEE', 'wojcickis@wit.edu'),
        ('W00000037', 'Meg', 'Whitman', 'password', 2024, 'BSCE', 'whitmanm@wit.edu'),
        ('W00000038', 'Ginni', 'Rometty', 'password', 2026, 'BSEE', 'romettyg@wit.edu'),
        ('W00000039', 'Indra', 'Nooyi', 'password', 2025, 'BSCE', 'nooyii@wit.edu'),
        ('W00000040', 'Mary', 'Barra', 'password', 2024, 'BSEE', 'barram@wit.edu'),
        ('W00000041', 'Ursula', 'Burns', 'password', 2026, 'BSCE', 'burnsu@wit.edu'),
        ('W00000042', 'Angela', 'Merkel', 'password', 2025, 'BSEE', 'merkela@wit.edu'),
        ('W00000043', 'Margaret', 'Thatcher', 'password', 2024, 'BSCE', 'thatcherm@wit.edu'),
        ('W00000044', 'Donald', 'Trump', 'password', 2026, 'BSEE', 'trumpd@wit.edu'),
        ('W00000045', 'Melania', 'Trump', 'password', 2025, 'BSCE', 'trumpm@wit.edu'),
        ('W00000046', 'Barron', 'Trump', 'password', 2024, 'BSEE', 'trumpb@wit.edu'),
        ('W00000047', 'George', 'Washington', 'password', 2026, 'BSCE', 'washingtong@wit.edu'),
        ('W00000048', 'Thomas', 'Jefferson', 'password', 2025, 'BSEE', 'jeffersont@wit.edu'),
        ('W00000049', 'Abraham', 'Lincoln', 'password', 2024, 'BSCE', 'lincolna@wit.edu'),
        ('W00000050', 'Theodore', 'Roosevelt', 'password', 2026, 'BSEE', 'rooseveltt@wit.edu'),
        ('W00000051', 'Franklin', 'Roosevelt', 'password', 2025, 'BSCE', 'rooseveltf@wit.edu'),
        ('W00000052', 'John', 'Kennedy', 'password', 2024, 'BSEE', 'kennedyj@wit.edu'),
        ('W00000053', 'Ronald', 'Reagan', 'password', 2026, 'BSCE', 'reaganr@wit.edu'),
        ('W00000054', 'Winston', 'Churchill', 'password', 2025, 'BSEE', 'churchillw@wit.edu'),
        ('W00000055', 'Nelson', 'Mandela', 'password', 2024, 'BSCE', 'mandelan@wit.edu'),
        ('W00000056', 'Mahatma', 'Gandhi', 'password', 2026, 'BSEE', 'gandhim@wit.edu'),
        ('W00000057', 'Martin', 'Luther King', 'password', 2025, 'BSCE', 'kingm@wit.edu'),
        ('W00000058', 'Mother', 'Teresa', 'password', 2024, 'BSEE', 'teresam@wit.edu'),
        ('W00000059', 'Nelson', 'Mandela', 'password', 2026, 'BSCE', 'mandelan@wit.edu'),
        ('W00000060', 'Ivanka', 'Trump', 'password', 2025, 'BSEE', 'trumpi@wit.edu'),
        ('W00000061', 'Amelia', 'Earhart', 'password', 2024, 'BSCE', 'earharta@wit.edu'),
        ('W00000062', 'Helen', 'Keller', 'password', 2026, 'BSEE', 'kellerh@wit.edu'),
        ('W00000063', 'Cleopatra', 'VII', 'password', 2025, 'BSCE', 'cleopatravii@wit.edu'),
        ('W00000064', 'Joan', 'of Arc', 'password', 2024, 'BSEE', 'joanofarck@wit.edu'),
        ('W00000065', 'Marie', 'Antoinette', 'password', 2026, 'BSCE', 'antoinettem@wit.edu'),
        ('W00000066', 'Catherine', 'the Great', 'password', 2025, 'BSEE', 'catherinetg@wit.edu'),
        ('W00000067', 'Queen', 'Elizabeth I', 'password', 2024, 'BSCE', 'elizabethq@wit.edu'),
        ('W00000068', 'Queen', 'Victoria', 'password', 2026, 'BSEE', 'victoriaq@wit.edu'),
        ('W00000069', 'William', 'Shakespeare', 'password', 2025, 'BSCE', 'shakespearew@wit.edu'),
        ('W00000070', 'Homer', 'Simpson', 'password', 2024, 'BSEE', 'simpsonh@wit.edu'),
        ('W00000071', 'Bruce', 'Wayne', 'password', 2026, 'BSCE', 'wayneb@wit.edu'),
        ('W00000072', 'Clark', 'Kent', 'password', 2025, 'BSEE', 'kentc@wit.edu'),
        ('W00000073', 'Peter', 'Parker', 'password', 2024, 'BSCE', 'parkerp@wit.edu'),
        ('W00000074', 'Tony', 'Stark', 'password', 2026, 'BSEE', 'starkt@wit.edu'),
        ('W00000075', 'Diana', 'Prince', 'password', 2025, 'BSCE', 'princed@wit.edu'),
        ('W00000076', 'Barry', 'Allen', 'password', 2024, 'BSEE', 'allenb@wit.edu'),
        ('W00000077', 'Hal', 'Jordan', 'password', 2026, 'BSCE', 'jordanh@wit.edu'),
        ('W00000078', 'Arthur', 'Curry', 'password', 2025, 'BSEE', 'currya@wit.edu'),
        ('W00000079', 'Victor', 'Stone', 'password', 2024, 'BSCE', 'stonev@wit.edu'),
        ('W00000080', 'Bruce', 'Banner', 'password', 2026, 'BSEE', 'bannerb@wit.edu'),
        ('W00000081', 'Steve', 'Rogers', 'password', 2025, 'BSCE', 'rogerss@wit.edu'),
        ('W00000082', 'Natasha', 'Romanoff', 'password', 2024, 'BSEE', 'romanoffn@wit.edu'),
        ('W00000083', 'Clint', 'Barton', 'password', 2026, 'BSCE', 'bartonc@wit.edu'),
        ('W00000084', 'Challa', 'Panther', 'password', 2025, 'BSEE', 'panthert@wit.edu'),
        ('W00000085', 'Wanda', 'Maximoff', 'password', 2024, 'BSCE', 'maximoffw@wit.edu'),
        ('W00000086', 'Vision', 'Vision', 'password', 2026, 'BSEE', 'visionv@wit.edu'),
        ('W00000087', 'Scott', 'Lang', 'password', 2025, 'BSCE', 'langs@wit.edu'),
        ('W00000088', 'Stephen', 'Strange', 'password', 2024, 'BSEE', 'stranges@wit.edu'),
        ('W00000089', 'Nick', 'Fury', 'password', 2026, 'BSCE', 'fury@wit.edu'),
        ('W00000090', 'Peggy', 'Carter', 'password', 2025, 'BSEE', 'carterp@wit.edu'),
        ('W00000091', 'Bucky', 'Barnes', 'password', 2024, 'BSCE', 'barnesb@wit.edu'),
        ('W00000092', 'Sam', 'Wilson', 'password', 2026, 'BSEE', 'wilsons@wit.edu'),
        ('W00000093', 'James', 'Rhodes', 'password', 2025, 'BSCE', 'rhodesj@wit.edu'),
        ('W00000094', 'Carol', 'Danvers', 'password', 2024, 'BSEE', 'danversc@wit.edu'),
        ('W00000095', 'Shuri', 'Wakanda', 'password', 2026, 'BSCE', 'wakandas@wit.edu'),
        ('W00000096', 'Peter', 'Quill', 'password', 2025, 'BSEE', 'quillp@wit.edu'),
        ('W00000097', 'Gamora', 'Zen', 'password', 2024, 'BSCE', 'zen@wit.edu'),
        ('W00000098', 'Drax', 'Destroyer', 'password', 2026, 'BSEE', 'destroyerd@wit.edu'),
        ('W00000099', 'Rocket', 'Raccoon', 'password', 2025, 'BSCE', 'raccoonr@wit.edu'),
        ('W00000100', 'Groot', 'Tree', 'password', 2024, 'BSEE', 'treeg@wit.edu'),
    ]

    for student in students:
        cursor.execute(
            "INSERT INTO STUDENT (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, GRADYEAR, MAJOR, EMAIL) VALUES (?, ?, "
            "?, ?, ?, ?, ?)", student)

    # Instructor data
    instructors = [
        ('W00000101', 'Douglas', 'Dow', 'password', 'BSCE', 2005, 'Professor', 'dowd@wit.edu'),
        ('W00000102', 'Junsangsri', 'Pilin', 'password', 'BSEE', 2010, 'Professor', 'junsangsrip@wit.edu'),
        ('W00000103', 'Yugu', 'Yang-Keathley', 'password', 'BSEE', 2008, 'Professor', 'yangkeathleyy@wit.edu'),
    ]

    for instructor in instructors:
        cursor.execute(
            "INSERT INTO INSTRUCTOR (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, DEPARTMENT, HIREYEAR, TITLE, EMAIL)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?)", instructor)

    # Admin data
    cursor.execute("INSERT INTO ADMIN (WENTWORTHID, FIRSTNAME, LASTNAME, PASSWORD, TITLE, OFFICE, EMAIL) VALUES "
                   "('admin', 'adminFirst', 'adminLast', 'admin', 'adminMan', 'adminDesk', 'admin@wit.edu')")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_tables()
    add_data()
