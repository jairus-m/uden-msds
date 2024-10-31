import csv
import sys
import os
import requests
import logging
import argparse
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# get the root logger, set default to DEBUG
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#  file handler --> debug info to log file
fh = logging.FileHandler('autompg3.log', 'w')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# stream handler --> warning/errors to console
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)

class AutoMPG:
    """Class representing the autompg.data.txt dataset.
        Attributes:
            make (str) : automobile manufacturer
            model (str) : automobile model
            year (int) : automobile year of manufacture
            mpg (float) : miles per gallon
        Methods:
            __init__ : constructor with 4 attributes
            __repr__ : returns string representation
            __str__ : returns string representation
            __eq__ : implements equality comparison between two AutoMPG objects
            __lt__ : implements less-than comparison between two AutoMPG objects
            __hash__ : allows AutoMPG objects to be hashed
        """
    def __init__(self, make:str, model:str, year:int, mpg:float):
        """Class constructor"""
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
    
    def __str__(self):
        """String representation of AutoMPG Object"""
        return f'AutoMPG({self.make}, {self.model}, {self.year}, {self.mpg})'
    
    def __repr__(self):
        """String representation of AutoMPG Object"""
        return self.__str__()
    
    def __eq__(self, other):
        """Equality method"""
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and self.year == other.year and self.mpg == other.mpg
        else:
            return NotImplemented
        
    def __lt__(self, other):
        """Less than / Greater than method"""
        if type(self) == type(other):
            # Compare 'make' attribute first
            if self.make < other.make:
                return True
            elif self.make > other.make:
                return False

            # If 'make' is the same, compare 'model' attribute
            if self.model < other.model:
                return True
            elif self.model > other.model:
                return False

            # If 'make' and 'model' are the same, compare 'year' attribute
            if self.year < other.year:
                return True
            elif self.year > other.year:
                return False

            # If 'make', 'model', and 'year' are the same, compare 'mpg' attribute
            return self.mpg < other.mpg
        else:
            return NotImplemented
    def __hash__(self):
        """Make AutoMPG class object hashable"""
        return hash((self.make, self.model, self.year, self.mpg))
    

class AutoMPGData:
    """
    This class represents the entire AutoMPG dataset.
    Attributes:
        data (list) : list containing AutoMPG class objects created from auto-mpg.clean.txt
    Methods
        __init__ : contructor with no args
        __iter__ : allows class to be iterable
        _load_data : loads cleaned data and creates AutoMPG objects
        _clean_data : creates clean (auto-mpg.clean.txt) dataset from original dataset (auto-mpg.data.txt)
        sort_by_default : uses the list.sort method to sort the data list in place using the default __lt__ operator (make, model, year, mpg)
        _get_data : downloads/saves original data file from UCI ML Repo if the auto-mpg.data.txt file does not locally exist
        sort_by_year : uses the list.sort method to sort the data based on year first (year, make, model, mpg)
        sort_by_mpg : uses the list.sort method to sort the data based on mog (mpg, make, model, year)
        mpg_by_year : returns a dictionary where keys are years and the values are avg MPG for all cars in that year
        mpg_by_make : returns a dictionary where keys are car make and the values are avg MPG for all cars for that make
    """
    def __init__(self):
        """
        Constructor with no args. Calls _load_data() method
        and initializes self.data list.
        """
        logging.info('AutoMPGData object initialized.')
        self.data = []
        self._load_data()

    def __iter__(self):
        """Makes the AutoMPGData class iterable and returns self.data"""
        return iter(self.data)
    
    def _load_data(self):
        """
        Loads auto-mpg.clean.txt, instantiates AutoMPG objects, and adds them to 
        self.data list attribute. If txt file does not exist, will call _clean_data().
        """
        if not os.path.exists('auto-mpg.clean.txt'):
            logging.debug('Data file does not exist.')
            self._get_data()
            self._clean_data()

        data = []
        # read clean data and parse out relevant fields
        with open('auto-mpg.clean.txt', 'r') as f:
            next(f)
            for line in f:
                make, model, year, mpg = tuple(line.split(','))
                year = int(year)
                mpg = float(mpg)

                # create AutoMPG object from field values and append to self.data
                auto = AutoMPG(make, model, year, mpg)
                logging.debug(f'Processing autoMPG object: {auto}')
                self.data.append(auto)
        logging.info('Sucessfully processed autoMPG Data!')

    def _clean_data(self):
        """
        Reads orignal txt data file and creates new, cleaned txt file (auto-mpg.clean.txt)
        """
        logging.debug('Attempting to clean data.')
        # instantiate the headers of the relevant fields as a tuple in the data list object
        data = [('Make', 'Model', 'Year', 'MPG')]
        with open('auto-mpg.data.txt', 'r') as file:
            csv_reader = csv.reader(file, delimiter=' ')
            for line in csv_reader:
                # filter out all spaces
                line = [x for x in line if x != '']

                # pack relevant field data into variables and append as tuple to data list
                make, model, year, mpg = ' '.join(line[7:]).split()[1].strip('"').title(), ' '.join(line[8:]).strip('"').title(), '19' + line[6], line[0]

                # check and fix typos (hard code solution yuck!)
                typos = {'chevroelt':'chevrolet', 'chevy':'chevrolet', 'maxda':'mazda','mercedes-benz':'mercedes',
                         'toyouta':'toyota','vokswagen':'volkswagen', 'vw':'volkswagen'}
                
                if make.lower() in typos.keys():
                    make = typos[make.lower()].title()

                data.append((make, model, year, mpg))

        # write data file to txt file       
        with open('auto-mpg.clean.txt', 'w') as f:
            for line in data:
                line = ','.join(map(str, line)) + '\n'
                f.write(line)
        logging.debug('Data cleaned.')
    def _get_data(self):
        """
        This method uses the request module to grab the auto mpg text data and saves it as a txt file.
        """
        logging.info('Calling _get_data() method to get data from internet.')
        # link to auto mpg text data
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

        try:
            # get request to URL
            response = requests.get(url)

            # raise error if request not successful (200)
            response.raise_for_status()

            # save data as txt file
            with open('auto-mpg.data.txt', 'w') as f:
                f.write(response.text)
            logging.debug('Sucessfully downloaded data from internet.')
        except requests.exceptions.RequestException as e:
            logging.error('_get_data() failed')
            logging.error(f'Shit did not work. Could not successfully download data. Error: {e}')

    def sort_by_default(self):
        """
        Sorts data by default order make, model, year, mpg
        """
        return self.data.sort()
    def sort_by_year(self):
        """
        Sorts data by year first (year, make, model, mpg)
        """
        return self.data.sort(key=lambda auto: (auto.year, auto.make, auto.model, auto.mpg))
    def sort_by_mpg(self):
        """
        Sorts data by mpg first (mpg, make, model, year)
        """
        return self.data.sort(key=lambda auto: (auto.mpg, auto.make, auto.model, auto.year))
    def mpg_by_year(self):
        """
        Returns dictionary where keys are the unique years in the dataset
        and the values are the avg mpg for all cars in a year.
        """
        # create a dict that logs both the total mpg and counts per year
        year_mpgs = defaultdict(lambda: [0,0])
        for car in self.data:
            year_mpgs[car.year][0] += car.mpg
            year_mpgs[car.year][1] += 1

        # use mpg total and year count to get avg mpg per year
        for year in year_mpgs.keys():
            year_mpgs[year] = np.round(year_mpgs[year][0] / year_mpgs[year][1], 1)

        return year_mpgs
    def mpg_by_make(self):
        """
        Returns dictionary where keys are the unique make in the dataset
        and the values are the avg mpg for all cars of that make.
        """ 
        make_mpgs = defaultdict(lambda: [0,0])
        for car in self.data:
            make_mpgs[car.make][0] += car.mpg
            make_mpgs[car.make][1] += 1

        # use mpg total and year count to get avg mpg per year
        for make in make_mpgs.keys():
            make_mpgs[make] = np.round(make_mpgs[make][0] / make_mpgs[make][1], 1)

        return make_mpgs

def main():
    # create an ArgumentParser object
    logging.debug('Creating parser object')
    parser = argparse.ArgumentParser(description="Analyze Auto MPG data set")

    # add commands and arguments
    parser.add_argument('command', help='command to execute', choices=['print', 'mpg_by_year', 'mpg_by_make'])
    parser.add_argument('-s', '--sort', help='sort order', choices=['year', 'mpg', 'default'])
    parser.add_argument('-o', '--ofile', help='output file name')
    parser.add_argument('-p', '--plot', help='create graphical output using matplotlib', action='store_true')

    logging.debug('Parsing CLI arguments')
    # parse the command-line arguments
    args = parser.parse_args()

    # create AutoMPGData object
    data = AutoMPGData()

    # sort the data based on the specified sort order, if provided
    if args.sort:
        if args.sort == 'year':
            logging.debug('Sorting by year')
            data.sort_by_year()
        elif args.sort == 'mpg':
            logging.debug('Sorting by mpg')
            data.sort_by_mpg()
        elif args.sort == 'default':
            logging.debug('Sorting by default')
            data.sort_by_default()


    # execute the commands
    if args.command == 'print':
        logging.debug('Printing autoMPG data objects')
        # execute the ofile command

        for auto in data:
            print(auto)

        # Write the output to a CSV file if ofile specified
        if args.ofile:
            with open(args.ofile, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Make', 'Model', 'Year', 'MPG'])
                for line in data:
                    writer.writerow([line.make, line.model, line.year, line.mpg])
            logging.debug(f'Creating file: {args.ofile}')
      
    elif args.command == 'mpg_by_year':
        # execute the mpg_by_year function
        year_mpg = data.mpg_by_year()
        year_mpg = sorted(year_mpg.items(), key=lambda x: x[0])
        logging.debug(f'Output mpg data by year')

        if args.ofile is None and args.plot is False:
            print(['Year', 'Avg MPG'])
            for line in year_mpg:
                    print([line[0],line[1]], file=sys.stdout)

        # Write the output to a CSV file or sys.stdout
        if args.ofile:
            with open(args.ofile, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Year', 'AvgMPG'])
                for line in year_mpg:
                    writer.writerow([line[0],line[1]])
            logging.debug(f'Creating file: {args.ofile}')


    elif args.command == 'mpg_by_make':
        # Execute the mpg_by_make function
        make_mpg = data.mpg_by_make()
        make_mpg = sorted(make_mpg.items(), key=lambda x: x[0])
        logging.debug(f'Output mpg data by make')

        if args.ofile is None and args.plot is False:
            print(['Make', 'Avg MPG'])
            for line in make_mpg:
                    print([line[0],line[1]], file=sys.stdout)

        # Write the output to a CSV file or sys.stdout
        if args.ofile:
            with open(args.ofile, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Make', 'AvgMPG'])
                for line in make_mpg:
                    writer.writerow([line[0],line[1]])
            logging.debug(f'Creating file: {args.ofile}')
            

    # execute the plot argument
    if args.plot:
        # inititialize the x and y values
        x = []
        y = []

        if args.command == 'mpg_by_year':
            logging.debug(f'Plotting {args.command}')
            # set x and y values
            year_mpg = data.mpg_by_year()
            for year, avg_mpg in year_mpg.items():
                x.append(year)
                y.append(avg_mpg)

            # create bar plot
            fig, ax = plt.subplots()

            ax.bar(x, y)

            plt.xlabel('Year')
            plt.ylabel('Average MPG')
            plt.title('Average MPG by Year')
            # remove splines for stylistic choice
            for x in ['top', 'right']:
                ax.spines[x].set_visible(False)

            plt.show()

        elif args.command == 'mpg_by_make':
            logging.debug(f'Plotting {args.command}')
            # set the x and y values
            make_mpg = data.mpg_by_make()
            make_mpg = sorted(make_mpg.items(), key=lambda x: x[0])
            for line in make_mpg:
                x.append(line[0])
                y.append(line[1])

            # create the bar plot    
            fig, ax = plt.subplots()
            
            ax.bar(x, y)

            plt.xlabel('Make')
            plt.ylabel('Average MPG')
            plt.title('Average MPG by Make')
            # rotate xticks since make names are long
            plt.xticks(rotation=90)

            # remove splines for stylistic choice
            for x in ['top', 'right']:
                ax.spines[x].set_visible(False)

            plt.show()
        

if __name__ == '__main__':
    main()