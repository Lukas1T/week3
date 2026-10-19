correct_username = "harry"
correct_passwort = "potter" 

username = input("Enter your username: ")
password = input("Enter your password: ")

if username != correct_username and password != correct_passwort :
    print(f"Access denied! Go way, {username}!")

else: 
    print(f"Welcome to Hogwarts, {username} {password}!")