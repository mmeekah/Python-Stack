numbers = [1, 2, 3, 4, 5, 6, 7, 8]


evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)



user_input = input("Enter your choice: ").lower()
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")    
