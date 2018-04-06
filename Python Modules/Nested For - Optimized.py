import time

t0 = time.time()


height = 100
width = 100
for i in range(height*width):
    if (i%width==0):
        print("Hello")
    print("Foo")
        
t1 = time.time()

print(t1-t0)
