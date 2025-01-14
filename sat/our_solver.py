import time

def is_safe(board, row, col, n):
    # Check diagonals only (row conflicts impossible in this representation)
    for i in range(col):
        if board[i] == row or \
           abs(board[i] - row) == abs(i - col):
            return False
    return True

def our_solver(n):
    board = [-1] * n
    solutions = []
    stats = {'failures': 0, 'branches': 0}
    
    def backtrack(col):
        if col >= n:
            solutions.append(board[:])
            return
        
        for row in range(n):
            stats['branches'] += 1
            if is_safe(board, row, col, n):
                board[col] = row
                backtrack(col + 1)
            else:
                stats['failures'] += 1
        board[col] = -1
    
    start_time = time.time()
    backtrack(0)
    time_taken = time.time() - start_time
    
    return stats['failures'], stats['branches'], time_taken, len(solutions)