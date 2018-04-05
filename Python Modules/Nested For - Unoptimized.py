import time

t0 = time.time()

height = 100
width = 100
for i in range(height):
    print("Hello")
    for j in range(width):
        print("Foo")	


t1 = time.time()

print(t1-t0)
