import time

t0 = time.time()

number = 100000000
for i in range(number):
    z = i*10

t1 = time.time()

print(t1-t0)
