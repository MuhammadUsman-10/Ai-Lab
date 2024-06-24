#### Code 01 ####
#### Using random selection ####
#### Distance = 93 but gives random paths ####

# import random

# # Define the distance matrix
# distances = {
#     'A': {'A': 0, 'B': 25, 'C': 42, 'D': 13, 'E': 20},
#     'B': {'A': 25, 'B': 0, 'C': 18, 'D': 50, 'E': 14},
#     'C': {'A': 42, 'B': 18, 'C': 0, 'D': 28, 'E': 19},
#     'D': {'A': 13, 'B': 50, 'C': 28, 'D': 0, 'E': 32},
#     'E': {'A': 20, 'B': 14, 'C': 19, 'D': 32, 'E': 0}
# }

# # Define the fitness function
# def fitness(path):
#     return sum(distances[path[i-1]][path[i]] for i in range(len(path)))

# # Define the selection function
# def selection(population):
#     fitnesses = [fitness(path) for path in population]
#     total = sum(fitnesses)
#     selection_probs = [f/total for f in fitnesses]
#     return random.choices(population, weights=selection_probs, k=2)

# # Define the crossover function
# def crossover(parents):
#     parent1, parent2 = parents
#     child = parent1[:len(parent1)//2] + parent2[len(parent1)//2:]
#     return child

# # Define the mutation function
# def mutate(path):
#     i, j = random.sample(range(len(path)), 2)
#     path[i], path[j] = path[j], path[i]
#     return path

# # Define the GA function
# def genetic_algorithm(population, generations=100):
#     for _ in range(generations):
#         parents = selection(population)
#         child = crossover(parents)
#         child = mutate(child)
#         population.append(child)
#         population = sorted(population, key=fitness)[:len(population)//2]
#     return min(population, key=fitness)

# # Define the initial population
# population = [list(distances.keys()) for _ in range(10)]
# random.shuffle(population)

# # Run the GA
# best_path = genetic_algorithm(population)
# print("Best path:", best_path)
# print("Distance:", fitness(best_path))





#### Code 02 ####
#### Using random selection but uses roulette selection method ####
#### Distance = 93 but gives random paths ####

import random

distances_of_cities = [
    [0, 25, 42, 13, 20],
    [25, 0, 18, 50, 14],
    [42, 18, 0, 28, 19],
    [13, 50, 28, 0, 32],
    [20, 14, 19, 32, 0]
]
heuristic = [0, 5, 18, 12, 9]  # Heuristic values for each city

#fitness 
def fitness(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances_of_cities[path[i]][path[i + 1]]
    total_distance += distances_of_cities[path[-1]][path[0]]  # Return to the starting city
    return total_distance

# initial population
def initial_population(population_size, cities):
    population = []
    for _ in range(population_size):
        node = list(range(cities))
        random.shuffle(node)
        population.append(node)
    return population

# roulette wheel selection
def roulette_wheel_selection(fitness_value):
    fitness = sum(fitness_value)
    r = random.uniform(0, fitness)
    total_fitness = 0
    for i, fitness in enumerate(fitness_value):
        total_fitness += fitness
        if total_fitness >= r:
            return i

# crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2

# mutation
def mutate(node):
    index1, index2 = random.sample(range(len(node)), 2)
    node[index1], node[index2] = node[index2], node[index1]
    return node

# GA
def genetic_algorithm(num_generations, population_size):
    population = initial_population(population_size, len(distances_of_cities))
    for generation in range(num_generations):
        fitness_value = [fitness(node) for node in population]

        # Selection
        new_population = []
        for _ in range(population_size // 2):
            parent1_index = roulette_wheel_selection(fitness_value)
            parent2_index = roulette_wheel_selection(fitness_value)
            parent1 = population[parent1_index]
            parent2 = population[parent2_index]

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    best_route_index = min(range(len(population)), key=lambda i: fitness(population[i]))
    best_route = population[best_route_index]

    return best_route, fitness(best_route)

# Main
if __name__ == "__main__":
    best_route, min_distance = genetic_algorithm(num_generations=100, population_size=50)
    print("Best Route:", best_route)
    print("Minimum Distance:", min_distance)
