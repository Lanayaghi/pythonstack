 
import random
def randInt(min=0   , max=100   ):
    num = 0 
    if min <= max and max > 0:
        num = round(random.random() * (max-min) +min)
    return num

print(randInt()) 		    
print(randInt(max=50)) 	    
print(randInt(min=50)) 	   
print(randInt(min=50, max=500))

print(randInt(min=90, max=60))