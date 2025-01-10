from pysat.solvers import Glucose3


def gen_dict(vars, size):
    var_dict = {}
    k = 1
    for i in vars:
        for j in range(0, size):
            var_dict[(i, j)] = k
            k += 1
    return var_dict


def gen_clauses(vars, size, var_dict):
    clauses = []
    for i in vars:
        for j in range(0, size):
            clause = []
            for k in range(0, size):
                if k != j:
                    clause.append(-var_dict[(i, k)])
            clause.append(var_dict[(i, j)])
            clauses.append(clause)
    return clauses


''' Only one Solution
def solve_n_queens_sat(board_size):

    vars = [f"x{i}" for i in range(board_size)]
    var_dict = gen_dict(vars, board_size)
    clauses = gen_clauses(vars, board_size, var_dict)



    for row in range(board_size):
        clauses.append([var_dict[(f"x{row}", col)] for col in range(board_size)])


    for i in range(board_size):
        for j in range(board_size):
            for k in range(i + 1, board_size):
                if 0 <= j + (k - i) < board_size:
                    clauses.append([-var_dict[(f"x{i}", j)], -var_dict[(f"x{k}", j + (k - i))]])
                if 0 <= j - (k - i) < board_size:
                    clauses.append([-var_dict[(f"x{i}", j)], -var_dict[(f"x{k}", j - (k - i))]])

    #print(clauses)
    solver = Glucose3()
    for clause in clauses:
        solver.add_clause(clause)

    if solver.solve():
        model = solver.get_model()
        solutions = [var for var in model if var > 0]
        return solutions
    else:
        return None



solutions = solve_n_queens_sat(8)
print("SAT Solutions:", solutions)
'''


'''All Solutions'''

def solve_all_n_queens_sat(board_size):
    vars = [f"x{i}" for i in range(board_size)]
    var_dict = gen_dict(vars, board_size)
    clauses = []

    # Each row must have exactly one queen
    for row in range(board_size):
        clauses.append([var_dict[(f"x{row}", col)] for col in range(board_size)])

    # No two queens in the same column
    for col in range(board_size):
        for row1 in range(board_size):
            for row2 in range(row1 + 1, board_size):
                clauses.append([-var_dict[(f"x{row1}", col)], -var_dict[(f"x{row2}", col)]])

    # No diagonal attacks
    for i in range(board_size):
        for j in range(board_size):
            for k in range(i + 1, board_size):
                if 0 <= j + (k - i) < board_size:
                    clauses.append([-var_dict[(f"x{i}", j)], -var_dict[(f"x{k}", j + (k - i))]])
                if 0 <= j - (k - i) < board_size:
                    clauses.append([-var_dict[(f"x{i}", j)], -var_dict[(f"x{k}", j - (k - i))]])

    solver = Glucose3()
    for clause in clauses:
        solver.add_clause(clause)

    all_solutions = []
    while solver.solve():
        model = solver.get_model()
        solution = [var for var in model if var > 0]
        all_solutions.append(solution)

        # Block the current solution
        solver.add_clause([-var for var in solution])

    return all_solutions


# Find all solutions for the 8-queens problem
all_solutions = solve_all_n_queens_sat(8)
print(f"Total Solutions: {len(all_solutions)}")
for sol in all_solutions:
    print("SAT Solution:", sol)
print("Total Solutions:", len(all_solutions))