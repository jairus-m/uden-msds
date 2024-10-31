import random
from time import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def merge(left, right):
    """
    Function to merge two sorted lists.
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
    Returns:
        list: The merged and sorted list.
    """
    result = []
    i = j = 0
    
    # go thru both lists and insert the smallest element from either list into the result list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # if remaining elements in the left list, add them to the result
    while i < len(left):
        result.append(left[i])
        i += 1
        
    # if remaining elements in the right list, add them to the result
    while j < len(right):
        result.append(right[j])
        j += 1
        
    return result

def mergeSort(L):
    """
    Function to sort an array using merge sort algo.
    Args:
        L (list): The list of elements to be sorted.
    Returns:
        list: The sorted list.
    """
    # base case - if list length = 1, it's already sorted
    if len(L) < 2:
        return L[:]
    else:
        # find middle index
        mid = len(L) // 2
        
        # recursively sort left side
        left = mergeSort(L[:mid])
        
        # recursively sort right side
        right = mergeSort(L[mid:])
        
        # merge!
        return merge(left, right)
    
def insertionSort(L):
    """
    Function to sort an array using insertion sort algo.
    Args:
        L (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    # go thru 1 to len(L) since the first element is considered sorted
    for i in range(1, len(L)):
        key = L[i]  # current element to be compared and inserted
        j = i - 1    # index of previous element

        # move elements that are greater than key, to one position ahead of current
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]  
            j -= 1         
        L[j + 1] = key 
    return L

def bubbleSort(L):
    """
    Function to sort an array using bubble sort algo.
    Args:
        L (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(L)
    # index of element in list
    for i in range(n):
        # get index of comparison element
        for k in range(0, n-i-1):
            # swap index if current element is smaller than larger element
            if L[k] > L[k + 1]:
                L[k], L[k + 1] = L[k + 1], L[k]
    return L

def time_sorting_algorithm(algorithm, L):
    """
    Timing function for different sort algos.
    Args:
        algorithm (function): sorting function
        L (list): The list of elements to be sorted.
    Returns:
        float: Time in milliseconds 
    """
    t1 = time()
    algorithm(L)
    t2 = time()
    return (t2 - t1) * 1000

def merge_sort_fit(n, a):
    """
    Fit function for merge sort time complexity.
    This function models the time complexity as a * n * log(n), where 'a' is a constant to be determined.
    The merge sort algorithm has an average time complexity of O(n log n).
    Args:
        n (array): Input array of sizes, pd.Series for this specific case
        a (float): Coefficient to be determined by curve fitting.
    Returns:
        array: Computed merge sort times for the input sizes.
    """
    return a * n * np.log(n)

def quadratic_fit(n, a, b, c):
    """
    Quadratic fit function for sorting algorithms with O(n^2) complexity.
    
    Both insertion sort and bubble sort have an average time complexity of O(n^2).
    This function models the time complexity as a * n^2 + b * n + c, where 'a', 'b', and 'c' are constants to be determined.
    
    Args:
        n (array-like): Input array of sizes.
        a (float): Quadratic coefficient to be determined by curve fitting.
        b (float): Linear coefficient to be determined by curve fitting.
        c (float): Constant term to be determined by curve fitting.
    Returns:
        array: Computed sorting times for the input sizes.
    """
    return a * n**2 + b * n + c
    
if __name__ == '__main__':
    n = 25
    A = [i for i in range(n)]
    random.shuffle(A)
    print(f'Unsorted list:\n{A}\n')
    print(f'Merge Sort:\n{mergeSort(A)}\n')
    print(f'Insertion Sort:\n{insertionSort(A)}\n')
    print(f'Bubble Sort:\n{bubbleSort(A)}\n')

    data = []
    print(f"{'n':<8}{'Merge':<9}{'Insertion':<12}{'Bubble':<10}")
    for n in range(100, 5500, 500):
        A = [random.randint(0, 10000) for _ in range(n)]
        
        B = A[:]
        merge_sort_time = time_sorting_algorithm(mergeSort, B)
        
        C = A[:]
        insert_sort_time = time_sorting_algorithm(insertionSort, C)
        
        D = A[:]
        bubble_sort_time = time_sorting_algorithm(bubbleSort, D)

        data_entry = {
            'n': n,
            'merge_sort_time': merge_sort_time,
            'insert_sort_time': insert_sort_time,
            'bubble_sort_time': bubble_sort_time
            }
        data.append(data_entry)
        
        print(f"{n:<8}{round(merge_sort_time, 2):<9}{round(insert_sort_time, 2):<12}{round(bubble_sort_time, 2):<10}")
    
    # save the data into a pandas df
    df = pd.DataFrame(data)

    n = df['n']
    merge_sort_time = df['merge_sort_time']
    insert_sort_time = df['insert_sort_time']
    bubble_sort_time = df['bubble_sort_time']

    # fit data
    merge_params, _ = curve_fit(merge_sort_fit, n, merge_sort_time)
    insert_params, _ = curve_fit(quadratic_fit, n, insert_sort_time)
    bubble_params, _ = curve_fit(quadratic_fit, n, bubble_sort_time)

    #  fit lines
    n_fit = np.linspace(100, 5100, 500)
    merge_fit = merge_sort_fit(n_fit, *merge_params)
    insert_fit = quadratic_fit(n_fit, *insert_params)
    bubble_fit = quadratic_fit(n_fit, *bubble_params)

    # plot points!
    plt.figure(figsize=(14, 8))
    plt.scatter(n, merge_sort_time, color='red')
    plt.scatter(n, insert_sort_time, color='purple')
    plt.scatter(n, bubble_sort_time, color='green')

    # plot lines with speacial lines / labels
    plt.plot(n_fit, merge_fit, label=f'Merge Sort Fit: {merge_params[0]:.2e} * n * log(n)', color='red', linestyle='--')
    plt.plot(n_fit, insert_fit, label=f'Insertion Sort Fit: {insert_params[0]:.2e} * n^2 + {insert_params[1]:.2e} * n + {insert_params[2]:.2e}', color='purple', linestyle='--')
    plt.plot(n_fit, bubble_fit, label=f'Bubble Sort Fit: {bubble_params[0]:.2e} * n^2 + {bubble_params[1]:.2e} * n + {bubble_params[2]:.2e}', color='green', linestyle='--')

    # plot attributes 
    plt.xlabel('n')
    plt.ylabel('Time (milliseconds)')
    plt.legend()
    plt.title('Time to Sort (ms) vs. Number of Elements in List (n)')

    n = 1_000_000
    print('\nOPTIONAL PART:\n')
    print('Computed Compute time for 1,000,000 Observations:')
    print(f'Merged: {merge_sort_fit(n, *merge_params) * 0.001:.2f} seconds')
    print(f'Insertion: {quadratic_fit(n, *insert_params) * 0.001 / 60 / 60:.2f} hours')
    print(f'Bubble: {quadratic_fit(n, *bubble_params) * 0.001 / 60 / 60:.2f} hours')

    plt.show()
    

# Terminal Output
#
# Unsorted list:
# [22, 15, 16, 10, 21, 5, 11, 3, 19, 24, 17, 20, 7, 6, 9, 2, 23, 14, 4, 18, 12, 8, 0, 1, 13]
# 
# Merge Sort:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# 
# Insertion Sort:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# 
# Bubble Sort:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# 
# n       Merge    Insertion   Bubble    
# 100     0.21     0.28        0.53      
# 600     1.58     10.71       19.28     
# 1100    2.7      36.2        68.09     
# 1600    4.18     76.37       149.34    
# 2100    5.52     136.89      265.3     
# 2600    7.22     212.87      410.24    
# 3100    8.69     297.79      580.69    
# 3600    10.31    400.8       781.1     
# 4100    11.76    522.46      1023.51   
# 4600    14.0     669.93      1306.08   
# 5100    15.54    825.9       1597.26   
# 
# OPTIONAL PART:
# 
# Computed Compute time for 1,000,000 Observations:
# Merged: 4.88 seconds
# Insertion: 9.08 hours
# Bubble: 17.52 hours
# 
# Prints out matplotlib plot with curves! (attatched to submission)