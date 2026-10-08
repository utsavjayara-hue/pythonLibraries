import numpy as np

#definaton
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
#[[1 2 3]
# [4 5 6]
#[7,8,9]]
#methods

print(array.size)# number of elements
print(array.shape)#shape of matrix in the form (x,y) where x is the  number of row and y is the number of collumn
print(array[0,2])#accessing element at (0,2)
print(array*2)#scaler operations


#uses standard slicing

print(array[:,2])#third element of each row
print(array[:,0:2])#first two element of each row

#vector operation
array2 =np.array([1,2,3])
print(array*array2)

#broadcating : smaller array made big by repearting element.for NumPy to broadcast two dimensions together, they must be compatible. Two dimensions are compatible when:They are equal to each other, OR    One of them is 1.

#Agregate functions
print(np.sum(array,0))#0 for collum and 1 for axis
print(np.argmax(array,1))

#filtering
print(array[array>4])#retrun 1d array
print(np.where(array>4,array,0))# return orignal array with the element not followign condition replaced by 0
#random
rng=np.random.default_rng()
print(rng.integers(1,10,(3,3)))# 3*3 array with randominteger from 1 to 9
print(np.random.uniform(-1,1,(3,3)))# 3*3 array with random float  from -1 to 1
