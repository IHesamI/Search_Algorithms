

class Node:
    def __init__(self, cost: int, state: list, alter=None, parentNode=None, successors=None) -> None:
        self.cost = cost
        self.state = state
        self.alter = alter
        self.parentNode = parentNode
        self.successors = successors

    def __eq__(self, other) -> bool:
        return self.cost == other.cost

    def __lt__(self, other) -> bool:
        return self.cost < other.cost

    def __str__(self) -> str:
        matrix_str = "\n["
        for row in self.state:
            row_str = " ".join(str(element) for element in row)
            matrix_str += f"{row_str}\n"
        return matrix_str + '] ' + str(self.cost)

    def __repr__(self) -> str:
        return self.__str__()

    def set_alternative(self, alternative):
        self.alter = alternative

    def update_cost(self, new_cost):
        self.cost = new_cost

    def set_successor(self, successors):
        self.successors = successors

def print_succ(parentnode:Node, succ):
    print('***********')
    print(parentnode.cost)
    print_puzzle(parentnode.state)
    print('---------------')

    for state in succ:
        print(state.cost)
        print_puzzle(state.state)
        print('------')

class Solution:
    def __init__(self, initial_state) -> None:
        self.state = Node(heuristic(initial_state),
                          initial_state, float('inf'))

        # ! NOT SURE IT SHOULD BE COMMENTED
        # self.successors.append(self.state)

    def solve_puzzle(self, goal_state):
        # print(self.state.state)
        if is_goal(self.state, goal_state):
            return self.state.state
        if self.state.successors == None:
            new_successors = successors(self.state)
            new_successors.sort(key=lambda node: node.cost)
            self.state.set_successor(new_successors)

        # * if the new best cost is less than parent node alter
        # * we should explore deeper

        if self.state.alter > self.state.successors[0].cost:
            print('1')

            if self.state.successors[1].cost < self.state.alter:
                self.state.successors[0].set_alternative(
                    self.state.successors[1].cost)
            else:
                self.state.successors[0].set_alternative(self.state.alter)
            # print_puzzle(self.state.successors[0].state)
            print_succ(self.state,self.state.successors)
            self.state = self.state.successors[0]
            self.solve_puzzle(goal_state)
        else:
            print('2')
            self.state.cost = self.state.successors[0].cost
            self.state = self.state.parentNode
            self.solve_puzzle(goal_state)


goal_state_positions = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],

    4: [1, 0],
    5: [1, 1],
    6: [1, 2],

    7: [2, 0],
    8: [2, 1],
    0: [2, 2],

}
# Heuristic function (Manhattan distance)


def heuristic(state):
    distance = 0
    ### your implementation ####
    ############################
    for i in range(len(state)):
        for j in range(len(state)):
            numb = state[i][j]
            x_goal_position = goal_state_positions[numb][0]
            y_goal_position = goal_state_positions[numb][1]
            if i != x_goal_position or y_goal_position != j:
                distance += abs(i-x_goal_position) + abs(j-y_goal_position)

    return distance

# Successor function


def successors(state: Node):
    successors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(3):
            if state.state[i][j] == 0:
                empty_i, empty_j = i, j

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_i, new_j = empty_i + move[0], empty_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state.state]
            new_state[empty_i][empty_j] = new_state[new_i][new_j]
            new_state[new_i][new_j] = 0
            successors.append(Node(cost=heuristic(new_state),
                              state=new_state, alter=None, parentNode=state))

    return successors

# Goal test function


def is_goal(node_state: Node, goal_state: list):
    return node_state.state == goal_state

# Print puzzle


def print_puzzle(state):
    for row in state:
        print(row)

# Recursive Best-First Search


def rbfs(state, goal_state, f_limit):
    if is_goal(state, goal_state):
        return state

    ### your implementation ###
    ###########################


# Example input
# initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

mysolution = Solution(initial_state)
mysolution.solve_puzzle(goal_state)
print_puzzle(mysolution.state.state)


# f_limit = heuristic(initial_state)
# result = rbfs(initial_state, goal_state, f_limit)
# print(initial_state)
# print('------')

# print("Initial state:")
# print_puzzle(initial_state)

# if result is not None:
#     print("Goal state reached:")
#     print_puzzle(result)
# else:
#     print("Goal state could not be reached.")
