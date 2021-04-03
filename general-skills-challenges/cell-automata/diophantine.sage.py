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

# This file was *autogenerated* from the file diophantine.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_16 = Integer(16)
import numpy as np

f = open("outpattern.txt", "r")
grid = f.readlines() # Array of text lines
# Make grid into array of arrays of numbers
for i in range(len(grid)):
    grid[i] = grid[i][_sage_const_1 :-_sage_const_1 ].split(" ")
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            grid[i][j] = _sage_const_0 
        else:
            grid[i][j] = int(grid[i][j], _sage_const_16 )

#grid = [[3, 5, 5, 3], [5, 8, 8, 5], [5, 8, 8, 5], [3, 5, 5, 3]]
height = len(grid)
width = len(grid[_sage_const_0 ])
print (height, width)
b = np.array(grid).flatten()
b = np.multiply(np.reshape(b, (-_sage_const_1 , _sage_const_1 )), -_sage_const_1 )

n = width * height
A = np.zeros([n, n])
for i in range(n):
    x = i % width
    y = i // width
    for xOffset in [-_sage_const_1 , _sage_const_0 , _sage_const_1 ]:
        for yOffset in [-_sage_const_1  , _sage_const_0 , _sage_const_1 ]:
            if xOffset == _sage_const_0  and yOffset == _sage_const_0 :
                continue
            newX = (x + xOffset) % width
            #if x + xOffset != newX:
                #continue
            newY = (y + yOffset) % height
            #if y + yOffset != newY:
                #continue
            index = newY * width + newX
            if i == _sage_const_0 :
              print (index)
            A[i][index] = _sage_const_1 

#print (b)
print (b.shape)
print (A.shape)
eq1 = np.concatenate((b, A), axis=_sage_const_1 )
#A = matrix(ZZ, A)
print (eq1)

lb = _sage_const_0 
ub = _sage_const_2 
identity = np.identity(n)
lb_vector = np.multiply(np.ones([n, _sage_const_1 ]), -lb)
lb_eqs = np.concatenate((lb_vector, identity), _sage_const_1 )

ub_vector = np.multiply(np.ones([n, _sage_const_1 ]), ub)
ub_eqs = np.concatenate((ub_vector, np.multiply(identity, -_sage_const_1 )), _sage_const_1 )
ieq1 = np.concatenate((ub_eqs, lb_eqs), _sage_const_0 )
print (ieq1)



p = Polyhedron(eqns=eq1, ieqs=ieq1, base_ring=QQ)
print (p.integral_points())
