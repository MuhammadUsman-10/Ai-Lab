import random

# Define distance matrix and heuristic values
distances = [
    [0, 25, 42, 13, 20],
    [25, 0, 18, 50, 14],
    [42, 18, 0, 28, 19],
    [13, 50, 28, 0, 32],
    [20, 14, 19, 32, 0]
]

heuristic = [0, 5, 18, 12, 9]  # Heuristic values for each city


def calculate_fitness(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]  # Return to the starting city
    return total_distance


def create_initial_population(population_size, num_cities):
    population = []
    for _ in range(population_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population


def roulette_wheel_selection(fitness_values):
    total_fitness = sum(fitness_values)
    r = random.uniform(0, total_fitness)
    cumulative_fitness = 0
    for i, fitness in enumerate(fitness_values):
        cumulative_fitness += fitness
        if cumulative_fitness >= r:
            return i


def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2


def mutate(individual):
    index1, index2 = random.sample(range(len(individual)), 2)
    individual[index1], individual[index2] = individual[index2], individual[index1]
    return individual


def genetic_algorithm(num_generations, population_size):
    population = create_initial_population(population_size, len(distances))
    for generation in range(num_generations):
        fitness_values = [calculate_fitness(individual) for individual in population]

        # Selection
        new_population = []
        for _ in range(population_size // 2):
            parent1_index = roulette_wheel_selection(fitness_values)
            parent2_index = roulette_wheel_selection(fitness_values)
            parent1 = population[parent1_index]
            parent2 = population[parent2_index]

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    best_route_index = min(range(len(population)), key=lambda i: calculate_fitness(population[i]))
    best_route = population[best_route_index]

    return best_route, calculate_fitness(best_route)


if __name__ == "__main__":
    best_route, min_distance = genetic_algorithm(num_generations=100, population_size=50)
    print("Best Route:", best_route)
    print("Minimum Distance:", min_distance)