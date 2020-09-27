#1

# def countDown(num):
#     arr = []


#     for i in range(0, num + 1):
#         arr.append(num-i)

#     print(arr)

# countDown(5)


#2
def print_and_return(arr):
    print(arr[0])
    return arr[1]

print_and_return([1,2])

#3


def first_plus_length(arr):
    
    print(arr[0]+len(arr))
    return (arr[0] + len(arr))

first_plus_length([1,2,3,4,5])

#4

def values_greater_than_second(arr):
    
    counter=0
    
    for i in range (len(arr)):
        if arr[i]>arr[1]:
            counter +=1
            print(counter)
    if len(arr) < 2:
        return False       

values_greater_than_second([5,2,3,2,1,4])

#5

def lengthAndValue(x,y):
    arr=[]
    for i in range(0,x):
        arr.append(y)
    print(arr)

lengthAndValue(4,7)




