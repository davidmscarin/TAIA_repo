mport time
from itertools import permutations

def solve_n_queens(n):
    cols = range(n)
    solutions = []
    failures = 0
    branches = 0
    
    start_time = time.time()  # Start timing
    
    for perm in permutations(cols):  # Generate all permutations of columns
        branches += 1  # Each permutation is a branch
        valid = True
        for i in range(n):
            for j in range(i + 1, n):
                if abs(perm[i] - perm[j]) == abs(i - j):  # Diagonal conflict
                    valid = False
                    failures += 1  # Count the failure
                    break
            if not valid:
                break
        if valid:
            solutions.append(perm)
    
    end_time = time.time()  # End timing
    
    # Compute total time taken
    time_taken = end_time - start_time
    
    # Return the results
    return {
        time_taken,
        failures,
         branches,
         len(solutions),
        solutions  # Optionally include solutions
    }

# Run the solver for n=8
n = 8
results = solve_n_queens(n)
