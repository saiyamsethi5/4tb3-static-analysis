import time

t0 = time.time()

input = 1000000
count = 0
while(count < input):

    length = 10

    matrix = [0 for x in range(length)]

    for i in range(length):
        matrix[i] = 4


    count = count + 1
t1 = time.time()

print(matrix)

print(t1-t0)
