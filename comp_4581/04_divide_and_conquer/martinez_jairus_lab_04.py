# 1D Implementation 

def cPairDist(points: list):
    """
    Sorts the list of points and then calls recCPairDist().
    Args:
        points (list) : list containing points on a 1D plane
    Returns
        int : minimum distance between all pair combinatoins in list
    """
    points.sort()
    return recCPairDist(points)

def recCPairDist(points: list):
    """
    Recursively calcualtes the minimum distance between 
    points via divide and conquer alorithm.
    Args:
        points (list) : list containing points on a 1D plane
    Returns
        int : minimum distance between all pair combinatoins in list
    """
    n = len(points)
    
    # one element list,  distance = 0
    if n <= 1:
        # print(f'n = {n}')
        return float('inf') # previously, I returned 0 but that was causing  
                            # unexpected behaviour with odd length lists
    # two elemenet list, distance between the 1st and 2nd element
    elif n == 2:
        # print(f'n = {n}')
        return abs(points[0] - points[1])
    
    # print(f'n = {n}')
    # cut list in half
    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]
    
    # part 1 and 2: recursively find the closest distance in each half
    min_left = recCPairDist(left_half)
    min_right = recCPairDist(right_half)
    
    # part 3: closest distance between the two halves
    min_split = abs(points[mid] - points[mid - 1])
    
    return min(min_left, min_right, min_split)

# CIRCLE IMPLEMENTATION

def cPairDistCircle(points: list, circumference: int):
    """
    Sorts the list of points and then calls recCPairDistCircle().
    Similar implementatino to 1D but with speacial case for circular list.
    Args:
        points (list) : list containing points on a 1D circular path
        circumference (int) : the circumference of the circle
    Returns
        int : minimum distance between all pair combinations in list
    """
    points.sort()
    return recCPairDistCircle(points, circumference)

def recCPairDistCircle(points: list, circumference: int):
    """
    Recursively calculates the minimum distance between 
    points with DAC algorithm on a circle.
    Args:
        points (list) : list containing points on a 1D circular path
        circumference (int) : the circumference of the circle
    Returns
        int : minimum distance between all pair combinations in list
    """
    n = len(points)
    
    # one element list, distance = 0
    if n <= 1:
        return float('inf')
    # two element list, distance between the 1st and 2nd element
    elif n == 2:
        # # find the min of 1. both elements 2. 2nd element of circle distance 3. 1st element of circle distance 
        return min(abs(points[0] - points[1]), abs(circumference - points[1]), points[0])
    
    # split!
    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]
    
    # recursively find the closest distance in each half via recursive DAC as normal
    min_left = recCPairDistCircle(left_half, circumference)
    min_right = recCPairDistCircle(right_half, circumference)
    
    # speacial cases to comare: 
    # find the min of 1. middle spit distance 2. end of circle distance 3. beginning of circle distance 
    min_split_circle = min(abs(points[mid] - points[mid - 1]), abs(circumference - points[-1]), points[0])
    
    return min(min_left, min_right, min_split_circle)

if __name__ == '__main__':

    print('\nPART 1: 1D LINE') 
    points1 = [7, 4, 12, 14, 2, 10, 16, 6]
    points2 = [7, 4, 12, 14, 2, 10, 16, 5]
    points3 = [14, 8, 2, 6, 3, 10, 12]

    print(f'\nPoints1 = {points1}:\n')
    print(f'\tshortest distance (expect 1 - between 6 and 7): {cPairDist(points1)}')  # exxpect 1 (between 6 and 7)
    print(f'\nPoints2 = {points2}:\n')
    print(f'\tshortest distance (expect 1 - between 4 and 5): {cPairDist(points2)}')  # expect 1 (between 4 and 5)
    print(f'\nPoints3 = {points3}:\n')
    print(f'\tshortest distance (expect 1 - between 2 and 3): {cPairDist(points3)}') # expect 1 (between 2 and 3)

    print('\nPART 2: OPTIONAL PART CIRCLE') 

    CIRCUMFRENCE = 20
    points1 = [10, 3, 16, 12] # expect 2 (between 10 and 12)
    points2 = [6, 2, 9, 17, 14] # expect 2 (between 20 and 2)
    points3 = [6, 16, 11] # expect 4 (between 16 and 20)
    points4 = [7, 14] # expect 6 (between 14 and 20)

    print(f'Circumfrence = {CIRCUMFRENCE}')
    print(f'\nPoints1 = {points1}:\n')
    print(f'\tshortest distance (expect 2 - between 10 and 12): {cPairDistCircle(points1, CIRCUMFRENCE)}')  
    print(f'\nPoints2 = {points2}:\n')
    print(f'\tshortest distance (expect 2 - between 20 and 2): {cPairDistCircle(points2, CIRCUMFRENCE)}')  
    print(f'\nPoints3 = {points3}:\n')
    print(f'\tshortest distance (expect 4 - between 16 and 20): {cPairDistCircle(points3, CIRCUMFRENCE)}')  
    print(f'\nPoints4 = {points4}:\n')
    print(f'\tshortest distance (expect 6 - between 14 and 20): {cPairDistCircle(points4, CIRCUMFRENCE)}')  



# TERMINAL OUTPUT
# 
# PART 1: 1D LINE
# 
# Points1 = [7, 4, 12, 14, 2, 10, 16, 6]:
# 
#         shortest distance (expect 1 - between 6 and 7): 1
# 
# Points2 = [7, 4, 12, 14, 2, 10, 16, 5]:
# 
#         shortest distance (expect 1 - between 4 and 5): 1
# 
# Points3 = [14, 8, 2, 6, 3, 10, 12]:
# 
#         shortest distance (expect 1 - between 2 and 3): 1
# 
# PART 2: OPTIONAL PART CIRCLE
# Circumfrence = 20
# 
# Points1 = [10, 3, 16, 12]:
# 
#         shortest distance (expect 2 - between 10 and 12): 2
# 
# Points2 = [6, 2, 9, 17, 14]:
# 
#         shortest distance (expect 2 - between 20 and 2): 2
# 
# Points3 = [6, 16, 11]:
# 
#         shortest distance (expect 4 - between 16 and 20): 4
# Points4 = [7, 14]:
#
#         shortest distance (expect 6 - between 14 and 20): 6

# Challenge: think about a possible way to implement a DAC method if we had a collection of points on the plane. 
# Can you think of an approach which would work, without adding too much computational complexity? 
# Sometimes we learn by trying, even if we cannot do something… 

# Brainstorm using DAC?
# 1. Create two 1D arrays - one that is the x-axis and one that contains the y-axis
# 2. Use DAC recursively like normal on the x-axis array to find the closest points 
# 3. Use that minimum x-axis distance to then sort the Y-axis array and then .... ?
# I am not too sure about the best way to use DAC for this problem :(

# Brute Force?
# Calculate each euclidean distance between each point in the plane
# Save the distances in a dict where the key is the pair of points and the value is the distance
# Get the minimum distance
# super not efficient haha
