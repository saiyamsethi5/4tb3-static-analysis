import time


height = 10000
width = 10000

t0 = time.time()

for i in range(height*width):
   z = i
        
t1 = time.time()

print(t1-t0)
