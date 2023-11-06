n = int(input("Enter the number of missionaries and cannibals: "))
boat_capacity = int(input("Enter the boat capacity: "))

def format_bank(bank):
    return f"({bank[0]}M, {bank[1]}C, {bank[2]})"

def is_valid(state):
    left_bank, right_bank = state
    if (left_bank[0] < left_bank[1] and left_bank[0] > 0) or (right_bank[0] < right_bank[1] and right_bank[0] > 0):
        return False
    for value in left_bank + right_bank:
        if value < 0 or value > n:
            return False
    return True

def generate_successors(state):
    left_bank, right_bank = state
    successors = []
    if left_bank[2] == 1:
        for m in range(n + 1):
            for c in range(n + 1):
                if m + c > 0 and m + c <= boat_capacity:
                    new_left = (left_bank[0] - m, left_bank[1] - c, 0)
                    new_right = (right_bank[0] + m, right_bank[1] + c, 1)
                    new_state = (new_left, new_right)
                    if is_valid(new_state):
                        successors.append(new_state)
    else:
        for m in range(n + 1):
            for c in range(n + 1):
                if m + c > 0 and m + c <= boat_capacity:
                    new_left = (left_bank[0] + m, left_bank[1] + c, 1)
                    new_right = (right_bank[0] - m, right_bank[1] - c, 0)
                    new_state = (new_left, new_right)
                    if is_valid(new_state):
                        successors.append(new_state)
    return successors

def solve():
    start_state = ((n, n, 1), (0, 0, 0))
    goal_state = ((0, 0, 0), (n, n, 1))
    frontier = [([start_state], [start_state])]
    while frontier:
        path, state = frontier.pop(0)
        current_state = state[-1]
        if current_state == goal_state:
            return path
        for successor in generate_successors(current_state):
            if successor not in state:
                new_path = list(path)
                new_path.append(successor)
                new_state = list(state)
                new_state.append(successor)
                frontier.append((new_path, new_state))
    return None

def print_solution(path):
    if path:
        for i, state in enumerate(path):
            left_bank, right_bank = state
            print(f"Step {i + 1}")
            print(f"Left Bank: {format_bank(left_bank)}")
            print(f"Right Bank: {format_bank(right_bank)}")
            print()

if __name__ == "__main__":
    solution_path = solve()
    if solution_path:
        print("Solution Found:")
        print_solution(solution_path)
    else:
        print("No solution found")
























/*from collections import deque
def generatenextstates(state, m, n):
    m_left, c_left, boat, m_right, c_right = state
    moves = [(0, 1), (0, 2), (1,0), (2, 0), (1, 1)]
    possible_states = []

    for i in moves:
        if boat == 1:
            move_str = str(i[0]) + "M " + str(i[1]) + "C move from left to right"
            new_state = (m_left - i[0], c_left - i[1], 0, m_right + i[0], c_right + i[1])
        else:
            move_str = str(i[0]) + "M " + str(i[1]) + "C  move from right to left"
            new_state = (m_left + i[0], c_left + i[1], 1, m_right - i[0], c_right - i[1])

        if checkvalidstate(new_state, m, n):
            possible_states.append((new_state, move_str))

    return possible_states
def checkvalidstate(state, m, n):
    m_left, c_left, boat, m_right, c_right = state

    if (
        0 <= m_left <= m and
        0 <= c_left <= n and
        0 <= m_right <= m and
        0 <= c_right <= n and
        (m_left == 0 or m_left >= c_left) and
        (m_right == 0 or m_right >= c_right)):
        return True

    return False
def bfs(m, n):
    initial_state = (m, n, 1, 0, 0)
    visited = set()
    queue = deque()
    queue.append((initial_state, []))

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if checkfinalstate(current_state, m):
            return path

        for next_state, move_description in generatenextstates(current_state, m, n):
            if next_state not in visited:
                queue.append((next_state, path + [(next_state, move_description)]))
def checkfinalstate(state, m):
    return state == (0, 0, 0, m, m)
def  path(s):
    print("Initial state:")
    print("Boat position:left")
    print("left side of river:",m,"M",n,"C")
    print("right side of river:",0,"M",0,"C")
    for i in range(len(s)):
        state, move_description = s[i]
        m_left, c_left, boat, m_right, c_right = state
        if boat == 1:
            boat_position = "left"
        else:
            boat_position="right"
        print("Step", i + 1,":")
        print(move_description)
        print( m_left, "M", c_left, "C"," Left side of river:" )
        print( "M", c_right, "C ","Right side of river:", m_right)
        print(" Boat position:", boat_position)
m = int(input("Enter the number of missionaries (m): "))
n = int(input("Enter the number of cannibals (n): "))
solution = bfs(m, n)
if solution:
    print("Solution found!")
    path(solution)
else:
    print("No solution found")*/
