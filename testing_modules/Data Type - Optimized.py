
import time

t0 = time.time()

input = 10000000
count = 0
while(count < input):
    result = 0
    a = 1
    b = 2


    result = result + a + b

    count = count + 1
    
t1 = time.time()

print(t1-t0)
