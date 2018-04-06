import sys

X = 80
Y = 25
betterY = 25
matrix = [[0 for x in range(X)] for y in range(betterY)]


for x in range(X):
    for y in range(Y):
        sys.stdout.write(str(matrix[y][x]) + " ")
    sys.stdout.write("\n")

