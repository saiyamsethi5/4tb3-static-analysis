
import time

t0 = time.time()

input = 10000000
count = 0

while(count < input):
    result = 'null'



    #print ("Result: " + result)

    x = 4
    if x < 3:
        result = 'Case A'
    else:
        result = 'Case B'
        
    #print ("Result: " + result)


    count = count + 1
    
t1 = time.time()

print(t1-t0)

