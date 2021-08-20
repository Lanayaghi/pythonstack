#  1 leap year
 if year % 4 == 0 and year % 100 !=0:
        return True
    elif year % 4 == 0 and year % 100 ==0 and year % 400 == 0:
        return true 
    else:
        return False
#  2 square
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        
        print(i*i)  
        
# 3 elif
  n = int(input().strip())
    if n % 2 == 0 and (n in range (2,6) or n > 20):
        print('Not Weird')
    else:
        
        print ('Weird')

# 4
    