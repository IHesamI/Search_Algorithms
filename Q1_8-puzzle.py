# Node Class 
# this class helps to traverse through tree
class Node:
    def __init__(self, cost: int, state: list, alter=None, parentNode=None, successors=None) -> None:
        self.cost = cost
        self.state = state
        self.alter = alter
        self.parentNode = parentNode
        self.successors = successors
        self.lower_priority = 0

    def __eq__(self, other):
        if other is None:
            return False
        return (self.cost, self.lower_priority) == (other.cost, other.lower_priority)

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.lower_priority < other.lower_priority
        return self.cost < other.cost

    def decrease_priority(self):
        self.lower_priority += 1

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


def print_succ(parentnode: Node, succ):
    print('***********')
    print(parentnode.cost, " , ", parentnode.alter)
    print_puzzle(parentnode.state)
    print('---------------')

    for state in succ:
        print(state.cost, " , ", state.alter)
        print_puzzle(state.state)
        print('------')

def find_alter_for(state:Node,successors:list):
    list_of_values=[state.alter]
    list_of_values.extend([succ.cost for succ in successors])
    return min(list_of_values,key=lambda x : float('inf') if x is None else x)

class Solution:
    def __init__(self, initial_state) -> None:
        self.state = Node(heuristic(initial_state),
                          initial_state, float('inf'))

    def rbfs(self, goal_state):
        if is_goal(self.state, goal_state):
                # print_puzzle(self.state.state)
                return 
        try:
            # ! when try to explore the node for the first time
            if self.state.successors == None:
                new_successors = successors(self.state)
                new_successors.sort(key=lambda node: node.cost)
                self.state.set_successor(new_successors)

            # * if the new best cost is less than parent node alter
            # * we should explore deeper

            # !
            else:
                self.state.successors = sorted(self.state.successors)

            # print_succ(self.state,self.state.successors)
            if check_for_loop(self.state.successors[0], self.state.parentNode):
                # print('zarppp')
                self.state.successors[0].cost = float('inf')
                # TODO
                # Need to set alter of the next_best_node
                self.state.successors[1].alter = find_alter_for(self.state,self.state.successors)
                self.state.successors = sorted(self.state.successors)

            if self.state.alter > self.state.successors[0].cost:
                self.state.successors[0].set_alternative(min(self.state.successors[1].cost,self.state.alter))
                self.state = self.state.successors[0]
                self.rbfs(goal_state)

            else:
                # print('2')
                self.state.cost = self.state.successors[0].cost
                self.state.decrease_priority()
                self.state = self.state.parentNode
                self.rbfs(goal_state)
            return
        except Exception as e:
            self.state=None
            return


def check_for_loop(best_succssor: Node, parentnode: Node):
    if parentnode == None:
        return False
    else:
        return is_goal(best_succssor, parentnode.state)


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
    if node_state==None or node_state.state==None:
        return False
    return node_state.state == goal_state

# Print puzzle


def print_puzzle(state):
    if state ==None:
        print('None')
        return
    # if result is not None:

    for row in state:
        print(row)

# Recursive Best-First Search


# def rbfs(state, goal_state, f_limit):
#     if is_goal(state, goal_state):
#         return state

    ### your implementation ###
    ###########################


# Example input

# *Best Result
# initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]

# !WORST Result
# initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

mysolution = Solution(initial_state)


# f_limit = heuristic(initial_state)
# result = rbfs(initial_state, goal_state, f_limit)
# print(initial_state)

print("Initial state:")
print_puzzle(initial_state)
print('------')

mysolution.rbfs(goal_state)


#     print_puzzle(result)
if is_goal(mysolution.state,goal_state):
    print("Goal state reached:")
    print_puzzle(mysolution.state.state)
else:
    print("Goal state could not be reached.")
