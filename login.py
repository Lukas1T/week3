correct_username = "harry"
correct_passwort = "potter" 

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_passwort :
    print(f"Welcome to Hogwarts, {username} {password}!")

else: 
    print(f"Access denied! Go away, {username}!")
