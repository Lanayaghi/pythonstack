# 1
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr
print (biggie_size([1,2,3,-2,-5]))

# 2
def count_positives(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
            arr[len(arr)-1] = count
            arr[-1] = count
    return arr
arr = [-1,2,1,3]
print(count_positives(arr))
print("-"*30)

# 3
def total(list):
    count = 0 
    for element in list:
        count += element
    return count
print(total([1,2,7]))

# 4
def average(lists):
    average = 0 
    for i in lists:
        average = sum(lists) / len(lists)
    return average
print (average([1,2,3]))

# 5

def length(lists):
    return len(lists)
print(length([1,2,3,4]))

# 6

def mini(lists):
    if len(lists) ==0:
            return False
    else:
        min = lists[0]
        for i in lists:
            if lists[i] < min:
                min = lists[i]
        
        return min
print(mini([]))

# 7

def maxi(lists):
    if len(lists) ==0:
            return False
    else:
        max = lists[0]
        for i in lists:
            if lists[i] > min:
                max = lists[i]
        
        return max
print(mini([]))

# 8
def analysis(lists):
    dict = {
        "sum total": sum(lists),
        "average": sum(lists) / len(lists),
        "minimum": min(lists),
        "maximum": max(lists),
        "length" : len(lists)
    }
    return dict

print(analysis([1,2,3,10,-1]))

# 9

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


print(Reverse([10, 11, 12, 13, 14, 15]))