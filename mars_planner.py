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

    def __init__(self,
                 loc="station",
                 sample_extracted=False,
                 holding_sample=False,
                 charged=False,
                 holding_tool=False):
        self.loc = loc
        self.sample_extracted = sample_extracted
        self.holding_sample = holding_sample
        self.charged = charged
        self.holding_tool = holding_tool
        self.prev = None

    def __eq__(self, other):
        return (self.loc == other.loc
                and self.sample_extracted == other.sample_extracted
                and self.holding_sample == other.holding_sample
                and self.charged == other.charged
                and self.holding_tool == other.holding_tool)

    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n" +
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}\n" +
                f"Holding Tool?: {self.holding_tool}")

    def __hash__(self):
        return hash(
            (self.loc, self.sample_extracted, self.holding_sample,
             self.charged, self.holding_tool))

    def successors(self, list_of_actions):
        succ = [(item(self), item.__name__) for item in list_of_actions]
        succ = [item for item in succ if not item[0] == self]
        return succ


def use_tool(state):
    r2 = deepcopy(state)
    if state.holding_tool and state.loc == "sample" and not state.sample_extracted:
        r2.sample_extracted = True
    r2.prev = state
    return r2


action_list.append(use_tool)


if __name__ == "__main__":
    s = RoverState()
    print("Initial State:", s)

    # BFS
    result = breadth_first_search(s, action_list, mission_complete)
    print("BFS Search result:", result)

    # DFS
    result = depth_first_search(s, action_list, mission_complete)
    print("DFS Search result:", result)

    # Depth-Limited Search
    result = depth_limited_search(s, action_list, mission_complete, limit=6)
    print("DLS Search result:", result)
