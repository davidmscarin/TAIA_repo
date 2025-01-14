import os
import matplotlib.pyplot as plt
from n_queens_original_SAT import original_SAT_solver
from n_queens_cpSAT import cp_SAT_solver
from ortools.constraint_solver import pywrapcp

def main():

    # Configure plot style
    plt.style.use('ggplot')
    
    # Define board sizes to test
    sizes = range(8, 14)
    
    # Data structures for statistics
    stats = {
        'original': {'time': [], 'solutions': [], 'branches': [], 'failures': []},
        'cp': {'time': [], 'solutions': [], 'branches': [], 'failures': []}
    }
    
    # Collect data
    for size in sizes:
        
        # Get stats from original solver
        orig_failures, orig_branches, orig_time, orig_solutions = original_SAT_solver(size)
        orig_time = orig_time/1000  #convert to seconds

        # Get stats from CP-SAT solver
        cp_conflicts, cp_branches, cp_time, cp_solutions = cp_SAT_solver(size)
        
        # Store statistics
        stats['original']['time'].append(orig_time)
        stats['original']['solutions'].append(orig_solutions)
        stats['original']['branches'].append(orig_branches)
        stats['original']['failures'].append(orig_failures)
        stats['cp']['time'].append(cp_time)
        stats['cp']['solutions'].append(cp_solutions)
        stats['cp']['branches'].append(cp_branches)
        stats['cp']['failures'].append(cp_conflicts)

    # Time comparison plot
    plt.figure(figsize=(10, 6))
    plt.plot(sizes[:len(stats['original']['time'])], 
             stats['original']['time'], 'o-', label="Original SAT")
    plt.plot(sizes[:len(stats['cp']['time'])], 
             stats['cp']['time'], 's-', label="CP-SAT")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Time (s)")
    plt.title("N-Queens Solver Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/time_comparison.png')
    plt.show()


    #Failures comparison plot
    plt.figure(figsize=(10, 6))
    plt.figure(figsize=(10, 6))
    plt.plot(sizes[:len(stats['original']['failures'])], 
             stats['original']['failures'], 'o-', label="Original SAT")
    plt.plot(sizes[:len(stats['cp']['failures'])], 
             stats['cp']['failures'], 's-', label="CP-SAT")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Time (s)")
    plt.title("N-Queens Solver Failures Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/n_failures_comparison.png')
    plt.show()

    #branches comparison plot
    plt.figure(figsize=(10, 6))
    plt.figure(figsize=(10, 6))
    plt.plot(sizes[:len(stats['original']['branches'])], 
             stats['original']['branches'], 'o-', label="Original SAT")
    plt.plot(sizes[:len(stats['cp']['branches'])], 
             stats['cp']['branches'], 's-', label="CP-SAT")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Time (s)")
    plt.title("N-Queens Solver Branches Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/n_branches_comparison.png')
    plt.show()

    #no. solutions cp-sat solver
    plt.figure(figsize=(10, 6))
    plt.plot(sizes[:len(stats['cp']['solutions'])], 
             stats['cp']['solutions'], 's-')
    plt.xlabel("Board Size (N)")
    plt.ylabel("Number of Solutions")
    plt.title("N-Queens Solutions Found")
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/n_solutions_cp_sat.png')
    plt.show()


    #no. solutions original solver
    plt.figure(figsize=(10, 6))
    plt.plot(sizes[:len(stats['original']['solutions'])], 
             stats['original']['solutions'], 'o-', label="Original SAT", color='blue')
    plt.xlabel("Board Size (N)")
    plt.ylabel("Number of Solutions")
    plt.title("N-Queens Solutions Found")
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/n_solutions_original.png')
    plt.show()

if __name__ == "__main__":
    main()