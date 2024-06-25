# Define the base class User
class User:
    # Constructor to initialize attributes
    def __init__(self, first_name, last_name, ID):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID

    # Setter functions for attributes
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_ID(self, ID):
        self.ID = ID

    # Function to print all info for the object
    def print_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("ID:", self.ID)


# Define the derived class Student
class Student(User):
    # Constructor to initialize attributes
    def __init__(self, first_name, last_name, ID):
        # Call the constructor of the base class (User)
        super().__init__(first_name, last_name, ID)

    # Functions specific to students
    def search_courses(self):
        print("Searching courses...")

    def add_course(self):
        print("Adding course...")

    def drop_course(self):
        print("Dropping course...")

    def print_schedule(self):
        print("Printing schedule...")


# Define the derived class Instructor
class Instructor(User):
    # Constructor to initialize attributes
    def __init__(self, first_name, last_name, ID):
        # Call the constructor of the base class (User)
        super().__init__(first_name, last_name, ID)

    # Functions specific to instructors
    def print_schedule(self):
        print("Printing schedule...")

    def print_class_list(self):
        print("Printing class list...")

    def search_courses(self):
        print("Searching courses...")


# Define the derived class Admin
class Admin(User):
    # Constructor to initialize attributes
    def __init__(self, first_name, last_name, ID):
        # Call the constructor of the base class (User)
        super().__init__(first_name, last_name, ID)

    # Functions specific to admins
    def add_course(self):
        print("Adding course...")

    def remove_course(self):
        print("Removing course...")

    def add_user(self):
        print("Adding user...")

    def remove_user(self):
        print("Removing user...")

    def add_student_to_course(self):
        print("Adding student to course...")

    def remove_student_from_course(self):
        print("Removing student from course...")

    def search_rosters(self):
        print("Searching rosters...")

    def search_courses(self):
        print("Searching courses...")


# Main program
if __name__ == "__main__":
    # Create objects of each class
    user_obj = User("John", "Doe", "12345")
    student_obj = Student("Alice", "Smith", "67890")
    instructor_obj = Instructor("Bob", "Johnson", "54321")
    admin_obj = Admin("Emily", "Davis", "98765")

    # Demonstrate functionality by calling methods and printing messages
    print("User Info:")
    user_obj.print_info()


    print("\nStudent Functions:")
    student_obj.search_courses()
    student_obj.add_course()
    student_obj.drop_course()
    student_obj.print_schedule()
    print("\Student Functions Successful")

    print("\nInstructor Functions:")
    instructor_obj.print_schedule()
    instructor_obj.print_class_list()
    instructor_obj.search_courses()
    print("\nInstructor Functions Successful")


    print("\nAdmin Functions:")
    admin_obj.add_course()
    admin_obj.remove_course()
    admin_obj.add_user()
    admin_obj.remove_user()
    admin_obj.add_student_to_course()
    admin_obj.remove_student_from_course()
    admin_obj.search_rosters()
    admin_obj.search_courses()
    print("\nAdmin Functions Successful")

