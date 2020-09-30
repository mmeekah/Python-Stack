from operator import itemgetter

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0.")


#     return dividend/divisor



# def calculate(*values, operator):
#     return operator(*values)



# result = calculate(20,4, operator = divide)

# print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem)==expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")




friends =[
    {"name": "Rolf Smith", "age":20},
    {"name": "Bob David", "age":30},
    {"name": "Mikah JOhns", "age":26},
]

def get_friend_name(friend):  #finder function
    return friend["name"]



print(search(friends, "Rolf Smith", itemgetter("name")))