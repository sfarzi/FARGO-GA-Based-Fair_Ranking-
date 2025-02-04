import math
def DCG(score_solution):
    DCG_val = 0
    for i in range(len(score_solution)):
        w_i = 1/math.log((i+2), 2)
        q_i = score_solution[i]
        wq = w_i * q_i
        DCG_val = DCG_val + wq
    return DCG_val