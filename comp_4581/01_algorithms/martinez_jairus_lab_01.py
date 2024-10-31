import timeit
import numpy as np

def printMatrix(m):
    """
    Prints the matrix nicely
    Args:
        m : matrix
    Returns:
        None
    """
    for row in m:
        print(row)

def matrixMult(A, B):
    """
    Caclulates the matrix multiplcation of 
    two matrices, A and B.
    Args:
        A: matrix (q x p)
        B: matrix (p x r)
    Returns:
        C: Resultant Matrix (q x r)
    """
    if len(A[0]) == len(B):
        # get the dimensions 
        q = len(A)
        p = len(A[0])
        r = len(B[0])
        
        # set dimensions of matrix C (q rows, r cols)
        C = [[0 for _ in range(r)] for _ in range(q)] 

       # loop through rows of A
        for i in range(q):
            # loop through cols of B
            for j in range(r):
                # loop through cols of A and rows of B
                for k in range(p):
                    # set the element in the resultant matrix C
                    C[i][j] += A[i][k] * B[k][j]
        return C
    else:
        print('Matrices have no compatible dimensions!')
        return None
    
def test_custom_mult():
    """
    Runs custom matrix multiplication
    results for timing.
    Args:
        None
    Returns:
        None
    """
    matrixMult(A, B)

def test_numpy_mult():
    """
    Runs Numpy matrix multiplication
    results for timing.
    Args:
        None
    Returns:
        None
    """
    np.matmul(A, B)
    
if __name__ == '__main__':
    # Test1
    print('\nTest Case 1 Results:\n')
    A = [[ 2, -3, 3],
        [-2, 6, 5],
        [ 4, 7, 8]]

    B = [[-1, 9, 1],
        [ 0, 6, 5],
        [ 3, 4, 7]]
    C = matrixMult(A, B)
    if not C == None:
        printMatrix(C)
        #print(np.matmul(A,B))
        assert C == [[7, 12, 8], [17, 38, 63], [20, 110, 95]] 

    # Test2
    print('\nTest Case 2 Results:\n')
    A = [[ 2, -3, 3, 0],
        [-2, 6, 5, 1],
        [ 4, 7, 8, 2]]
    B = [[-1, 9, 1],
        [ 0, 6, 5],
        [ 3, 4, 7]]
    C = matrixMult(A, B)

    if not C == None:
        printMatrix(C)
        #print(np.matmul(A,B))
        assert C == None

    # # Test3
    print('\nTest Case 3 Results:\n')
    A = [[ 2, -3, 3, 5],
        [-2, 6, 5, -2]]
    B = [[-1, 9, 1],
        [ 0, 6, 5],
        [ 3, 4, 7],
        [ 1, 2, 3]]
    C = matrixMult(A, B)
    if not C == None:
        printMatrix(C)
        #print(np.matmul(A,B))
        assert C == [[12, 22, 23], [15, 34, 57]]

    # Comparing the times!

    print('\nCompare the Times:\n')

    custom_time = timeit.timeit(test_custom_mult, number=1000)
    print(f"Custom matrix multiplication time: {custom_time:.6f} seconds")

    numpy_time = timeit.timeit(test_numpy_mult, number=1000)
    print(f"NumPy matrix multiplication time: {numpy_time:.6f} seconds\n")

# Test Case 1 Results:

# [7, 12, 8]
# [17, 38, 63]
# [20, 110, 95]

# Test Case 2 Results:

# Matrices have no compatible dimensions!

# Test Case 3 Results:

# [12, 22, 23]
# [15, 34, 57]

# Compare the Times:

# Custom matrix multiplication time: 0.007119 seconds
# NumPy matrix multiplication time: 0.005738 seconds