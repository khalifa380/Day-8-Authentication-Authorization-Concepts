# auth_concepts.py
users = {"khalifa": "pass123", "admin": "admin123"}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Authentication Successful!")
        if username == "admin":
            print("Authorization: You have admin privileges.")
        else:
            print("Authorization: You have user privileges.")
    else:
        print("Authentication Failed.")

login()
