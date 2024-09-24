from queue import PriorityQueue
from Graph import Graph, Edge
import math


class map_state:

    def __init__(self,
                 location="",
                 mars_graph=None,
                 prev_state=None,
                 g=0,
                 h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def is_goal(self):
        return self.location == '1,1'

    def successors(self):
        # Retrieve all edges (or neighbors) from the graph's curr. loc.
        neighbors = self.mars_graph.get_edges(self.location)
        successor_states = []

        for edge in neighbors:
            # Create a new map_state for each neighbor with updated g cost
            neighbor_state = map_state(location=edge.dest,
                                       mars_graph=self.mars_graph,
                                       prev_state=self,
                                       g=self.g + edge.val)
            successor_states.append((neighbor_state, "move"))

        return successor_states


# A* Search Implementation
def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(
        (start_state.f, start_state))  # Push the start state with its f value

    state_counter = 0  # To count generated states

    while not search_queue.empty():
        _, current_state = search_queue.get(
        )  # Get the state with the lowest f value
        state_counter += 1
        print(f"Processing state #{state_counter}: {current_state}")

        if goal_test(current_state):  # Check if the goal is reached
            print(f"Goal found after generating {state_counter} states.")
            return current_state

        if use_closed_list:
            closed_list[current_state] = True

        # Expand neighbors (successors)
        for neighbor_state, action in current_state.successors():
            neighbor_state.h = heuristic_fn(
                neighbor_state)  # Update the heuristic (h value)
            neighbor_state.f = neighbor_state.g + neighbor_state.h  # Recalculate f = g + h

            if use_closed_list and neighbor_state in closed_list:
                continue

            search_queue.put(
                (neighbor_state.f, neighbor_state))  # Add to queue

    print(f"Total number of states generated: {state_counter}")
    return None


# Default heuristic for uniform cost search (h = 0 for all states)
def h1(state):
    return 0


# Heuristic function - Straight Line Distance to the goal (1,1)
def sld(state):
    current_x, current_y = map(int, state.location.split(','))
    goal_x, goal_y = 1, 1  # The goal is at (1,1)
    return math.sqrt((current_x - goal_x)**2 + (current_y - goal_y)**2)


# Read Mars graph from file
def read_mars_graph(filename):
    mars_graph = Graph()

    # Open the file and read each line
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Split the line into the node and its neighbors
        node_info = line.strip().split(':')
        node = node_info[0].strip()  # The node (e.g., "1,1")
        neighbors = node_info[1].strip().split(
        )  # The neighbors (ex., ["2,1", "1,2"])

        # Add the node to the graph
        mars_graph.add_node(node)

        # Add edges to the neighbors
        for neighbor in neighbors:
            mars_graph.add_edge(Edge(node, neighbor,
                                     1))  # Assume uniform cost (val=1)

    return mars_graph


if __name__ == "__main__":
    mars_map = read_mars_graph("marsmap.txt")
    start_state = map_state(location="3,7",
                            mars_graph=mars_map)  # Set the start point
    goal_test = lambda state: state.is_goal()

    # Call a_star search
    result = a_star(start_state, sld, goal_test)
    print(result)
