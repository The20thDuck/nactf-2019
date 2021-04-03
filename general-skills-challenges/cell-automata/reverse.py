f = open("outpattern.txt", "r")
grid = f.readlines() # Array of text lines
# Make grid into array of arrays of numbers
for i in range(len(grid)):
    grid[i] = grid[i][1:-1].split(" ")
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            grid[i][j] = 0
        else:
            grid[i][j] = int(grid[i][j], 16)
print (grid)

import numpy as np
#A = np.random.rand(700, 700)
#b = np.random.rand(700)
#x = np.linalg.solve(A, b)

height = len(grid)
width = len(grid[0])
sum = 0
for i in range(height):
    assert len(grid[i]) == width
    sum += len(grid[i])
print (sum)
print (height, width)

n = width * height
A = np.zeros([n, n])
for i in range(n):
    x = i % width
    y = i // width
    for xOffset in [-1, 0, 1]:
        for yOffset in [-1 , 0, 1]:
            if xOffset == 0 and yOffset == 0:
                continue
            newX = (x + xOffset) % width
            #if x + xOffset != newX:
                #continue
            newY = (y + yOffset) % height
            #if y + yOffset != newY:
                #continue
            index = newY * width + newX
            if i == 2499:
              print (np.array(grid).flatten()[index])
            A[i][index] = 1

print (A)
#print (np.linalg.det(A))
b = np.array(grid).flatten()
print (b)
#x = np.dot(np.linalg.pinv(A), b)
print (A.shape, b.shape)
x = np.linalg.lstsq(A, b)[0]
print (x)
print ("Ax: ", np.dot(A, x))
x = np.round(x).astype(int)
print (x)
img = np.reshape(x, (height, width))


flag = open("inpattern.txt", "w")
for box in img:
    flag.write("%s\n" % " ".join(str(x) for x in box))