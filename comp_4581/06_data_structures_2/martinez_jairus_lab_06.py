class MyHashtable:
    """
    Open addressing implementation of a hash table.
    Attributes:
        size (int) : desired size of the table.
        table (list) : initialized size of the table, containing keys or None
        status (list) : The status of each slot in the table ('empty', 'filled', 'deleted')
    Methods:
        hash : computes the hash value for a given key
        insert : inserts a key into the hash table using open addressing for collision resolution
        member : checks if a key is present in the hash table
        delete : deletes a key from the hash table
        __str__ : returns a string representation of the hash table
    """
    def __init__(self, size):
        """
        Initializes the hash table with the given size.
        Args:
            size (int): desired size of the hash table
        """
        self.size = size
        self.table = [None] * size
        # keeps slot status: ('empty', 'filled', 'deleted')
        self.status = ['empty'] * size  

    def hash(self, key):
        """
        Computes the hash value for a given key.
        Args:
            key (str): key that you want to hash
        Returns:
            int: hash value for the key
        """
        # gets the ASCII value of the first character of the key
        # and then computes hash with 'mod size'
        return ord(key[0]) % self.size

    def insert(self, key):
        """
        Inserts a key into the hash table using open addressing for collision resolution.
        Args:
            key (str): key to insert
        Returns:
            None
        """
        # store start index to keep track of full table loop
        start_i = self.hash(key)  

        # loop until we find an empty slot
        i = start_i
        while self.status[i] == 'filled':
            # increment over next slot
            i = (i + 1) % self.size 
            if i == start_i:  
                raise Exception("Hashtable is full")

        # insert the key into the found empty slot
        self.table[i] = key
        # update indec to be 'filled'
        self.status[i] = 'filled'

    def member(self, key):
        """
        Checks if a key is present in the hash table.
        Args:
            key (str): key to check
        Returns:
            bool: true if the key is found, false otherwise
        """
         # store start index to keep track of full table loop
        start_i = self.hash(key)

        # loop until we find the key or an empty slot
        i = start_i
        while self.status[i] != 'empty':
            # if slot filled key present = is member True
            if self.status[i] == 'filled' and self.table[i] == key:
                return True  
            # increment to next slot
            i = (i + 1) % self.size  
            # if back at start, key not in table
            if i == start_i:  
                return False
        # key not there :(
        return False 

    def delete(self, key):
        """
        Deletes a key from the hash table.
        Args:
            key (str): key to delete
        """
         # store start index to keep track of full table loop
        start_i = self.hash(key)

        # loop until we find the key or an empty slot
        i = start_i
        while self.status[i] != 'empty':
            # if slot filled key present = is member True
            if self.status[i] == 'filled' and self.table[i] == key:
                # if key present, delete it and mark as 'deleted'
                self.table[i] = None
                self.status[i] = 'deleted'
                return None
            # increment to next slot
            i = (i + 1) % self.size 
            # if back at start, key not in table return false and then do nothing
            if i == start_i: 
                return None

    def __str__(self):
        """
        String representation of the hash table.
        """
        return str(self.table)


if __name__ == '__main__':
    n = 10
    print(f'Create hastable with size {n}')
    s = MyHashtable(n)
    print(s)
    print("Insert 'amy'")
    s.insert("amy") #97
    print(s)
    print("Insert 'chase'")
    s.insert("chase") #99
    print(s)
    s.insert("chris") #99
    print('Is amy a member?')
    print(s.member("amy"))  # True
    print('Is chris a member?')
    print(s.member("chris"))  # True
    print('Is alyssa a member?')
    print(s.member("alyssa"))  # False
    print(s)
    print('Delete chase')
    s.delete("chase")
    print(s)
    print('Is chris a member?')
    print(s.member("chris"))  # True
    print(s)

# TERMINAL OUTPUT

# Create hastable with size 10
# [None, None, None, None, None, None, None, None, None, None]
# Insert 'amy'
# [None, None, None, None, None, None, None, 'amy', None, None]
# Insert 'chase'
# [None, None, None, None, None, None, None, 'amy', None, 'chase']
# Is amy a member?
# True
# Is chris a member?
# True
# Is alyssa a member?
# False
# ['chris', None, None, None, None, None, None, 'amy', None, 'chase']
# Delete chase
# ['chris', None, None, None, None, None, None, 'amy', None, None]
# Is chris a member?
# True
# ['chris', None, None, None, None, None, None, 'amy', None, None]