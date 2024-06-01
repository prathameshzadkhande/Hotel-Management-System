from admin import Admin
from user import User
class Interface:

    admin_id = "admin"
    admin_pass = "1234"

    def __init__(self):
        self.display()

    def display(self):
        print("""
            ___________________________________________
            |   Welcome To Hotel Management System    |
            |-----------------------------------------|
            |  1.  For Admin Interface                |
            |  2.  For User Interface                 |
            |  3.  Exit                               |
            -------------------------------------------
        """)
        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            self.authenticate_admin()  
        elif choice == 2:
            self.user_interface()  # Call method to proceed to user interface
        else:
            print("You have exited from the Hotel Management System")

    def authenticate_admin(self):
        username = input("Enter Admin ID: ")
        password = input("Enter Password: ")

        if username == self.admin_id and password == self.admin_pass:
            print("Authentication successful.")
            admin = Admin()
            # Call methods or initiate the admin interface based on your Admin class implementation
        else:
            print("Invalid credentials. Access denied.")

    def user_interface(self):
        user = User()


if __name__ == "__main__":
    a = Interface()
