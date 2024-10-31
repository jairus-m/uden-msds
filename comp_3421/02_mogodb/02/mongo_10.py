import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()

db = client.db_temp
school = db.schoolData  

# Q1: All employees grouped by state and the number of employees in that state
print('Q1: All employees grouped by state and the number of employees in that state')
pipe = [{"$group": {"_id": "$state","count": {"$sum": 1}}}]

result = school.aggregate(pipe)

for data in result:
    print(data)
print('\n')

# Q2: Average age of people in each state, grouped by state
print('Q2: Average age of people in each state, grouped by state')
pipe = [{"$group": {"_id": "$state","averageAge": {"$avg": "$age"}}}]

result = school.aggregate(pipe)
for data in result:
    print(data)
print('\n')

# Q3: Average age in each state, grouped by state, sorted by state
print('Q3: Average age in each state, grouped by state, sorted by state')
pipe = [{"$group": {"_id": "$state","averageAge": {"$avg": "$age"}}},
        {"$sort": {"_id": 1}}]

result = school.aggregate(pipe)
for data in result:
    print(data)
print('\n')

# Q4: Number of people and average age of people in each manager's group, grouped by and sorted by manager id
print("Q4: Number of people and average age of people in each manager's group, grouped by and sorted by manager id")
pipe = [{"$group": {"_id": "$managerId","count": {"$sum": 1},"averageAge": {"$avg": "$age"}}},
        {"$sort": {"_id": 1}}]
result = school.aggregate(pipe)
for data in result:
    print(data)
print('\n')

# Q5: Average age and number of employees in each manager group, where the employees are all born after 1990
print('Q5: Average age and number of employees in each manager group, where the employees are all born after 1990')
pipe = [{"$match": {"birth": {"$gt": 1990}}},
        {"$group": {"_id": "$managerId","count": {"$sum": 1}, "averageAge": {"$avg": "$age"}}},
        {"$sort": {"_id": 1}}]
result = school.aggregate(pipe)
for data in result:
    print(data)