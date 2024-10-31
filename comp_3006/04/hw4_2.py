from collections import deque

# instantiate deque and add 6 actors
actors = deque()

# add 6 actors:
movieStars = ['Ewan McGregor', 'Mark Hamil', 'Natalie Portman', 'Samuel L. Jackson', 'Oscar Isaac', 'Felicity Jones']
for actor in movieStars:
    actors.append(actor)

print('Add 6 movie stars to deque():')
print(f'\t{actors}')

# insert actor in the middle
actors.insert(round(len(actors)/2), 'Hayden Christensen')

# insert actor at the head/left end
actors.appendleft('Carrie Fisher')

# insert actor at tail/right end:
actors.append('Diego Luna')

print('Add H. Christensen to the middle, D. Luna to the end, and C. Fisher at the beginning:')
print(f'\t{actors}')

# remove two of the original names
actors.remove('Mark Hamil')
actors.remove('Natalie Portman')

print('Remove two of the orignal actors, H. Hamill and N. Portman:')
print(f'\t{actors}')

# remove Carrie Fischer which is at the head/left end
actors.popleft()

# remove Diego Luna who is at the tail/right end
actors.pop()

print('Use popleft() to remove C. Fischer from head and use pop() to remove D. Luna fron tail.')
print(f'\t{actors}')
