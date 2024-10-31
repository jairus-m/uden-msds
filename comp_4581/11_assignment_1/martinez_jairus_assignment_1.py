def loadGraph(filename: str):
    """
    Reads in edge data and returns an adjacency 
    list that corresponds to the undirected graph 
    of social connections.
    Args:
        filename (str) : name of Facebook edge file
    Returns:
        dict : adjacency list representation
    """
    adjacency_list = {}
    
    with open(filename, 'r') as file:
        for line in file:
            vertex1, vertex2 = map(int, line.split())
            
            # initialize empty list for vertices if not already in the graph
            if vertex1 not in adjacency_list:
                adjacency_list[vertex1] = []
            if vertex2 not in adjacency_list:
                adjacency_list[vertex2] = []
            
            # adds corresponding vertices to list if on the same line
            # do it for both directions so "undirected"
            adjacency_list[vertex1].append(vertex2)
            adjacency_list[vertex2].append(vertex1)
    
    return adjacency_list

class MyQueue:
    """
    Class for queue data structure.
    Taken from lab 05.
    Attributes:
        queue : queue data structure
    Methods:
        enqueue: adding an object to the tail
        dequeue: removing an object from the head
        empty: true if queue is empty
    """
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)
    
    def front(self):
        if self.empty():
            raise IndexError("front from empty queue")
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        """String representation of queue"""
        return str(self.queue)
    
def BFS(G, s):
    """
    Runs breadth-first-search to return the distance
    between the source vertext, s, to all other vertices, V.
    Args:
        G (dict) : adjacency list (graph)
        s (int) : source vertex index
    Returns:
        dict : key-value pair where key is the vertex (v) and 
                value is the distance between s and itself
    """
    queue = MyQueue()
    queue.enqueue(s)
    
    distances = {}
    for vertex in G:
        distances[vertex] = float('inf')
    distances[s] = 0
    
    while not queue.empty():
        current = queue.dequeue()
        
        for neighbor in G[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.enqueue(neighbor)
    
    return distances

def distanceDistribution(G):
    """
    Calculates and returns the distribution of all 
    distance frequencies between the vertices.
    Args:
        G (dict) : adjacency list graph representation
    Returns:
        dict : distribution of distances (key = distance, value = frequency in %)
    """
    distribution = {}
    
    # for every vertex, compute the distance to every other vertices
    for vertex in G:
        distances = BFS(G, vertex)
        for dist in distances.values():
            if dist != 0:  # dont count 0 distance to self
                # increment the counter within distribution dict
                if dist in distribution:
                    distribution[dist] += 1
                else:
                    distribution[dist] = 1
    
    # convert frequencies to percentages
     # ALL pairs excluding loops to self
    total_pairs = len(G) * (len(G) - 1) 
    
    for dist in distribution:
        distribution[dist] = (distribution[dist] / total_pairs) * 100
    
    return distribution

if __name__ == "__main__":
    # Step 1: Load graph from edge file
    filename = 'edges.txt'
    graph = loadGraph(filename)
    
    # Step 2: Compute distance distribution
    distribution = distanceDistribution(graph)
    
    # Step 3: Print the final distribution dictionary
    print("Distance Distribution:")
    for dist, percent in distribution.items():
        print(f"Distance {dist}: {percent:.2f}%")


# PART 1: TERMINAL OUTPUT

# Distance Distribution:
# Distance 1: 1.08%
# Distance 4: 35.94%
# Distance 2: 16.65%
# Distance 3: 24.41%
# Distance 6: 4.15%
# Distance 5: 15.73%
# Distance 7: 1.93%
# Distance 8: 0.10%

# PART 2: TO WHAT EXTEND DOES THIS NETWORK SATISFY THE SMALL WORLD PHENOMENON?

# This network exhibits characteristics of the small world phenomenon with a majority of "nodes" being connected within 3 and 6 "steps".
#   - Nearly 98% of people are connected by at most 6 aquaintances
#   - Nearly 42% of people are connected by at most 3 aquaitances

# Since nearly 98% of social connections between people can be done through 6 or less aquaitances, 
# the network given in 'edges.txt' strongly statisfied the small world phenomenon.
 
# PART 3: OPTIONAL
# EFFICIENTY UPDATING DISTANCE DISTRIBUTION
# 1. Calcuate existing distribution (via BFS) of distance counts of edge data
# 2. Store the counts of the distances
# 3. Add new vertext with new edge data/nodes
# 4. Calcuate the distance distribution via BFS for that new vertext only
# 5. Append the distance counts to the appropriate distances of the oringal, stored distribution
# 6. Simply recalcualte the distirbution after adding the new distance counts