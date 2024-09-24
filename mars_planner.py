## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search, depth_limited_search


class RoverState:

    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, charged=False, holding_tool=False):
        self.loc = loc
        self.sample_extracted = sample_extracted
        self.holding_sample = holding_sample
        self.charged = charged
        self.holding_tool = holding_tool  # New variable for holding the tool
        self.prev = None

    def __eq__(self, other):
        return (self.loc == other.loc
                and self.sample_extracted == other.sample_extracted
                and self.holding_sample == other.holding_sample
                and self.charged == other.charged
                and self.holding_tool == other.holding_tool)  # Include holding_tool in equality check

    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n" +
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}\n" +
                f"Holding Tool?: {self.holding_tool}")  # Include holding_tool in representation

    def __hash__(self):
        return hash((self.loc, self.sample_extracted, self.holding_sample, self.charged, self.holding_tool))  # Include holding_tool in hash

    def successors(self, list_of_actions):
        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect
        succ = [item for item in succ if not item[0] == self]
        return succ


## Action functions

def move_to_sample(state):
    r2 = deepcopy(state)
    if state.loc != "sample":  # Ensure we are actually moving to a new location
        r2.loc = "sample"
        r2.prev = state
    return r2


def move_to_station(state):
    r2 = deepcopy(state)
    if state.loc != "station":  # Ensure we are actually moving to a new location
        r2.loc = "station"
        r2.prev = state
    return r2


def move_to_battery(state):
    r2 = deepcopy(state)
    if state.loc != "battery":  # Ensure we are actually moving to a new location
        r2.loc = "battery"
        r2.prev = state
    return r2


def pick_up_sample(state):
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample" and not state.holding_sample:
        r2.holding_sample = True
        r2.prev = state
    return r2


def drop_sample(state):
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station" and state.holding_sample:
        r2.holding_sample = False
        r2.prev = state
    return r2


def charge(state):
    r2 = deepcopy(state)
    if state.loc == "battery" and not state.charged:
        r2.charged = True
        r2.prev = state
    return r2


def extract_sample(state):
    r2 = deepcopy(state)
    if state.loc == "sample" and not state.sample_extracted:
        r2.sample_extracted = True
        r2.prev = state
    return r2


# New tool-related actions
def pick_up_tool(state):
    r2 = deepcopy(state)
    if state.loc == "station" and not state.holding_tool:  # Assuming the tool is at the station
        r2.holding_tool = True
        r2.prev = state
    return r2

def drop_tool(state):
    r2 = deepcopy(state)
    if state.loc == "station" and state.holding_tool:
        r2.holding_tool = False
        r2.prev = state
    return r2

def use_tool(state):
    r2 = deepcopy(state)
    if state.holding_tool and state.loc == "sample" and not state.sample_extracted:
        r2.sample_extracted = True
        r2.prev = state
    return r2


action_list = [
    charge, drop_sample, pick_up_sample, move_to_sample, move_to_battery,
    move_to_station, extract_sample, pick_up_tool, drop_tool, use_tool
]


## Goal check functions
def battery_goal(state):
    return state.loc == "battery"


def charge_goal(state):
    return state.charged


def sample_goal(state):
    return state.sample_extracted and not state.holding_sample


# True if we are at the battery, charged, and the sample is at the station.
# False otherwise.
def mission_complete(state):
    print(f"Checking goal state: {state}")
    return battery_goal(state) and charge_goal(state) and sample_goal(state)


if __name__ == "__main__":
    s = RoverState()  # Start with an initial state
    print("Initial State:", s)

    # Perform BFS
    result = breadth_first_search(s, action_list, mission_complete)
    if result:
        print("BFS Search result:", result)
    else:
        print("No solution found with BFS.")

    # Perform DFS
    result = depth_first_search(s, action_list, mission_complete)
    if result:
        print("DFS Search result:", result)
    else:
        print("No solution found with DFS.")

    # Perform Depth-Limited Search with a depth limit of 5
    result = depth_limited_search(s, action_list, mission_complete, limit=5)
    if result:
        print("Depth-Limited Search result:", result)
    else:
        print("No solution found with Depth-Limited Search.")
