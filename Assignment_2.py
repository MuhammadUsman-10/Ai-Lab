import random

items = [
    {"name": "A", "weight": 2200, "value": 15},
    {"name": "B", "weight": 400, "value": 18},
    {"name": "C", "weight": 250, "value": 9},
    {"name": "D", "weight": 370, "value": 12},
    {"name": "E", "weight": 90, "value": 5}
]

knapsack_capacity = 2000  # grams

# Genetic Algorithm parameters
population_size = 6
generations = 3
mutation_rate = 0.1

def evaluate_fitness(solution):
    total_weight = sum(item["weight"] if bit else 0 for bit, item in zip(solution, items))
    total_value = sum(item["value"] if bit else 0 for bit, item in zip(solution, items))

    if total_weight > knapsack_capacity:
        return 0  # Exceeds capacity of knapsack
    else:
        return total_value

# Define the population
def initialize_population():
    return [[random.randint(0, 1) for _ in range(len(items))] for _ in range(population_size)]

# crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# mutation function
def mutate(solution):
    # Flip a random gene with a certain probability
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = 1 - solution[i]
    return solution

def main():
    population = initialize_population()

    for generation in range(generations):
        population.sort(key=evaluate_fitness, reverse=True)
        print(f"Generation {generation + 1}: Best fitness = {evaluate_fitness(population[0])}")

        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.choices(population, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    best_solution = population[0]
    selected_items = [item["name"] for i, item in enumerate(items) if best_solution[i]]
    print(f"Selected items: {', '.join(selected_items)}")

if __name__ == "__main__":
    main()