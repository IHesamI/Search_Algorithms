import math


def Min_Max_Alpha(current_depth, index, is_max, values, alpha, beta, tree_depth):

    if current_depth == tree_depth:
        return values[index]

    if is_max:
        best = float('-inf')
        for i in range(2):
            position_of_all_checked_values.add(index*2+i)
            val = Min_Max_Alpha(current_depth+1, index*2+i,
                                not is_max, values, alpha, beta, tree_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            position_of_all_checked_values.add(index*2+i)
            val = Min_Max_Alpha(current_depth+1, index*2+i,
                                not is_max, values, alpha, beta, tree_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def print_pruned(positions, values):
    for i in positions:
        print('Pruned value at {} : {}'.format(i, values[i]))


position_of_all_checked_values = set()

values = [3, 5, 6, 9, 1, 2, 0, -1]
depth = int(math.log(len(values), 2))

alpha = float('-inf')
beta = float('+inf')

print(Min_Max_Alpha(0, 0, True, values, alpha, beta, depth))
pruned_nodes = list(filter(lambda x: not (
    x in position_of_all_checked_values), [i for i in range(len(values))]))
print_pruned(pruned_nodes, values)
