import csv

data = [('Name','Symbol','Atomic Number'),
        ('Hydrogen','H', 1),
        ('Helium','He', 2),
        ('Lithium','Li', 3),
        ('Beryllium','Be', 4),
        ('Boron','B', 5),
        ('Carbon','C', 6),
        ('Nitrogen','N', 7),
        ('Oxygen','O', 8)]

with open('elements.csv', 'w', newline='') as f:
    csvwrtier = csv.writer(f)
    csvwrtier.writerows(data)