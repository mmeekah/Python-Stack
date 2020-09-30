users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Ann", "longpassword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}  #user[0] or user[1] depending on which info you want5 to sort


username_input = input("Enter your username: ")
password_input = input("Enter your password: ")


_,username, password = username_mapping[username_input]


if password_input == password:
    print("Welcome!")


