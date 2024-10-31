import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()

# for cursor in client.list_databases():
#     print(cursor)
# print('\n')

db = client.db_people
peeps = db.thePeople  

print('Part 1: Queries')
print('\n')

# Q1: Complete info about people who have 7 children
print('Q1: Complete info about people who have 7 children')
query = {"numChildren": 7}
result = peeps.find(query)

for person in result:
    print(person)
print('\n')

# Q2: pid, state, and name of the children for people who have 7 children
print('Q2: pid, state, and name of the children for people who have 7 children')
query = {"numChildren": 7}
projection = {"pid": 1, "state": 1, "children": 1}
result = peeps.find(query, projection)

for person in result:
    print(person)
print('\n')

# Q3: Complete info of people who live in CA and have 6 children
print('Q3: Complete info of people who live in CA and have 6 children')
query = {"state": "CA", "numChildren": 6}
result = peeps.find(query)

for person in result:
    print(person)
print('\n')

# Q4: Complete info of people who live in CA and have 6 or 7 children
print('Q4: Complete info of people who live in CA and have 6 or 7 children')
query = {"state": "CA", "numChildren": {"$in": [6, 7]}}
result = peeps.find(query)

for person in result:
    print(person)
print('\n')

# Q5: List the pid and children names for all people who have a child whose name contains 'Bob A' => hint - use $regex
print('Q5: List the pid and children names for all people who have a child whose name contains "Bob A"')
query = {"children": {"$regex": "Bob A"}}
projection = {"pid": 1, "children.name": 1}
result = peeps.find(query, projection)

for person in result:
    print(person)
print('\n')

# Q6: Aggregation 5: number of people who have 0, 1, ... 8 children
print('Q6: Aggregation: number of people who have 0, 1, ... 8 children')
pipeline = [
    {"$group": {"_id": "$numChildren", "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
]

result = peeps.aggregate(pipeline)

for person in result:
    print(person)
print('\n')

# Q7: Aggregation: average salary for each state:
print('Q7: Aggregation: average salary for each state')
pipeline = [
    {"$group": {"_id": "$state", "average_salary": {"$avg": "$salary"}, "numInGroup": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
]

result = peeps.aggregate(pipeline)

for person in result:
    print(person)
print('\n')

# Q8: Aggregation: average salary and count for people living in WI state
print('Q8: Aggregation: average salary and count for people living in WI state')
pipeline = [
    {"$match": {"state": "WI"}},  # Filter only documents for WI state
    {"$group": {"_id": "$state", "average_salary": {"$avg": "$salary"}, "numInGroup": {"$sum": 1}}}
]

result = peeps.aggregate(pipeline)

for person in result:
    print(person)
print('\n')

# Q9: Aggregation: average, min, and max salary for Midwest states
midwest_states = ["IL", "IN", "IA", "KS", "MI", "MN", "MO", "NE", "ND", "OH", "SD", "WI"]

print('Q9: Aggregation: average, min, and max salary for Midwest states')
pipeline = [
    {"$match": {"state": {"$in": midwest_states}}},  
    {"$group": {"_id": "$state", 
                "avgSalary": {"$avg": "$salary"}, 
                "minSalary": {"$min": "$salary"}, 
                "maxSalary": {"$max": "$salary"},
                "numInGroup": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
]

result = peeps.aggregate(pipeline)

for person in result:
    print(person)
print('\n')

# Q10: Aggregation: average salary and count for states with average salary >= 82,000
print('Q10: Aggregation: average salary and count for states with average salary >= 82,000')
pipeline = [
    {"$group": {"_id": "$state", 
                "average_salary": {"$avg": "$salary"}, 
                "numInGroup": {"$sum": 1}}},
    {"$match": {"average_salary": {"$gte": 82000}}},
    {"$sort": {"_id": 1}}
]

result = peeps.aggregate(pipeline)

for person in result:
    print(person)
print('\n')

# Q11: Aggregation: average, min, and max salary for Midwest states wi
midwest_states = ["IL", "IN", "IA", "KS", "MI", "MN", "MO", "NE", "ND", "OH", "SD", "WI"]

print('Q11: Aggregation: average, min, and max salary for Midwest states with average salary > 82,000')
pipeline = [
    {"$match": {"state": {"$in": midwest_states}}}, 
    {"$group": {"_id": "$state", 
                "avgSalary": {"$avg": "$salary"}, 
                "minSalary": {"$min": "$salary"}, 
                "maxSalary": {"$max": "$salary"},
                "numInGroup": {"$sum": 1}}},
    {"$match": {"avgSalary": {"$gt": 82000}}},
    {"$sort": {"_id": 1}}
]

result = peeps.aggregate(pipeline)

for person in result:
    print(person)
print('\n')

print('Part 2: Updates/Deletes')
print('\n')

print('1. Update one document (pid = 1 will have have new salary of $90k):')
# before
print('\nBefore:\n')
result = peeps.find_one({"pid": 1})
print("Document Before Update:")
print(result)

# update one line
print('\n')
query = {"pid": 1}
update = {"$set": {"salary": 90000}}  # Update the salary field to 90,000
peeps.update_one(query, update)

# after
print('After:')
new_result = peeps.find_one({"pid": 1})
print("\nDocument After Update:")
print(new_result)

print('\n2. Update multiple documents (all states = CA will have new salaries of $95k):')
# before
print('\nBefore:\n')
query = {"state": "CA"}
result = peeps.find(query)
print("Documents Before Update:")
for document in result[:5]:
    print(document)

# update multiple documents (all states = CA)
print('\n')
query = {"state": "CA"}
update = {"$set": {"salary": 95000}}  # Update the salary field to 95,000 for all documents in CA
peeps.update_many(query, update)

# after
print('After:')
query = {"state": "CA"}
new_result = peeps.find(query)
print("\nDocuments After Update:")
for document in new_result[:5]:
    print(document)
print('\n')

print('3. Delete all documents where the state is "CA:')
# before
print('\nBefore:\n')
query = {"state": "CA"}
result = peeps.find(query)  
print("Documents Before Deletion:")
for document in result[:5]:
    print(document)

# delete all documents where the state is "CA"
query = {"state": "CA"}
result = peeps.delete_many(query)

print("\nNumber of Documents Deleted:", result.deleted_count)

# Print a subset of documents after the deletion
print('\nAfter:')
query = {"state": "CA"}
print(f"Documents After Deletion: {peeps.count_documents(query)}")