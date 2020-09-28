# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(arr):
    for i in range(0,len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    print(arr)
    return(arr)

biggie_size([-1, 3, 5, -5])


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it

def count_positives(arr):
    count =0
    for i in range(len(arr)):
        if arr[i] > 0:
            count +=1
            
    arr[len(arr)-1]=count
    # arr[].append(arr[arr[len(arr)-1]])
    print(arr)
    return arr

count_positives([-1,1,1,1])


# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.


def countPositives(arr):
    count =0
    i=0

    while i<len(arr):
        if arr[i]>0:
            count +=1
        
        i=i+1
    arr[len(arr)-1] = count

    print(arr)
    return arr

countPositives([1,6,-4,-2,-7,-2])



# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(arr):
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)
    return sum


sum_total([1,2,3,4])    


# Using WHILE loop


def sumTotal(arr):

    total = 0
    i = 0

    while i < len(arr):
        total = total + arr[i]
        i = i + 1

    print(total)
    return total

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(arr):
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum/len(arr))
    return sum/len(arr)


average([1,2,3,4]) 


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(arr):
    print (len(arr))
    return len(arr)
length([37,2,1,-9])



# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(arr):
    if len(arr) > 0:
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] < min:
                min=arr[i]
        print(min)
    else:
        
        return False

minimum([37,2,1,-9])
minimum([]) 



# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(arr):
    if len(arr) > 0:
        max = arr[0]
        for i in range(len(arr)):
            if arr[i] > max:
                max=arr[i]
        print(max)
    else:
        
        return False

maximum([37,2,1,-9])
maximum([]) 


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def UltimateAnalyze(arr):

    total = 0
    minimum = arr[0]
    maximum = arr[0]
    count = 0

    if arr == []:
        return False

    for num in range(len(arr)):
        total = total + arr[num]
        count = count + 1

        if arr[num] < minimum:
            minimum = arr[num]
        elif arr[num] > maximum:
            maximum = arr[num]

    average = total / count
    summary = {"Total": total, "Average": average,
        "Minimum": minimum, "Maximum": maximum, "Length": count}

    print(summary)
    return summary
UltimateAnalyze([1, 2, 3, 4, 5, 6, 7, 8, 9])


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]



def reverseList(arr):

    temp = arr[0]

    for i in range(int(len(arr) / 2)):
        arr[i] = arr[len(arr) - (i + 1)]
        arr[len(arr) - (i + 1)] = temp
        temp = arr[i + 1]

    print(arr)
    return arr

reverseList([1, 2, 3, 4])

