import numpy as np
width, height = 3, 3
n = height * width
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
            A[i][index] = 1
print (np.linalg.det(A))
#print ("inv: ", np.linalg.pinv(A))
print (np.dot(np.linalg.pinv(A), np.ones([n, 1])))
print (np.linalg.solve(A, np.ones([n, 1])))
for box in A:
    print (np.reshape(box, (height, width)))
    print ("\n")
'''
grid = [[1, 2], [3, 4], [5, 6]]

b = np.array(grid).flatten()
print (np.reshape(b, (3, 2)))'''