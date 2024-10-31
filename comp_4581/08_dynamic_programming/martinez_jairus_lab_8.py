def printMatrix(m):
    """
    Nicely print out a matrix.
    Args:
        m (list): matrix to be printed
    Returns:
        None
    """
    for row in m:
        print(row)

def chainMatrix(p):
    """
    Matrix chain multiplication thru dynamic programming.
    Args:
        p (list): dimensions of the matrices (has dimensions p[i-1] x p[i])
    Returns:
        int: min number of scalar multiplications needed to multiply the chain of matrices
    """
    # empty 2-D table
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    
    # base case vals across diagonals
    for i in range(n):
        m[i][i] = 0
        
    # fill table diagonal by diagonal on the right side of base case diag (refer to slide 22 of lecture)
    for chainlength in range(2, n + 1):
        for i in range(n - chainlength + 1):
            j = i + chainlength - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    # track cost and traceback
    print("\nCost matrix:\n")
    printMatrix(m)
    print("\nTraceback matrix:\n")
    printMatrix(s)
    
    # optimal parenthesization
    optimal_parens = parenStr(s, 0, n - 1)
    print("\nOptimal parenthesization:")
    print(optimal_parens)
    
    return m[0][n - 1]

def parenStr(s, i, j):
    """
    Recursively construct the optimal parenthesization for the matrix chain multiplication problem.
    Args:
        s (list): traceback matrix that indicates the optimal splits.
        i (int): starting index of the matrix chain.
        j (int): ending index of the matrix chain.
    Returns:
        str: string of optimal parenthesization
    """
    if i == j:
        return f"A{i}"
    else:
        k = s[i][j]
        left_part = parenStr(s, i, k)
        right_part = parenStr(s, k + 1, j)
        return f"({left_part}{right_part})"

if __name__ == '__main__':
    dims = [30, 35, 15, 5, 10, 20, 25]
    optimal_cost = chainMatrix(dims)
    print(f"\nOptimal cost: {optimal_cost}\n")

# TERMINAL OUTPUT

# Cost matrix:
# 
# [0, 15750, 7875, 9375, 11875, 15125]
# [0, 0, 2625, 4375, 7125, 10500]
# [0, 0, 0, 750, 2500, 5375]
# [0, 0, 0, 0, 1000, 3500]
# [0, 0, 0, 0, 0, 5000]
# [0, 0, 0, 0, 0, 0]
# 
# Traceback matrix:
# 
# [0, 0, 0, 2, 2, 2]
# [0, 0, 1, 2, 2, 2]
# [0, 0, 0, 2, 2, 2]
# [0, 0, 0, 0, 3, 4]
# [0, 0, 0, 0, 0, 4]
# [0, 0, 0, 0, 0, 0]
# 
# Optimal parenthesization:
# 
# ((A0(A1A2))((A3A4)A5))     
# 
# Optimal cost: 15125
