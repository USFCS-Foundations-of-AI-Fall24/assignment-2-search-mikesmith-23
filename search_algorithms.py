from collections import deque

## Breadth-First Search with state counting
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True):
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

        if goal_test(next_state[0]):
            print(f"Goal found after generating {state_counter} states.")
            return next_state
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True

            search_queue.extend(successors)

    print(f"Total number of states generated: {state_counter}")
    return None

## Depth-First Search with state counting
def depth_first_search(startState, action_list, goal_test, use_closed_list=True):
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

        if goal_test(next_state[0]):
            print(f"Goal found after generating {state_counter} states.")
            return next_state
        else:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True

            search_queue.extend(successors)

    print(f"Total number of states generated: {state_counter}")
    return None
