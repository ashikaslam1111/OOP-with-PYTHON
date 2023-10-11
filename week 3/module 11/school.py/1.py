class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class LoginSystem:
    def __init__(self):
        self.users = []

    def register(self, email, password):
        user = User(email, password)
        self.users.append(user)
        print(f"User with email {email} registered successfully!")

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                print(f"User with email {email} logged in successfully!")
                return
        print("Login failed. Invalid email or password.")


# Usage example
login_system = LoginSystem()

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        login_system.register(email, password)
    elif choice == '2':
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        login_system.login(email, password)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
