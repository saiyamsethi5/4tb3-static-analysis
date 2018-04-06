import time

t0 = time.time()

input = 1000000
counta = 0
while(counta < input):

    length = 10

    matrix = [0 for x in range(length)]

    count = 0
    while True:
      matrix[count] = 4
      if count == length -1:
        break 
      count = count + 1

    counta = counta + 1
t1 = time.time()

print(t1-t0)
