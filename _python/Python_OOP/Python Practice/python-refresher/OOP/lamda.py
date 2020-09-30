print((lambda x, y: x+y)(5,7))


def double(x):
    return x * 2

sequence = [1, 2, 3 , 4]
# doubled = [double(x) for x in sequence]
doubled =  map(double, sequence)   # iterates over sequence list and applies double function on each item

print(doubled)