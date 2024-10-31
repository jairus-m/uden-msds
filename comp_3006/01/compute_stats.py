import sys

def read_stdin(input_lines):
    '''
    This function reads in the stdout from a pipelined program as 
    the stdin and returns a list of float values.
    Args:
        input_lines : stdout txt from another program
    Returns:
        numbers (list)
    '''
    numbers = []
    for line in input_lines:
        try:
            number = float(line.strip('\n'))
            # constrain the numbers to realistic temps (-9999 and -99 = missing data)
            if number not in [-9999, 99]:
                numbers.append(number)
        except:
            pass
    return numbers

def average(numbers):
    '''
    Calculates the average of a list of numbers.
    Args:
        numbers (list) : list of numbers
    Returns
        average (float)
    '''
    numbers.sort()
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def minimum(numbers):
    '''
    Returns the minimum value from a list of numbers.
    Args:
        numbers (list) : list of numbers
    Returns:
        minimum (float)
    '''
    numbers.sort()
    return numbers[0]

def maximum(numbers):
    '''
    Returns the maximum value of a list of numbers.
    Args:
        numbers (list) : list of numbers
    Returns:
        maximum (float)
    '''
    numbers.sort()
    return numbers[-1]

def median(numbers):
    '''
    Returns the median value from a list of numbers.
    Args:
        numbers (list) : list of numbers
    Returns:
        median (float)
    '''
    numbers.sort()
    
    n = len(numbers)
    # median calculation for even numbers
    if n % 2 == 0:
        med = (numbers[int(n/2) - 1] + numbers[int((n/2)+1) - 1]) / 2
    # median calculation for off numbers
    else:
        med = numbers[int((n+1)/2) - 1]
    return med

def main():
    '''
    This is the main function of the script. It takes in the standard input 
    from a piped txt file and calculates the average/minimum/maximum/median of the data.
    Args:
        None
    Returns
        string : f'min: {min_}, max: {max_}, average: {avg}, median: {med_}'
    '''
    # read in the data
    input_lines = sys.stdin.readlines()
    
    # convert the data from the txt file into a list of numbers
    numbers = read_stdin(input_lines)
    
    # compute statistics
    avg, min_, max_, med_ = average(numbers),  minimum(numbers), maximum(numbers), median(numbers)
    return f'min: {min_}, max: {max_}, average: {avg}, median: {med_}'

if __name__ == '__main__':
    print(main())