import heapq

def n_queens(n):
    def heuristic(board):
        # Count the number of queens that are attacking each other
        queens = [(i, j) for i, val in enumerate(board) for j, is_queen in enumerate(val) if is_queen]
        return sum(1 for i, j in queens for x, y in queens if i != x and j != y and abs(i - x) == abs(j - y))

    def generate_board(queens):
        # Generate a board with the specified queens placed on it
        board = [[0] * n for _ in range(n)]
        for x, y in queens:
            board[x][y] = 1
        return board

    def generate_neighbors(board):
        # Generate all boards that can be reached by moving a single queen
        queens = [(i, j) for i, val in enumerate(board) for j, is_queen in enumerate(val) if is_queen]
        for x, y in queens:
            for i in range(n):
                if i != x:
                    new_queens = [(i, y) if (i, j) == (x, y) else (i, j) for i, j in queens]
                    yield generate_board(new_queens)

    start = generate_board([(0, i) for i in range(n)])
    heap = [(heuristic(start), start)]
    visited = set()

    while heap:
        _, current = heapq.heappop(heap)
        if heuristic(current) == 0:
            return current
        for neighbor in generate_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(heap, (heuristic(neighbor), neighbor))

    return None

result = n_queens(8)
for row in result:
    for val in row:
        print(val, end=" ")
    print()

