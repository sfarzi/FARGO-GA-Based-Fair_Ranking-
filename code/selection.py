# import random
import numpy as np
# def roullete_selection(population, fitness_pop): #return one parent based on Roulette Wheel Selection
#     max = sum(fitness_pop)
#     pick = random.uniform(0, max)
#     current_fitness = 0
#     for ch in range(len(population)):
#         current_fitness += fitness_pop[ch]
#         if current_fitness > pick:
#             return population[ch]

def select_mating_pool(population, fitness_pop, num_parents):
    # Selecting the best individuals in the current generation as
    # parents for producing the offspring of the next generation.
    parents = []
    for parent_num in range(num_parents):
        min_fitness_idx = np.where(fitness_pop == np.min(fitness_pop))
        min_fitness_idx = min_fitness_idx[0][0]
        parents.append(min_fitness_idx)
        fitness_pop[min_fitness_idx] = 1000000

    return parents