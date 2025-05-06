import random
from deap import base, creator, tools, algorithms

# Example evaluation function (minimize a quadratic function)
def eval_func(individual):
    return sum(x ** 2 for x in individual),

# Create fitness and individual classes
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimize the fitness
creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize the toolbox
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5.0, 5.0)  # Example: Float values between -5 and 5
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)  # 3-dimensional individual
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register genetic algorithm operators
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create population
population = toolbox.population(n=50)
generations = 20

# Main loop
for gen in range(generations):
    # Apply crossover and mutation
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    # Evaluate the individuals
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit

    # Select the next generation
    population = toolbox.select(offspring, k=len(population))

# Get the best individual
best_ind = tools.selBest(population, k=1)[0]
best_fitness = best_ind.fitness.values[0]

# Output the results
print("Best individual:", best_ind)
print("Best fitness:", best_fitness)
