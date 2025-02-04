import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def draw_graph_fit_itr(num_run, mut_rate, fitness_itr):
    num_itr = [i+1 for i in range(len(fitness_itr))]
    fig = plt.figure()
    plt.plot(num_itr, fitness_itr)
    # fig.suptitle('', fontsize=20)
    plt.xlabel('Iteration', fontsize=16)
    plt.ylabel('Best fitness', fontsize=16)
    fig.savefig(str(mut_rate)+'_'+str(num_run)+'.png')
    plt.close(fig)

def draw_graph_fit_var_itr(num_run, mut_rate, fitness_var):
    num_itr = [i + 1 for i in range(len(fitness_var))]
    figv = plt.figure()
    plt.plot(num_itr, fitness_var)
    # fig.suptitle('', fontsize=20)
    plt.xlabel('Iteration', fontsize=16)
    plt.ylabel('Variance', fontsize=16)
    figv.savefig('var_' +str(mut_rate)+'_'+str(num_run)+'.png')
    plt.close(figv)

def draw_graph_fit_mrate(mut_array, fitness_m):
    figv = plt.figure()
    plt.plot(mut_array, fitness_m)
    # fig.suptitle('', fontsize=20)
    plt.xlabel('Mutation Rate', fontsize=16)
    plt.ylabel('Best fitness', fontsize=16)
    figv.savefig('mut.png')
    plt.close(figv)