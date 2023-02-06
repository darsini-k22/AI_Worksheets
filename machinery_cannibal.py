import heapq

class State:
    def __init__(self, missionaries, cannibals, boat, cost, parent):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.cost = cost
        self.parent = parent

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0

    def is_valid(self):
        if self.missionaries < 0 or self.missionaries > 3:
            return False
        if self.cannibals < 0 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if (3 - self.missionaries) < (3 - self.cannibals) and (3 - self.missionaries) > 0:
            return False
        return True

    def __lt__(self, other):
        return self.cost < other.cost

def astar(start, goal):
    heap = []
    heapq.heappush(heap, start)
    while heap:
        current = heapq.heappop(heap)
        if current.is_goal():
            return current
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            if current.boat == 1:
                next_state = State(current.missionaries - move[0], current.cannibals - move[1], 0, current.cost + 1, current)
                if next_state.is_valid():
                    heapq.heappush(heap, next_state)
            else:
                next_state = State(current.missionaries + move[0], current.cannibals + move[1], 1, current.cost + 1, current)
                if next_state.is_valid():
                    heapq.heappush(heap, next_state)
    return None

start = State(3, 3, 1, 0, None)
goal = State(0, 0, 0, 0, None)
result = astar(start, goal)
if result is None:
    print("No solution found")
else:
    path = []
    while result:
        path.append(result)
        result = result.parent
    for i in range(len(path) - 1, -1, -1):
        state = path[i]
        print("Step {}: Missionaries = {}, Cannibals = {}, Boat = {}".format(len(path) - i - 1, state.missionaries, state.cannibals, state.boat))

