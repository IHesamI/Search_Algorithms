from Q2_Min_Max_Alpha import Min_Max_Alpha
import math
import random

initial_state = [3, 5, 6, 9, 1, 2, 0, -1]
depth = int(math.log(len(initial_state), 2))
alpha = float('-inf')
beta = float('+inf')
is_max=True
G_size = 100
P_size = 40
crossover_prob = 0.8
mutation_prob = 0.1

def chromosome_generator(state: list):
    temp = state.copy()
    random.shuffle(temp)
    return temp
# def


def evaluate_function(chromosome: list):
    return Min_Max_Alpha(0, 0, is_max, chromosome, alpha, beta, depth)

def select_parents(population):
    """
    Selects parents from the population for reproduction using tournament selection.
    """
    tournament_size = int(P_size * 0.1)  # Size of the tournament
    parents = []

    while len(parents) < 2:
        tournament = random.sample(population, tournament_size)
        tournament.sort(key=lambda x: evaluate_function(x), reverse=is_max)
        parents.append(tournament[0])

    return parents


def crossover(parent1, parent2):
    """
    Performs crossover between two parents to produce offspring.
    """
    # Select a random subtree from each parent
    subtree_index = random.randint(0, len(parent2) - 1)

    # Create offspring by exchanging the subtrees
    offspring1 = parent1[:subtree_index] + parent2[subtree_index:]
    offspring2 = parent2[:subtree_index] + parent1[subtree_index:]

    return offspring1, offspring2

def mutate(chromosome):
    """
    Performs mutation on a chromosome by randomly replacing a node with a different leaf.
    """
    mutated_chromosome = chromosome.copy()
    node_index = random.randint(0, len(chromosome) - 1)
    leaf_index = random.randint(0, len(initial_state) - 1)
    mutated_chromosome[node_index] = initial_state[leaf_index]
    return mutated_chromosome




def genetic_algorithm():
    population = []
    # generate population
    for _ in range(P_size):
        population.append(chromosome_generator(initial_state))
    scores = []
    for g in range(G_size):
        # new population for next generation
        new_population=[]
        
        while len(new_population) < P_size:
            parent1, parent2 = select_parents(population)

            if random.random() < crossover_prob:
                offspring1, offspring2 = crossover(parent1, parent2)
                new_population.extend([offspring1, offspring2])
            else:
                new_population.extend([parent1, parent2])
        for i in range(P_size):
            if random.random() < mutation_prob:
                new_population[i] = mutate(new_population[i])
    population = new_population

    best_chromosome = max(population, key=lambda x: evaluate_function(x))
    best_fitness = evaluate_function(best_chromosome)
    return best_chromosome , best_fitness
best_tree,best_score=genetic_algorithm()
print("\n--- Genetic Algorithm Complete ---")
print(f"Best Fitness: {best_score}")
print(f"Best Sub Tree: {best_tree}")

