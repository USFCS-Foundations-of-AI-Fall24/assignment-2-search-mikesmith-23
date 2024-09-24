from collections import deque


## Breadth-First Search Implementation
def breadth_first_search(startState,
                         action_list,
                         goal_test_fn,
                         use_closed_list=True):
    """
    Implements Breadth-First Search with optional closed list.
    """
    search_queue = deque()
    closed_list = {}
    state_counter = 0  # Initialize state counter

    search_queue.append((startState, ""))
    if use_closed_list:
        closed_list[startState] = True

    while len(search_queue) > 0:
        next_state = search_queue.popleft()
        state_counter += 1  # Increment state counter

        print(f"Dequeued state #{state_counter}: {next_state[0]}")

        if goal_test_fn(next_state[0]):
            print(f"Goal found after generating {state_counter} states.")
            return next_state
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [
                    item for item in successors if item[0] not in closed_list
                ]
                for s in successors:
                    closed_list[s[0]] = True

            search_queue.extend(successors)

    print(f"Total number of states generated: {state_counter}")
    return None  # Return None if no solution found


## Depth-First Search Implementation
def depth_first_search(startState,
                       action_list,
                       goal_test_fn,
                       use_closed_list=True):
    """
    Implements Depth-First Search with optional closed list.
    """
    search_queue = deque()
    closed_list = {}
    state_counter = 0  # Initialize state counter

    search_queue.append((startState, ""))
    if use_closed_list:
        closed_list[startState] = True

    while len(search_queue) > 0:
        next_state = search_queue.pop()  # DFS uses stack (LIFO)
        state_counter += 1  # Increment state counter

        print(f"Dequeued state #{state_counter}: {next_state[0]}")

        if goal_test_fn(next_state[0]):
            print(f"Goal found after generating {state_counter} states.")
            return next_state
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [
                    item for item in successors if item[0] not in closed_list
                ]
                for s in successors:
                    closed_list[s[0]] = True

            search_queue.extend(successors)

    print(f"Total number of states generated: {state_counter}")
    return None


## Depth-Limited Search (w/ depth limit)
def depth_limited_search(startState,
                         action_list,
                         goal_test_fn,
                         use_closed_list=True,
                         limit=0):
    """
    Implements Depth-Limited Search up to a specified depth limit.
    """
    search_queue = deque()
    closed_list = {}
    state_counter = 0  # Initialize state counter

    search_queue.append((startState, "", 0))  # Track the current depth

    while len(search_queue) > 0:
        next_state, action, depth = search_queue.pop()
        state_counter += 1

        if depth > limit:
            continue  # Skip states that go past the specified depth limit

        print(f"Dequeued state #{state_counter}: {next_state}")

        if goal_test_fn(next_state):
            print(f"Goal found after generating {state_counter} states.")
            return next_state
        else:
            successors = next_state.successors(action_list)
            if use_closed_list:
                successors = [
                    item for item in successors if item[0] not in closed_list
                ]
                for s in successors:
                    closed_list[s[0]] = True

            search_queue.extend([(s[0], s[1], depth + 1) for s in successors])

    print(f"Total number of states generated: {state_counter}")
    return None
