import math
from Q2_Min_Max_Alpha import Min_Max_Alpha , position_of_all_checked_values ,print_pruned
def __main():
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth = int(math.log(len(values), 2))

    alpha = float('-inf')
    beta = float('+inf')

    print("Optimal value :",Min_Max_Alpha(0, 0, True, values, alpha, beta, depth))
    pruned_nodes = list(filter(lambda x: not (
        x in position_of_all_checked_values), [i for i in range(len(values))]))
    print_pruned(pruned_nodes, values)

__main()
