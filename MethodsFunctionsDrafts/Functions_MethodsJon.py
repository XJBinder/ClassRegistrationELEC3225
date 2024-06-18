# Tech with Tim's YouTube
# https://www.youtube.com/watch?v=VchuKL44s6E
# Corey Schafer's YouTube
# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

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

    def add_course(self):
        print('\nAdmin Add Course Method')

    def remove_course(self):
        print('\nAdmin Remove Course Method')

    def add_user(self):
        print('\nAdmin Add User Method')

    def remove_user(self):
        print('\nAdmin Remove User Method')

    def add_student(self):
        print('\nAdmin Add Student Method') # To Course

    def remove_student(self):
        print('\nAdmin Remove Student Method') # From Course

    def search_roster(self):
        print('\nAdmin Search Roster Method')

    def show_roster(self):
        print('\nAdmin Print Roster Method')

    def search_course(self):
        print('\nAdmin Search Course Method')

    def show_course(self):
        print('\nAdmin Print Course Method')


# Creating Objects
user_object = User('Jon', 'Binder', 'W00409648')
student_object = Student('Carson', 'Mershon', 'W00414141')
instructor_object = Instructor('Douglas', 'Dr. Dow')
admin_object = Admin('Admin', 'Person')

# Welcome Message
print('\n\t  --Welcome to Leopard Web Class Registration--')
print('This is a test to show methods and classes work in Python')
print('\n\t--Test Objects--\n1) User\n2) Student\n3) Instructor\n4) Admin\n5) Exit')
# Get User Input
user_input = input('>> ')

while user_input != '5':
    # User Selected User
    if user_input == '1':
        print('\nUser:', user_object.show_all_info(), 'was selected.\n')
        # Menu Items
        print('1) Change First Name\n2) Change Last Name\n3) Change Wentworth ID')
        user_input = input('>> ')
        # Changing Users First Name
        if user_input == '1':
            new_attribute = input('\nChanging First Name\n>> ')
            user_object.set_first_name(new_attribute)
        # Changing Users Last Name
        elif user_input == '2':
            new_attribute = input('\nChanging Last Name\n>> ')
            user_object.set_last_name(new_attribute)
        # Changing Users Wentworth ID
        elif user_input == '3':
            new_attribute = input('\nChanging Wentworth ID\n>> ')
            user_object.set_wentworthID(new_attribute)
        else:
            print('Invalid Input')
    # User Selected Student
    elif user_input == '2':
        print('\nStudent:', student_object.show_all_info(), 'was selected.\n')
        # Menu Items
        print('1) Change First Name\n2) Change Last Name\n3) Change Wentworth ID')
        print('4) Search Course\n5) Add/Drop Course\n6) Print Schedule')
        user_input = input('>> ')
        # Changing Students First Name
        if user_input == '1':
            new_attribute = input('\nChanging First Name\n>> ')
            student_object.set_first_name(new_attribute)
        # Changing Students Last Name
        elif user_input == '2':
            new_attribute = input('\nChanging Last Name\n>> ')
            student_object.set_last_name(new_attribute)
        # Changing Students Wentworth ID
        elif user_input == '3':
            new_attribute = input('\nChanging Wentworth ID\n>> ')
            student_object.set_wentworthID(new_attribute)
        # Search for Course
        elif user_input == '4':
            student_object.search_course()
        # Add/Drop Course
        elif user_input == '5':
            student_object.add_drop_course()
        # Print Schedule
        elif user_input == '6':
            student_object.show_schedule()
        else:
            print('Invalid Input')
    # User Selected Instructor
    elif user_input == '3':
        print('\nInstructor:', instructor_object.show_all_info(), 'was selected.\n')
        # Menu Items
        print('1) Change First Name\n2) Change Last Name\n3) Search Course')
        print('4) Print Class List\n5) Print Schedule')
        user_input = input('>> ')
        # Changing Instructors First Name
        if user_input == '1':
            new_attribute = input('\nChanging First Name\n>> ')
            instructor_object.set_first_name(new_attribute)
        # Changing Instructors Last Name
        elif user_input == '2':
            new_attribute = input('\nChanging Last Name\n>> ')
            instructor_object.set_last_name(new_attribute)
        # Search for Course
        elif user_input == '3':
            instructor_object.search_course()
        # Print Class List
        elif user_input == '4':
            instructor_object.show_class_list()
        # Print Schedule
        elif user_input == '5':
            instructor_object.show_schedule()
        else:
            print('Invalid Input')
    # User Selected Admin
    elif user_input == '4':
        print('\nAdmin:', admin_object.show_all_info(), 'was selected.\n')
        # Menu Items
        print('1) Change First Name\n2) Change Last Name\n3) Add Course')
        print('4) Remove Course\n5) Add User\n6) Remove User\n7) Add Student to Course')
        print('8) Remove Student from Course\n9) Search Roster\n10) Print Roster')
        print('11) Search Course\n12) Print Course')
        user_input = input('>> ')
        # Changing Admins First Name
        if user_input == '1':
            new_attribute = input('\nChanging First Name\n>> ')
            admin_object.set_first_name(new_attribute)
        # Changing Admins Last Name
        elif user_input == '2':
            new_attribute = input('\nChanging Last Name\n>> ')
            admin_object.set_last_name(new_attribute)
        # Add Course
        elif user_input == '3':
            admin_object.add_course()
        # Remove Course
        elif user_input == '4':
            admin_object.remove_course()
        # Add User
        elif user_input == '5':
            admin_object.add_user()
        # Remove User
        elif user_input == '6':
            admin_object.remove_user()
        # Add Student to Course
        elif user_input == '7':
            admin_object.add_student()
        # Remove Student from Course
        elif user_input == '8':
            admin_object.remove_student()
        # Search Roster
        elif user_input == '9':
            admin_object.search_roster()
        # Print Roster
        elif user_input == '10':
            admin_object.show_roster()
        # Search Course
        elif user_input == '11':
            admin_object.search_course()
        # Print Course
        elif user_input == '12':
            admin_object.show_course()
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')

    # Menu Options
    print('\n\t--Test Objects--\n1) User\n2) Student\n3) Instructor\n4) Admin\n5) Exit')
    # Get User Input
    user_input = input('>> ')
