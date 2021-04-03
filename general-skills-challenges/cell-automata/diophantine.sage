'''
lb = -1
ub = 1
A = matrix(ZZ, [(8,2,10,0,12,2,0), (4,6,9,1,14,5,2), (2,0,1,1,0,1,0), (2,1,3,0,4,0,1)])
eq1 = [(0,8,2,10,0,12,2,0), (0,4,6,9,1,14,5,2), (0,2,0,1,1,0,1,0), (0,2,1,3,0,4,0,1)]
ieq1 = [(-lb,1,0,0,0,0,0,0), (ub,-1,0,0,0,0,0,0),
         (-lb,0,1,0,0,0,0,0), (ub,0,-1,0,0,0,0,0),
         (-lb,0,0,1,0,0,0,0), (ub,0,0,-1,0,0,0,0),
         (-lb,0,0,0,1,0,0,0), (ub,0,0,0,-1,0,0,0),
         (-lb,0,0,0,0,1,0,0), (ub,0,0,0,0,-1,0,0),
         (-lb,0,0,0,0,0,1,0), (ub,0,0,0,0,0,-1,0),
         (-lb,0,0,0,0,0,0,1), (ub,0,0,0,0,0,0,-1)]
p = Polyhedron(eqns=eq1, ieqs=ieq1, base_ring=QQ)
p.integral_points()
'''

import numpy as np

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

#grid = [[3, 5, 5, 3], [5, 8, 8, 5], [5, 8, 8, 5], [3, 5, 5, 3]]
height = len(grid)
width = len(grid[0])
print (height, width)
b = np.array(grid).flatten()
b = np.multiply(np.reshape(b, (-1, 1)), -1)

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
            if i == 0:
              print (index)
            A[i][index] = 1

#print (b)
print (b.shape)
print (A.shape)
eq1 = np.concatenate((b, A), axis=1)
#A = matrix(ZZ, A)
print (eq1)

lb = 0
ub = 2
identity = np.identity(n)
lb_vector = np.multiply(np.ones([n, 1]), -lb)
lb_eqs = np.concatenate((lb_vector, identity), 1)

ub_vector = np.multiply(np.ones([n, 1]), ub)
ub_eqs = np.concatenate((ub_vector, np.multiply(identity, -1)), 1)
ieq1 = np.concatenate((ub_eqs, lb_eqs), 0)
print (ieq1)



p = Polyhedron(eqns=eq1, ieqs=ieq1, base_ring=QQ)
print (p.integral_points())
