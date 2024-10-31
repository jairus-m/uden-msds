import csv
import os

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
    """
    def __init__(self):
        """
        Constructor with no args. Calls _load_data() method
        and initializes self.data list.
        """
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
            self._clean_data()

        data = []
        # read clean data and parse out relevant fields
        with open('auto-mpg.clean.txt', 'r') as f:
            next(f)
            for line in f:
                make, model, year, mpg = tuple(line.split('\t'))
                year = int(year)
                mpg = float(mpg)

                # create AutoMPG object from field values and append to self.data
                auto = AutoMPG(make, model, year, mpg)
                self.data.append(auto)

    def _clean_data(self):
        """
        Reads orignal txt data file and creates new, cleaned txt file (auto-mpg.clean.txt)
        """
        # instantiate the headers of the relevant fields as a tuple in the data list object
        data = [('Make', 'Model', 'Year', 'MPG')]
        with open('auto-mpg.data.txt', 'r') as file:
            csv_reader = csv.reader(file, delimiter=' ')
            for line in csv_reader:
                # filter out all spaces
                line = [x for x in line if x != '']

                # pack relevant field data into variables and append as tuple to data list
                make, model, year, mpg = ' '.join(line[7:]).split()[1].strip('"').title(), ' '.join(line[8:]).strip('"').title(), '19' + line[6], line[0]
                data.append((make, model, year, mpg))

        # write data file to txt file (delimiited by tabs with \t)      
        with open('auto-mpg.clean.txt', 'w') as f:
            for line in data:
                line = '\t'.join(map(str, line)) + '\n'
                f.write(line)

def main():
    # instantiate AutoMPGData class
    auto = AutoMPGData()
    for a in auto:
        print(a)

if __name__ == '__main__':
    main()