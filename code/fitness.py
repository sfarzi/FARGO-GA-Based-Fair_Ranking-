from utility_loss import *
from in_group_monotonicity import *
import numpy as np

def step_func(M, g, i):
    sum_g = sum(g[0:i+1])
    Mi = M[i]
    if Mi <= sum_g:
        return 0
    else:
        return 1

def weighted_sum_score(score):
    sum_score = 0
    for i in range(len(score)):
        weight = 1/(i+1)
        sum_score = sum_score + score[i]*weight
    return sum_score

def fitness(chromosome, Mlist, allowed_items, new_pr_data, new_non_pr_data):
    score = []; k = len(chromosome)
    g_arr = np.zeros(shape=(k, len(Mlist)))
    for c in range(k):
        item = chromosome[c]
        y = np.where(new_pr_data[:,:,0] == item)
        list_where = list(zip(y[0], y[1]))

        if list_where == []:
            y = np.where(new_non_pr_data[:,0] == item)[0][0]
            score.append(new_non_pr_data[y][3])
        else:
            score.append(new_pr_data[list_where[0][0],list_where[0][1],3])
            for l in list(y[0]):
                g_arr[c][l] = 1

    remain_items = find_exclude_items(chromosome, allowed_items)
    sel_loss = selection_loss(remain_items, score, new_pr_data, new_non_pr_data)
    non_mono_npr = 0; non_mono_pr = 0
    C = g_arr.shape[1]
    for i in range(C):
        non_mono_npr = non_monotonicity(score, list(g_arr[:,i]), 0) + non_mono_npr
        sys_bias = 0; eps = 1.0
        for j in range(k):
            sys_bias = step_func(Mlist[i], g_arr[:,i], j) + sys_bias
        sys_bias = sys_bias / k + eps

        non_mono_pr = non_monotonicity(score, list(g_arr[:,i]), 1) * sys_bias + non_mono_pr



    wss = weighted_sum_score(score)
    fitness = (sel_loss * non_mono_pr/C * non_mono_npr/C)/wss #*(non_mono_ch)

    return fitness
##################################################################################################
def fitness_info(chromosome, Mlist, allowed_items, new_pr_data, new_non_pr_data):
    score = []; k = len(chromosome)
    g_arr = np.zeros(shape=(k, len(Mlist)))
    for sc in range(k):
        item = chromosome[sc]
        y = np.where(new_pr_data[:,:,0] == item)
        list_where = list(zip(y[0], y[1]))

        if list_where == []:
            y = np.where(new_non_pr_data[:, 0] == item)[0][0]
            score.append(new_non_pr_data[y][3])
        else:
            score.append(new_pr_data[list_where[0][0],list_where[0][1],3])
            for l in list(y[0]):
                g_arr[sc][l] = 1

    remain_items = find_exclude_items(chromosome, allowed_items)
    sel_loss = selection_loss(remain_items, score, new_pr_data, new_non_pr_data)
    non_mono_npr = 0; non_mono_pr = 0
    non_mono_npr_list = []; non_mono_pr_list = []; sys_bias_list = []
    C = g_arr.shape[1]
    for i in range(C):
        non_mono_npr_temp = non_monotonicity(score, list(g_arr[:,i]), 0)
        non_mono_npr_list.append(non_mono_npr_temp)
        non_mono_npr = non_mono_npr_temp + non_mono_npr
        sys_bias = 0; eps = 1.0
        for j in range(k):
            sys_bias = step_func(Mlist[i], g_arr[:,i], j) + sys_bias
        sys_bias = sys_bias / k + eps
        sys_bias_list.append(sys_bias)
        non_mono_pr_temp = non_monotonicity(score, list(g_arr[:, i]), 1)
        non_mono_pr_list.append(non_mono_pr_temp)
        non_mono_pr = non_mono_pr_temp * sys_bias + non_mono_pr



    wss = weighted_sum_score(score)
    fitness = (sel_loss * non_mono_pr/C * non_mono_npr/C)/wss #*(non_mono_ch)

    return [fitness, wss, sel_loss,non_mono_npr_list, non_mono_pr_list, sys_bias_list]