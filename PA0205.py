# 1. Ask the user to enter a username
username = input("Enter username: ")

# 2. Ask the user to enter a password
password = input("Enter password: ")

# 3. Compare the entered information with the correct details
if username == "admin" and password == "Python123":
    print("Login successful.")
else:
    print("Login unsuccessful. Incorrect username or password.")
