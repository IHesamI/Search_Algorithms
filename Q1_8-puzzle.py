import sys
# %%
# Heuristic function (Manhattan distance)
def heuristic(state, goal_state):
    distance = 0
    ### your implementation ####
    ############################
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal_state[i][j]:
                distance += 1
    return distance

# %%
def get_blank_position(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    row, col = get_blank_position(state)
    
    # Generate neighboring states by swapping the blank tile with its adjacent tiles
    if row > 0:
        neighbor = [list(row) for row in state]
        neighbor[row][col], neighbor[row-1][col] = neighbor[row-1][col], neighbor[row][col]
        neighbors.append(neighbor)
    if row < 2:
        neighbor = [list(row) for row in state]
        neighbor[row][col], neighbor[row+1][col] = neighbor[row+1][col], neighbor[row][col]
        neighbors.append(neighbor)
    if col > 0:
        neighbor = [list(row) for row in state]
        neighbor[row][col], neighbor[row][col-1] = neighbor[row][col-1], neighbor[row][col]
        neighbors.append(neighbor)
    if col < 2:
        neighbor = [list(row) for row in state]
        neighbor[row][col], neighbor[row][col+1] = neighbor[row][col+1], neighbor[row][col]
        neighbors.append(neighbor)
    
    return neighbors

# Successor function
def successors(state):
    successors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_i, empty_j = i, j

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_i, new_j = empty_i + move[0], empty_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[empty_i][empty_j] = new_state[new_i][new_j]
            new_state[new_i][new_j] = 0
            successors.append(new_state)

    return successors

# Goal test function
def is_goal(state, goal_state):
    return state == goal_state

# Print puzzle 
def print_puzzle(state):
    for row in state:
        print(row)

# Recursive Best-First Search
def rbfs(state, goal_state, f_limit):
    if is_goal(state, goal_state):
        return state , f_limit

    ### your implementation ###
    ###########################    
    neighbors = get_neighbors(state)
    # print(neighbor/s)
    if len(neighbors) == 0:
        return None, sys.maxsize
    
    # Calculate the f-value for each neighbor
    f_values = []
    for neighbor in neighbors:
        f = heuristic(neighbor, goal_state) + 1  # f = h + g, where g = 1
        # print(neighbor,f)
        f_values.append(f)
    # index=0
    index=f_values.index(min(f_values))
    # print(index)
    while True:
        # Sort the neighbors based on their f-values
        # sorted_neighbors = [x for _,x in sorted(zip(f_values, neighbors))]
        best_neighbor = neighbors[index]
        best_f = f_values[index]
        # print(best_neighbor,f_values)        

        if best_f > f_limit:
            return None, best_f
        
        # Recursive call to RBFS
        alternative_f = f_values[1] if len(f_values) > 1 else sys.maxsize
        result, best_f = rbfs(best_neighbor, goal_state, min(f_limit, alternative_f))
                
        if result is not None:
            return result, best_f
        f_values[0] = best_f


# Example input
# initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
f_limit = heuristic(initial_state, goal_state)
result ,cost = rbfs(initial_state, goal_state, f_limit)


print("Initial state:")
print_puzzle(initial_state)
if result is not None:
    print("Goal state reached:")
    print_puzzle(result)
    print('cost is :',cost)
else:
    print("Goal state could not be reached.")
