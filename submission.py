from mars_planner import RoverState, mission_complete, action_list
from search_algorithms import breadth_first_search, depth_first_search, depth_limited_search
from routefinder import a_star, read_mars_graph, sld, map_state
from antenna import solve_antenna_frequencies


def question_2_rover_planning():
    """
    Solves the Mars Rover problem using different search algorithms.
    """
    print("\n" + "=" * 50)
    print("Question 2: Mars Rover Planning")
    print("=" * 50)

    # Initial state for the rover planning problem
    initial_state = RoverState(loc="station",
                               sample_extracted=False,
                               holding_sample=False,
                               charged=True,
                               holding_tool=False)

    print("\nRunning Breadth First Search...\n")
    bfs_result = breadth_first_search(initial_state, action_list,
                                      mission_complete)
    print(f"\nBFS Result:\n{bfs_result}")

    print("\nRunning Depth First Search...\n")
    dfs_result = depth_first_search(initial_state, action_list,
                                    mission_complete)
    print(f"\nDFS Result:\n{dfs_result}")

    print("\nRunning Depth-Limited Search (limit=6)...\n")
    dls_result = depth_limited_search(initial_state,
                                      action_list,
                                      mission_complete,
                                      limit=6)
    print(f"\nDLS Result:\n{dls_result}")


def is_goal(state):
    """Goal test for A* search in question 3"""
    return state.is_goal()


def heuristic_zero(state):
    """Heuristic function that always returns 0 for UCS"""
    return 0


def question_3_a_star_search():
    """
    Solves the Mars pathfinding problem using A* and UCS (with heuristic h=0).
    """
    print("\n" + "=" * 50)
    print("Question 3: A* Search on Mars")
    print("=" * 50)

    # Reading the Mars graph
    mars_graph = read_mars_graph("marsmap.txt")

    # Define start and goal nodes
    start = map_state(location="3,7",
                      mars_graph=mars_graph)  # Set the actual start state

    # Run A* with straight-line distance heuristic
    print("\nRunning A* Search...\n")
    a_star_result = a_star(start, sld, is_goal)
    print(f"\nA* Result:\n{a_star_result}")

    # Run UCS (A* with h=0)
    print("\nRunning Uniform Cost Search (UCS)...\n")
    ucs_result = a_star(start, heuristic_zero,
                        is_goal)  # Use the heuristic_zero function for UCS
    print(f"\nUCS Result:\n{ucs_result}")


def question_4_antenna_constraints():
    """
        Solves the antenna frequency assignment problem using OR-Tools.
        """
    print("\n" + "=" * 50)
    print("Question 4: Antenna Frequency Assignment")
    print("=" * 50)

    # Solve the antenna frequency problem
    antenna_solution = solve_antenna_frequencies()

    # Display the antenna frequencies in a clean, table-like format
    print("\nAntenna Frequency Assignment Solution:")
    print(f"{'Antenna':<10} {'Frequency':<10}")
    print("-" * 20)
    for antenna, frequency in antenna_solution.items():
        print(f"{antenna:<10} {frequency:<10}")


if __name__ == "__main__":
    # Run Question 2 (Rover Planning)
    question_2_rover_planning()

    # Run Question 3 (A* Search)
    question_3_a_star_search()

    # Run Question 4 (Antenna Frequency Assignment)
    question_4_antenna_constraints()
