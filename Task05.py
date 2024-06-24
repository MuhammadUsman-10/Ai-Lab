import random


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class GA:
    def __init__(self, cities, population_size, crossover_rate, mutation_rate, num_generations):
        self.cities = cities
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.population = self.init_population()

    def init_population(self):
        population = []
        for _ in range(self.population_size):
            permutation = random.sample(range(len(self.cities)), len(self.cities))
            population.append(permutation)
        return population

    def fitness(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            city1 = self.cities[route[i]]
            city2 = self.cities[route[i + 1]]
            total_distance += city1.distance(city2)
        total_distance += self.cities[route[-1]].distance(self.cities[route[0]])
        return 1 / total_distance

    def selection(self):
        fitness_values = [self.fitness(route) for route in self.population]
        total_fitness = sum(fitness_values)
        probabilities = [fitness / total_fitness for fitness in fitness_values]
        selected = []
        for _ in range(self.population_size):
            spin = random.random()
            prob_sum = 0
            for i in range(len(self.population)):
                prob_sum += probabilities[i]
                if prob_sum >= spin:
                    selected.append(self.population[i].copy())
                    break
        return selected

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 2)
        child1 = []
        child2 = []
        for gene in parent1[:crossover_point]:
            child1.append(gene)
        for gene in parent2:
            if gene not in child1:
                child1.append(gene)
        for gene in parent2[:crossover_point]:
            child2.append(gene)
        for gene in parent1:
            if gene not in child2:
                child2.append(gene)
        return child1, child2

    def mutation(self, route):
        if random.random() < self.mutation_rate:
            i1, i2 = random.sample(range(len(route)), 2)
            route[i1], route[i2] = route[i2], route[i1]
        return route

    def run(self):
        best_distance = float('inf')
        best_route = None
        for generation in range(self.num_generations):
            selected = self.selection()
            offspring = []
            for i in range(0, self.population_size, 2):
                parent1, parent2 = selected[i], selected[i + 1]
                if random.random() < self.crossover_rate:
                    child1, child2 = self.crossover(parent1, parent2)
                else:
                    child1, child2 = parent1.copy(), parent2.copy()
                offspring.append(self.mutation(child1))
                offspring.append(self.mutation(child2))
            self.population = offspring

            for route in self.population:
                distance = self.fitness(route)
                if distance < best_distance:
                    best_distance = distance
                    best_route = route.copy()

            print(f"Generation {generation+1} | Best distance: {best_distance}")

        return best_route, best_distance


if __name__ == "__main__":
    cities = [City(25, 42), City(18, 50), City(42, 18), City(13, 28), City(20, 14)]
    ga = GA(cities, population_size=100, crossover_rate=0.8, mutation_rate=0.01, num_generations=100)
    best_route, best_distance = ga.run()
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
