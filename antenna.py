from ortools.sat.python import cp_model


def solve_antenna_frequencies():
    # Instantiate model and solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    # Frequencies: 0 -> f1, 1 -> f2, 2 -> f3
    frequencies = {0: 'f1', 1: 'f2', 2: 'f3'}

    Antenna1 = model.NewIntVar(0, 2, "A1")
    Antenna2 = model.NewIntVar(0, 2, "A2")
    Antenna3 = model.NewIntVar(0, 2, "A3")
    Antenna4 = model.NewIntVar(0, 2, "A4")
    Antenna5 = model.NewIntVar(0, 2, "A5")
    Antenna6 = model.NewIntVar(0, 2, "A6")
    Antenna7 = model.NewIntVar(0, 2, "A7")
    Antenna8 = model.NewIntVar(0, 2, "A8")
    Antenna9 = model.NewIntVar(0, 2, "A9")

    # Add edges (adjacent antennas cannot share the same frequency)
    model.Add(Antenna1 != Antenna2)
    model.Add(Antenna1 != Antenna3)
    model.Add(Antenna1 != Antenna4)
    model.Add(Antenna2 != Antenna1)
    model.Add(Antenna2 != Antenna3)
    model.Add(Antenna2 != Antenna5)
    model.Add(Antenna2 != Antenna6)
    model.Add(Antenna3 != Antenna1)
    model.Add(Antenna3 != Antenna2)
    model.Add(Antenna3 != Antenna6)
    model.Add(Antenna3 != Antenna9)
    model.Add(Antenna4 != Antenna1)
    model.Add(Antenna4 != Antenna2)
    model.Add(Antenna4 != Antenna5)
    model.Add(Antenna5 != Antenna2)
    model.Add(Antenna5 != Antenna4)
    model.Add(Antenna6 != Antenna2)
    model.Add(Antenna6 != Antenna7)
    model.Add(Antenna6 != Antenna8)
    model.Add(Antenna7 != Antenna6)
    model.Add(Antenna7 != Antenna8)
    model.Add(Antenna8 != Antenna7)
    model.Add(Antenna8 != Antenna9)
    model.Add(Antenna9 != Antenna3)
    model.Add(Antenna9 != Antenna8)

    # Solve the problem
    status = solver.Solve(model)

    # Collect results
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        result = {
            'Antenna1': frequencies[solver.Value(Antenna1)],
            'Antenna2': frequencies[solver.Value(Antenna2)],
            'Antenna3': frequencies[solver.Value(Antenna3)],
            'Antenna4': frequencies[solver.Value(Antenna4)],
            'Antenna5': frequencies[solver.Value(Antenna5)],
            'Antenna6': frequencies[solver.Value(Antenna6)],
            'Antenna7': frequencies[solver.Value(Antenna7)],
            'Antenna8': frequencies[solver.Value(Antenna8)],
            'Antenna9': frequencies[solver.Value(Antenna9)]
        }
        return result
    else:
        return "No solution found"


# Sample usage of solve_antenna_frequencies
if __name__ == "__main__":
    solution = solve_antenna_frequencies()
    print(solution)
