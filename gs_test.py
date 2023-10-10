import numpy as np


def gram_schmidt(A):
    
    (n, m) = A.shape
    
    for i in range(m):
        
        q = A[:, i] # i-th column of A
        
        for j in range(i):
            q = q - np.dot(A[:, j], A[:, i]) * A[:, j]
        
        if np.array_equal(q, np.zeros(q.shape)):
            raise np.linalg.LinAlgError("The column vectors are not linearly independent")
        
        # normalize q
        q = q / np.sqrt(np.dot(q, q))
        
        # write the vector back in the matrix
        A[:, i] = q

m = np.array([[85, 51, 60, 6],
              [60, 20, 12, 77],
              [81, 60, 84, 91],
              [65, 34, 81, 26]])

gram_schmidt(m)

print(m)
