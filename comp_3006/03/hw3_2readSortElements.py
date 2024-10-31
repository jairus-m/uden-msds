import csv

def read_csv(filename : str):
    """
    Read a csv file and convert to a list of tuples.
    Args:
        filename (str) : path to/name of file
    Returns:
        data (list) : list of tuples
    """
    data = []
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f)
        # skip the the first line (header/column names) of csv_reader - Week 4 Topic
        next(csv_reader)

        for line in csv_reader:
            # check each element with the tuples if a number (if so, convert to int)
            for i in range(len(line)):
                try:
                    line[i] = int(line[i])
                except ValueError:
                    pass
            data.append(line)
    return data


def sort_data(data : list, index : int, reverse : bool):
    """
    Sorts list of tuples based on the index of the element within the tuple (row).
    Args:
        data (list): list of tuples
        index (int): index position of element in tuple (row) to sort by
        reverse (bool): True for ascending order, False otherwise
    Returns:
        data (list): sorted list of tuples by chosen element in tuple
    """
    # using lambda function to choose tuple index to sort by
    data.sort(reverse=reverse, key=lambda x: x[index])
    return data

if __name__ == '__main__':
    # sort list in reverse order using the index = 2 for the key (key index 2 = atomic number)
    data = sort_data(read_csv('elements.csv'), 2, reverse=True)
    for line in data:
        print(line)