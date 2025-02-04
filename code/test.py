from create_population import *
from fitness import *
from selection import *
from cross_over import *
from mutation import *
from calculate_metrics import *
from draw_graph import *
import random
# from numpy import mean, var
import time

def second_largest(numbers):
    m1, m2 = float('-inf'), float('-inf')
    for x in numbers:
        if x >= m1:
            m1, m2 = x, m1
        elif x > m2:
            m2 = x
    return [m2, numbers.index(m2)]

def run_ga(num_run, N, k, allowed_items, Mlist, cross_over_rate, mrate, new_pr_data, new_non_pr_data):
    start_time = time.time()
    ini_pop = create_population(N, k, allowed_items)
    population = ini_pop
    fitness_itr = []
    best_chrom_itr = []
    max_num_generation = 20

    min_mrate = mrate[0]; max_mrate = mrate[1]; step = -1*mrate[2]
    fitness_pop = []
    for chromosome in ini_pop:
        fitness_pop.append(fitness(chromosome, Mlist, allowed_items, new_pr_data, new_non_pr_data)) #list of all chromosome's fitnesses in a population

    min_fitness = min(fitness_pop)
    fitness_itr.append(min_fitness)
    idx_min_fitness = fitness_pop.index(min_fitness)
    best_chrom_itr.append(population[idx_min_fitness]) #the chromosome with the best fitness in a population

    for mutation_rate in np.arange(max_mrate, min_mrate, step):
        mutation_rate = round(mutation_rate, 2)
        current_generation = 1
        while(current_generation <= max_num_generation):
    #################################################### cross_over:
            num_parents = int(cross_over_rate * N)
            parents = select_mating_pool(population, fitness_pop[:], num_parents)
            random.shuffle(parents)
            for i in range(0, num_parents, 2):
                [off_spring_1 , off_spring_2] = position_based_cross_over(population[parents[i]], population[parents[i+1]])
                # [off_spring_1 , off_spring_2] = order_based_cross_over(population[parents[i]], population[parents[i+1]])
                # [off_spring_1 , off_spring_2] = modified_order_cross_over(population[parents[i]], population[parents[i+1]])
                # [off_spring_1 , off_spring_2] = MPMX_cross_over(population[parents[i]], population[parents[i+1]])
                # [off_spring_1 , off_spring_2] = MPX_cross_over(population[parents[i]], population[parents[i+1]])
                # [off_spring_1 , off_spring_2] = order_cross_over(population[parents[i]], population[parents[i+1]])

                fit1 = fitness(off_spring_1, Mlist, allowed_items, new_pr_data, new_non_pr_data)
                fit2 = fitness(off_spring_2, Mlist, allowed_items, new_pr_data, new_non_pr_data)

                population.extend([off_spring_1, off_spring_2])
                fitness_pop.extend([fit1, fit2])
            sorted_fp = sorted(zip(fitness_pop, population))
            population = [y for _, y in sorted_fp][0:N]
            fitness_pop = [x for x, _ in sorted_fp][0:N]

    ####################################################
            num_mut = int(mutation_rate * N)
            all_ch = list(set(range(0, N)))
            mut_ch = random.sample(all_ch, num_mut)

            for ch in mut_ch:
                C = population[ch] #N0
                fitness_C = fitness_pop[ch] #E0

                chrom = mutation(C, allowed_items) #N1
                fitness_chrom = fitness(chrom, Mlist, allowed_items, new_pr_data, new_non_pr_data) #E1

                if fitness_chrom < fitness_C:
                    population[ch] = chrom
                    fitness_pop[ch] = fitness_chrom
                else:
                    accept_prob = math.exp((fitness_C -fitness_chrom)/mutation_rate)
                    random_num = random.uniform(0, 1)
                    if accept_prob >= random_num:
                        # print('F')
                        population[ch] = chrom
                        fitness_pop[ch] = fitness_chrom
                    # else:
                    #     print('True')

            min_fitness = min(fitness_pop)
            fitness_itr.append(min_fitness) #the best fitness of a generation(itr) is appended
            idx_min_fitness = fitness_pop.index(min_fitness)
            best_chrom_itr.append(population[idx_min_fitness])


            current_generation += 1

    # draw_graph_fit_itr(num_run, mutation_rate, fitness_itr)
    # draw_graph_fit_var_itr(num_run, mutation_rate, fitness_var_itr)

    fc = open('itr.txt', 'a')
    fc.write(str(fitness_itr)+'\n')
    fc.close()
    best_gen_fitness = min(fitness_itr)

    solution = best_chrom_itr[fitness_itr.index(best_gen_fitness)]
    end_time = time.time()
    start_end_time = end_time - start_time
    # print(solution)
    # print(best_gen_fitness)

    g_arr_sol = np.zeros(shape=(k, len(Mlist)))
    sol_scores = []
    sc = 0
    for sol in solution:
        y = np.where(new_pr_data[:,:,0] == sol)
        list_where = list(zip(y[0], y[1]))

        if list_where == []:
            y = np.where(new_non_pr_data[:,0] == sol)[0][0]
            sol_scores.append(new_non_pr_data[y][3])
        else:
            sol_scores.append(new_pr_data[list_where[0][0], list_where[0][1], 3])
            for l in list(y[0]):
                g_arr_sol[sc][l] = 1
        sc += 1

    dcg = DCG(sol_scores)

    return best_gen_fitness, solution, g_arr_sol, sol_scores, dcg, start_end_time