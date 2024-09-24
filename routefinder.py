from queue import PriorityQueue
from Graph import Graph, Edge
import math

class map_state:

    def __init__(self, location="", mars_graph=None, prev_state=None, g=0, h=0):
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

def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((start_state.f, start_state))

    state_counter = 0

    while not search_queue.empty():
        _, current_state = search_queue.get()
        state_counter += 1
        print(f"Processing state #{state_counter}: {current_state}")

        if goal_test(current_state):
            print(f"Goal found after generating {state_counter} states.")
            return current_state

        if use_closed_list:
            closed_list[current_state] = True

        for neighbor_state, action in current_state.successors():
            neighbor_state.h = heuristic_fn(neighbor_state)
            neighbor_state.f = neighbor_state.g + neighbor_state.h

            if use_closed_list and neighbor_state in closed_list:
                continue

            search_queue.put((neighbor_state.f, neighbor_state))

    print(f"Total number of states generated: {state_counter}")
    return None

# Default heuristic for UCS
def h1(state):
    return 0

# Basic straight-line distance heuristic
def sld(state):
    current_x, current_y = map(int, state.location.split(','))
    goal_x, goal_y = 1, 1
    return math.sqrt((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2)

# Placeholder for reading graph
def read_mars_graph(filename):
    pass
