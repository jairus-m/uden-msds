import numpy as np

def compute_partial_sums(x, y):
    """
    Computes the partial sums of two arrays (x and y),
    needed to calculate the regression coefficeints.
    Args:
        x (array) : list of numbers
        y (array) : list of numbers
    Returns:
        tuple : n, sum_x, sum_y, sum_x2, sum_y2, sum_xy
    """
    n = len(x)

    sum_x = np.sum(x)
    sum_y = np.sum(y)

    sum_x2 = np.sum(x**2)
    sum_y2 = np.sum(y**2)

    sum_xy = np.sum(x * y)
    
    return n, sum_x, sum_y, sum_x2, sum_y2, sum_xy

def update_partial_sums(stats1, stats2):  
    """
    Takes in the partial sums of the already computed data points
    and new data points, and calcualates the partial sums of the combined results.
    Args:
        stats1 (tuple) : partial sums returned by compute_summary_statistics()
        stats2 (tuple) : partial sums returned by compute_summary_statistics()
    Returns:
        tuple : n, sum_x, sum_y, sum_x2, sum_y2, sum_xy
    """
    n1, sum_x1, sum_y1, sum_x2_1, sum_y2_1, sum_xy1 = stats1
    n2, sum_x2, sum_y2, sum_x2_2, sum_y2_2, sum_xy2 = stats2
    
    n = n1 + n2
    sum_x = sum_x1 + sum_x2
    sum_y = sum_y1 + sum_y2
    sum_x2 = sum_x2_1 + sum_x2_2
    sum_y2 = sum_y2_1 + sum_y2_2
    sum_xy = sum_xy1 + sum_xy2
    
    return n, sum_x, sum_y, sum_x2, sum_y2, sum_xy

def compute_regression_coefficients(stats):
    """
    Take the necessary partial sums to calculate the 
    final regression coefficeints. 
    Args:
        stats (tuple) : partial sums returned by compute_summary_statistics() or 
                        update_summary_statistics()
    Returns:
        tuple : beta_0, beta_1 (where beta_0 = y-intercept and beta_1 = slope)
    """
    n, sum_x, sum_y, sum_x2, sum_y2, sum_xy = stats
    
    S_xx = sum_x2 - (sum_x**2 / n)
    S_xy = sum_xy - (sum_x * sum_y / n)
    
    beta_1 = S_xy / S_xx
    beta_0 = (sum_y / n) - beta_1 * (sum_x / n)
    
    return beta_0, beta_1


if __name__ == '__main__':
    # initial data points
    x_initial = np.random.rand(1000000)
    # y = 6.5x + 500
    print('\nInitial data: y = 6.5x + 500\n')
    y_initial = 6.5 * x_initial+ 500 + np.random.randn(1000000) * 0.5 

    # get initial data points partial sums
    sums_initial = compute_partial_sums(x_initial, y_initial)

    beta_0, beta_1 = compute_regression_coefficients(sums_initial)

    print('Initial calculated regression coefficients:')
    print(f'Intercept (beta_0): {beta_0}')
    print(f'Slope (beta_1): {beta_1}')


    # new data points
    x_new = np.random.rand(50000)
    # y = 2.5x + 100
    print('\nNew data: y = 0.5x + 100\n')
    y_new = .5 * x_new + 100 + np.random.randn(50000) * 0.5  

    # get new data data points partial sums
    sums_new = compute_partial_sums(x_new, y_new)

    beta_0, beta_1 = compute_regression_coefficients(sums_new)

    print('New data calculated regression coefficients:')
    print(f'Intercept (beta_0): {beta_0}')
    print(f'Slope (beta_1): {beta_1}')

    # combine the old and new partial sums to calcualte regression coefficeints
    sums_combined = update_partial_sums(sums_initial, sums_new)

    # calc regression coefficients
    beta_0, beta_1 = compute_regression_coefficients(sums_combined)

    print('\nCombined/updated regression coefficients:')
    print(f'Intercept (beta_0): {beta_0}')
    print(f'Slope (beta_1): {beta_1}\n')

# TERMINAL OUTPUT

# Initial data: y = 6.5x + 500
# 
# Initial calculated regression coefficients:
# Intercept (beta_0): 500.0000854891037
# Slope (beta_1): 6.499746050117159
# 
# New data: y = 0.5x + 100
# 
# New data calculated regression coefficients:
# Intercept (beta_0): 99.99804792095856
# Slope (beta_1): 0.5032682444480296
# 
# Combined/updated regression coefficients:
# Intercept (beta_0): 481.02791052410385
# Slope (beta_1): 6.0627945907605945