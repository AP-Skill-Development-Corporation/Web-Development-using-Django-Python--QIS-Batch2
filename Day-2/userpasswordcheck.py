username = input("Enter new username")
password = input("Enter password ")

if username.isalnum():
    print("valid username")
else:
    print("Select another user name")

if password.isalnum() and password.isdigit():
    print("valid password")
else:
    print("invalid password")
