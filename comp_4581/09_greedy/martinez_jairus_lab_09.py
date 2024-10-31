def extractMin(verts):
    """
    Extracts the vertex with the minimum priority (distance) from the list.
    Args:
        verts (list): list of vertices [vertex, current minimum distance].
    Returns:
        list: vertex with the minimum distance (is removed from the original list)
    """
    minIndex = 0
    for v in range(1, len(verts)):
        if verts[v][1] < verts[minIndex][1]:
            minIndex = v
    return verts.pop(minIndex)

def mst(graph):
    """
    Implements Prim's Minimum Spanning Tree (MST) algorithm.

    Prim's algorithm constructs the MST by starting with an arbitrary vertex and
    adding the shortest edge connecting a vertex in the tree to a vertex outside the tree.
    Args:
        graph (list): A 2D adjacency matrix representing the graph 
            - graph[i][j] indicates the weight of the edge between vertex i and vertex j
            - a value of 0 indicates no edge between the vertices.
    Returns:
        list: list of edges representing the MST; each edge is represented as [vertex, parent_vertex]
            - `parent_vertex` is the vertex connected to `vertex` in the MST
    """
    nVerts = len(graph)
    
    # list of vertices  [vertex, current min edge weight]
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]
    
    # list to store the MST edges [current_vertex, previous_vertex]
    # starting point: vertex = 0 and parent = none (-1)
    mstEdges = [[0, -1]]  
    
    # starting vertex (0) w/ no cost
    vertsToProcess[0][1] = 0  
    
    while len(vertsToProcess) > 0:
        # extract vertex with the min edge weight
        u = extractMin(vertsToProcess)
        currentVertex = u[0]
        
        # process neighbors of the extracted vertex
        for v in vertsToProcess:
            neighborVertex = v[0]
            weight = graph[currentVertex][neighborVertex]
            
            # if no edge and edge weight < current known weight
            if weight > 0 and weight < v[1]:
                v[1] = weight
                # upd edge that connects to MST
                mstEdges.append([neighborVertex, currentVertex])
    
    return mstEdges


if __name__ == '__main__':
    graph = [[0, 7, 0, 0, 0, 10, 15, 0],
            [7, 0, 12, 5, 0, 0, 0, 9],
            [0, 12, 0, 6, 0, 0, 0, 0],
            [0, 5, 6, 0, 14, 8, 0, 0],
            [0, 0, 0, 14, 0, 3, 0, 0],
            [10, 0, 0, 8, 3, 0, 0, 0],
            [15, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0]]

    mst_edges = mst(graph)
    print(mst_edges)

# TERMINAL OUTPUT
# [[0, -1], [1, 0], [5, 0], [6, 0], [2, 1], [3, 1], [7, 1], [2, 3], [4, 3], [5, 3], [4, 5]]