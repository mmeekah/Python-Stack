# 1.an element in a list:

# create a new list, with a lambda as an elementcopy
my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print(my_list[2]) # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
my_list[2](5)

#<function <lambda> at 0x10fa6cd70>

# 2.passed to another function as a callback:

# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

#4,7

#3stored in a variable:

add10 = lambda x: x + 10 # store lambda expression in a variable
add10(2)  # returns 12
add10(98) # returns 108


#4returned by another function:

def incrementor(num):
    start = num
    return lambda x: num + x


#5
# create a list
my_arr = [1,2,3,4,5]
# define a function that squares values
def square(num):
    return num ** 2
# invoke map function
print(list(map(square, my_arr)))

# output:
# [1, 4, 9, 16, 25]


my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a lambda as the first argument
