friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    f = friends+ [friend_name]  # don't do like this -->  friends = friends+ [friend_name]


add_friend()
print(friends)