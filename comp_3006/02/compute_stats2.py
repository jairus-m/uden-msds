import sys
import csv

# for each column, this script will hard code the range to filter values by 
# since some columns contain -9999  or -99 for missing data

def colFromData_Stdin(col : int, textData):
    '''
    This function reads a txt file from standard input, parses it as a CSV, and
    returns a a specified column from that txt file and is meant for this CLI command:
    
    ```python compute_stats2.py col < textData```
    
    Args:
        col (int): column corresponding to column index starting at 1
        textData (.txt file) : textData from standard input (sys.stdin)
    Returns
        list : list containing the specified column elements 
    '''
    csv_reader = csv.reader(textData, delimiter=' ', skipinitialspace=True)


    # Iterate through each row in the file and append it to the data list
    data = []
    for row in csv_reader:
        data.append(row)

    column = []
    for row in data:
         try:
            number = float(row[int(col)-1].strip('\n'))
            # constrain the numbers to realistic temps (-9999 = missing data)
            if number not in [-99, -9999]:
                column.append(number)
         except:
            pass
    column.sort()
    return column

def colFromData_Filename(col : int, filename : str):
    '''
    This function reads in from a filename of a text file, parses it as a CSV, and
    returns a a specified column from that txt file and is meant for this CLI command:
    
    ```python compute_stats2.py 9 data.txt```
        
    Args:
        col (int): column corresponding to column index starting at 1
        filename (str) : string of path/name of text file
    Returns
        list : list containing the specified column elements 
    '''
    data = []
    with open(filename, mode='r') as file:
        # Create a CSV reader object with a comma as the delimiter
        csv_reader = csv.reader(file, delimiter=' ', skipinitialspace=True)

        # Iterate through each row in the file and append it to the data list
        for row in csv_reader:
            data.append(row)

    column = []
    for row in data:
         try:
            number = float(row[int(col)-1].strip('\n'))
            # constrain the numbers to realistic temps (-9999 = missing data)
            if number not in [-9999, -99]:
                column.append(number)
         except:
            pass
    column.sort()
    return column


def average(numbers : list):
    '''
    Calculates the average of the list, numbers.
    Args:
        numbers (list) : list of numbers
    Returns
        avgerage (float)
    '''
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def minimum(numbers : list):
    '''
    Returns the minimum value from a list.
    Args:
        numbers (list) : list of numbers
    Returns:
        minimum (float)
    '''
    numbers.sort()
    return numbers[0]

def maximum(numbers : list):
    '''
    Returns the maximum value from a list.
    Args:
        numbers (list) : list of numbers
    Returns:
        maximum (float)
    '''
    numbers.sort()
    return numbers[-1]

def median(numbers : list):
    '''
    Returns the median value from a list.
    Args:
        numbers (list) : list of numbers
    Returns:
        median (float)
    '''
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        med = (numbers[int(n/2) - 1] + numbers[int((n/2)+1) - 1]) / 2
    else:
        med = numbers[int((n+1)/2) - 1]
    return med

def compute_stats(values : list):
    '''
    This function calculates the average, minimum, maximum, and median
    from a list of number values. 
    Args:
        values (list) : list of numbers
    Returns:
        tuple : (min_, max_, avg_, med_)
    '''
    # if list of values is empty, return None
    if len(values) == 0:
        return None
    else:
        try:
            values.sort()
            avg = average(values)
            min_ = minimum(values)
            max_ = maximum(values)
            med_ = median(values)
            return (min_, max_, avg, med_)
        except TypeError:
            return None
    
def main():
    '''
    This will run the main script for compute_stats2.py. It allows for two options for reading in 
    data: from the standard in and from a text file.
    Args:
        None
    Return:
        string : f'min: {min_}, max: {max_}, average: {avg}, median: {med_}'
    '''
    try:
        # read in data from standard in: ```compute_stats2.py 9 < data.txt```
        col = int(sys.argv[1])
        if len(sys.argv) == 2:
            numbers = colFromData_Stdin(col = sys.argv[1], textData=sys.stdin)

        # read in data from txt file: ```compute_stats2.py 9 data.txt```
        elif len(sys.argv) == 3:
            numbers = colFromData_Filename(col = sys.argv[1], filename=sys.argv[2])
        else:
            raise IndexError

        avg, min_, max_, med_ = average(numbers),  minimum(numbers), maximum(numbers), median(numbers)
        
        return f'min: {min_}, max: {max_}, average: {avg}, median: {med_}'
    
    # exception if arguments are made incorrectly
    except IndexError:
        print("Error with CLI arguments. \nPlease enter command as 'python compute_stats2.py colToExtract < filename.txt' or\n 'python compute_stats2.py colToExtract filename.txt'", file=sys. stderr)
    except FileNotFoundError:
        print("Error with filename. \nPlease enter command as 'python compute_stats2.py colToExtract < filename.txt' or\n 'python compute_stats2.py colToExtract filename.txt'", file=sys. stderr)
    except ValueError:
        print("Error with col argument. Make sure col is an interger value. \nPlease enter command as 'python compute_stats2.py colToExtract < filename.txt' or\n 'python compute_stats2.py colToExtract filename.txt'", file=sys. stderr)
        
if __name__ == '__main__':
    print(main())