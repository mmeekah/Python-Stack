#1
for x in range(0, 151, 1):
    print(x)

#2
for x in range(5, 1001, 1):
    if (x % 5 == 0):
        print(x)

#3

for x in range(5, 101, 1):
    if (x % 10 == 0):
        print('Coding Dojo')
    elif (x % 5 == 0):
        print('Coding')
    else:
        print(x)


#4

sum = 0
for x in range (0,50, 1):
    if(x % 2 != 0):
        sum = sum + x
        print(sum)

#5

for x in range (2018, 0, -1):
    if(x % 4 == 0):
        print(x)


#6

def multiples(lowNum, highNum, mult):
    for x in range(lowNum, highNum):
        if(x % mult == 0):
            print(x)


# Test Case
multiples(0, 100, 2)
multiples(0, 100, 3)
multiples(0, 100, 4)
