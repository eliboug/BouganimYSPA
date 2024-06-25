import numpy as np
# method to get determinate of a 2d array

def determinant2d(arr:np.ndarray):
    a = arr[0, 0]
    b = arr[0,1]
    c = arr[1,0]
    d = arr[1,1]
    determinant = (a*d) - (b*c)
    return determinant
# method to get determinate of a 3d array
def determinant3d(arr:np.ndarray):
    # setting all variables for ease of use
    a = arr[0, 0]
    b = arr[0,1]
    c = arr[0,2]
    d = arr[1,0]
    e = arr[1, 1]
    f = arr[1,2]
    g = arr[2,0]
    h = arr[2,1]
    i = arr[2, 2]
    
    # the arrays of which I will need to find the 2x2 determinants
    comb1 = np.array([[e,f], [h, i]])
    comb2 = np.array([[d,f], [g, i]])
    comb3 = np.array([[d,e], [g, h]])
    # final calc
    determinant = a*determinant2d(comb1) - b*determinant2d(comb2) + c*determinant2d(comb3)
    return determinant
   
testarray1 = np.array([[1,2], [3, 4]])
testarray2 = np.array([[1,2,3], [4, 5, 6], [7,8,9]])
print(determinant2d(testarray1))
print(determinant3d(testarray2))
 
