from itertools import permutations

def solve_n_queens(n):

    # Generate all possible row arrangements (permutations of columns)
    cols = range(n)
    solutions = []
    
    for perm in permutations(cols):

        valid = True
        for i in range(n):
            for j in range(i + 1, n):
                if abs(perm[i] - perm[j]) == abs(i - j):  # Diagonal conflict
                    valid = False
                    break
            if not valid:
                break
        if valid:
            solutions.append(perm)
    
    return solutions

n = 8
n_queens_solutions = solve_n_queens(n)
print(n_queens_solutions)
print(f"Number of solutions for {n} queens: {len(n_queens_solutions)}")
