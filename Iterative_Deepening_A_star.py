"""Iterative Deepening A* (IDA*) is a search algorithm that combines the advantages of both depth-first search (DFS) and A*
 by using iterative deepening to find the optimal solution while maintaining a low memory footprint. It works well for large 
 search spaces, making it suitable for problems like pathfinding in AI and puzzles."""

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)



#Implement a heuristic function that estimates the cost from the current node to the goal node.
def heuristic(node, goal):
    # For example, Manhattan distance in a grid
    return abs(node.state[0] - goal.state[0]) + abs(node.state[1] - goal.state[1])


#Implement the main logic for the IDA* algorithm, where the search is carried out iteratively with an increasing threshold for the estimated cost (f = g + h).
def ida_star(start, goal):
    def search(node, goal, threshold):
        f = node.cost + node.heuristic
        if f > threshold:
            return f  # return the new threshold
        if node.state == goal.state:
            return node  # goal found
        
        min_threshold = float('inf')
        for neighbor in get_neighbors(node):
            result = search(neighbor, goal, threshold)
            if isinstance(result, Node):  # Goal found
                return result
            if result < min_threshold:
                min_threshold = result
        
        return min_threshold

    threshold = start.cost + heuristic(start, goal)
    while True:
        result = search(start, goal, threshold)
        if isinstance(result, Node):
            return result  # Goal found
        if result == float('inf'):
            return None  # No solution
        threshold = result


#Testing the Implementation
import unittest
from ida_star import ida_star, Node

class TestIDAStar(unittest.TestCase):
    def test_pathfinding(self):
        start = Node((0, 0), cost=0, heuristic=0)
        goal = Node((3, 3), cost=0, heuristic=0)
        result = ida_star(start, goal)
        self.assertEqual(result.state, goal.state)

if __name__ == "__main__":
    unittest.main()


"""
the key aspects of IDA*:

Low memory usage compared to A*.
Optimal solutions when using an admissible heuristic.
Suitable for large search spaces where A* might run out of memory.
"""