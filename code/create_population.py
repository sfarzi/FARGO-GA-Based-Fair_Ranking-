from create_chromosome import *

def create_population(N, k, allowed_items): #N: population_size

    population = []
    for i in range(N):
        population.append(create_chromosome(k, allowed_items))
    return population


