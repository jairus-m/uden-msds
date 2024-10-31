class MyStack(object):
    """Stack ADT with list implementation"""
    def __init__(self, element_type):
        """
        Initializes an empty stack of a specified element type.
        Args:
            elemType (type): type of data structure the stack will hold
        Returns:
            None
        """
        self.element_type = element_type
        self.state = []  
    
    def __str__(self):
        """
        Returns a string representation of the stack.
        Args:
            None
        Returns:
            str: string representation of the stack.
        """
        return str(self.state)
    
    def empty(self):
        """
        Checks if stack is empty.
        Args:
            None
        Returns:
            bool: true empty, false otherwise
        """
        return len(self.state) == 0
    
    def push(self, element):
        """
        Adds an element to the top of the stack.
        Args:
            element (element_type): element to be added to the stack.
        """
        # if element is the wrong type, raise error
        assert type(element) == self.element_type
        self.state.append(element)
    
    def pop(self):
        """
        Removes and returns the top element from the stack.
        Returns:
            element_type: element removed from the top of the stack
        """
        # raise error if stack has nothing
        if self.empty():
            raise ValueError("Empty stack!")
        else:
            return self.state.pop()
    
    def top(self):
        """
        Returns the top element from the stack.
        Returns:
            elemType: The element at the top of the stack.
        """
        # raise error if stack has nothing
        if self.empty():
            raise ValueError("Empty stack!")
        else:
            return self.state[-1]


def is_feasible(graph, current_state, node, color):
    """
    Checks if assigning a particular color to a node is feasible given the current state.
    Args:
        graph (list): adjacency matrix of the graph - boolean
        current_state (list): current color assignments for nodes - str
        node (int): node to check
        color (str): color to be assigned to the node
    Returns:
        bool: true if the color assignment is feasible, false otherwise
    """
    for adj_node in range(len(graph)):
        # if edge between nodes
        if graph[node][adj_node]:  
            if adj_node < len(current_state) and current_state[adj_node] == color:
                return False
    return True


def graphColoring(graph, colors):
    """
    Solves the graph coloring problem using backtracking 
    and an explicit stack similar to lab example.
    Args:
        graph (list): The adjacency matrix of the graph - bool
        colors (list): The list of available colors - str
    Returns:
        list: A valid color assignment for the graph, where each index represents 
                a node and the value at that index represents the assigned color - str
    """
    # Note: this is modeled off the lab 10/lecture nQueens code
    # Number of nodes in the graph
    n = len(graph)  
    initial_state = []  # Initial empty state
    
    s = MyStack(list)  # For a depth-first search
    s.push(initial_state)  # Push the initial state onto the Stack
    
    while not s.empty():
        current_state = s.pop()  # Grab the next state
        current_node = len(current_state)
        
        # See if we found a solved state at a leaf node
        if current_node == n:
            print(current_state)  # Display the solution
            return  # Stop after finding the first solution
        
        else:
            # Produce the state's children (if they are feasible)
            for color in reversed(colors):
                if is_feasible(graph, current_state, current_node, color):
                    # Create child by making a copy and appending new color
                    child_state = current_state.copy()
                    child_state.append(color)
                    s.push(child_state)  # Push child onto the stack

if __name__ == '__main__':
    # LAB 10 Example 
    graph = [
        [False, True,  False, False, False, True ],
        [True,  False, True,  False, False, True ],
        [False, True,  False, True,  True,  False],
        [False, False, True,  False, True,  False],
        [False, False, True,  True,  False, True ],
        [True, True,  False, False, True,  False]
    ]

    colors = ['r', 'g', 'b']

    graphColoring(graph, colors)    # EXPECT : ['r', 'g', 'r', 'b', 'g', 'b']

# TERMINAL OUTPUT
# ['r', 'g', 'r', 'b', 'g', 'b']