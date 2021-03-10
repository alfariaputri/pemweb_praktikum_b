import numpy 
arr = numpy.array([[4,4,5,7,6,4],[9,7,4,6,3,7]])  
print(arr) 

import numpy 
arr = numpy.array([[4,4,5],[7,6,4],[9,7,4],[6,3,7]])  
print(arr) #(no. 1f)

import numpy 
arr = numpy.array([
    [[7,8,5],
    [4,7,7],
    [7,1,9],
    [5,4,10]],
    
    [[2,1,2],
    [9,8,5],
    [3,7,3],
    [4,9,9]],
    
    [[2,9,3],
    [2,4,8],
    [1,6,6],
    [8,1,3]]
    ])  
print(arr) #(no.1g)

import numpy 
arr = numpy.array([
    [[7,8,5],
    [4,7,7],
    [7,1,9],
    [5,4,10]],
    
    [[2,1,2],
    [9,8,5],
    [3,7,3],
    [4,9,9]],
    
    [[2,9,3],
    [2,4,8],
    [1,6,6],
    [8,1,3]]
    ])  
print(arr[::-1]) #(no.2e)

import numpy as np
arr=np.array([
    [1,8,8,2],
    [8,2,1,2],
    [10,1,4,7],
    [1,4,7,8],
    [8,2,3,4]
    ])
arr[0::2] +=1
arr[:,1::2] +=2
print(arr) 
# (no.2d)

import numpy 
arr = numpy.array([
    [[7,8,5],
    [4,7,7],
    [7,1,9],
    [5,4,10]],
    
    [[2,1,2],
    [9,8,5],
    [3,7,3],
    [4,9,9]],
    
    [[2,9,3],
    [2,4,8],
    [1,6,6],
    [8,1,3]]
    ]) 
arrayku = arr.reshape(6,6) 
print(arrayku) #(2f)


import numpy
arr = numpy.array([
    [[5, 10, 10, 7], 
    [7, 8, 4, 10], 
    [9, 10, 2, 5], 
    [1, 8, 9, 3], 
    [6, 10, 5, 2], 
    [4, 6, 9, 4]], 
    
    [[9, 3, 1, 8], 
    [5, 2, 6, 10], 
    [9, 4, 4, 6], 
    [10, 7, 5, 10], 
    [4, 10, 7, 8], 
    [2, 5, 9, 10]]
    ])
print(arr)
variabel = arr[0:, 0:, :2].copy()
arr[0:, 0:, :2] = arr[0:, 0:, 2:]
arr[0:, 0:, 2:] = variabel
print("-----")
print(arr) #3e

