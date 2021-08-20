# 1
def countdown(num):
    newls = []
    for i in range(num, -1, -1):
        newls.append(i)
    print(newls)
countdown(5)

# 2
def print_and_return(arr):
    
    print (arr[0])
    return (arr[1])
    
x= print_and_return([1,2])
print (x)

# 3
def first_plus_length(arr):
    return arr[0] + len(arr)


x = first_plus_length([1,2,3,4,5])
print(x)

# 4
def values_greater_than_second(arr):
    newarr = []
    for i in range(0,len(arr)):
        if i > arr[1]:
            newarr.append(arr[i])
    print (len(newarr))
    if len(arr) < 2:
        return False
    else:
        return newarr
print (values_greater_than_second([1,2,3,4,5,6]))

# 5
def length_and_value(size,value):
    arr = []
    for i in range (size):
        arr.append(value)
    
    return arr
print (length_and_value(3,6))