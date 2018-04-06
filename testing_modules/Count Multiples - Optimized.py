import time

t0 = time.time()

number = 1000000000
for i in range(0,number,10):
    z = i

t1 = time.time()

print(t1-t0)
