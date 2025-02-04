import random
def mutation(C, allowed_items):
    random_point = random.randrange(0, len(C))
    all_items = set(allowed_items)
    C_items = set(C)
    remain_items = all_items.difference(C_items)
    new_gen = random.sample(remain_items, 1)[0]
    Cr = C[0:random_point]+[new_gen]+ C[random_point+1:]
    return Cr

