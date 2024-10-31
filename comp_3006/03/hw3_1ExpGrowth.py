import csv
    
def expGrowth(x_0, a, d_t, start=0, stop=2):
    '''
    This function will simulate population exponential growth. 
    Args:
        x_0 (int) : starting population size
        a (int) : growth parameter
        d_t (int) : time step of simulation
        start (int) : start time (default set at 0)
        stop (int) : stop time of simulation (default set at 2)
    Returns:
        population_sizes (list) : population size at every time step.
    '''
    # create the list of time intervals and population sizes (input initial data)
    time_intervals = [start]
    population_sizes = [x_0]
    
    # initiate time to starting time
    time = start
    current_population = x_0
    while time < stop:
        # xdot : rate of change
        xdot = a * current_population
        # increase population by adding the rate of change * time step
        current_population += xdot * d_t
        time += d_t
        
        # update the list
        time_intervals.append(time)
        population_sizes.append(current_population)

    # create a list of data containing time steps and population sizes
    data = [('Time', 'Population')]
    data.extend(list(zip(time_intervals, population_sizes)))
    
    return data
   
def dataToCSV(data, filename):
    '''
    This function takes in data (list of tuples) and exports 
    it as a CSV file.
    Args:
        data (list): list of tuples (each tuple within list is a row)
        filename (str): string to name file (filename.csv)
    Returns:
        None
    '''
    # Save results to a CSV file
    with open(filename, 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(data)
    return
   

if __name__ == '__main__':
    # assign params given by assigment
    data = expGrowth(x_0=100, a=5, d_t=0.1)
    
    # write data to a csv file
    dataToCSV(data, 'populationGrowth.csv')
    
    # output data to console
    for line in data:
        print(line)
