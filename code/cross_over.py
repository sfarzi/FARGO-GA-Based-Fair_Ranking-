import random
# def cross_over(ch1, ch2): #2-point
#     off_spring_1 = []
#     random_point_1 = random.randrange(0, len(ch1) -1)
#     random_point_2 = random.randrange(0, len(ch1) - 1)
#     while random_point_1 == random_point_2:
#         random_point_2 = random.randrange(0, len(ch1) - 1)
#     if random_point_2 < random_point_1:
#         random_point_1, random_point_2 = random_point_2, random_point_1
#
#     off_spring_1 = ch1[0:random_point_1]+ ch2[random_point_1:random_point_2]+ch1[random_point_2:]
#     off_spring_2 = ch2[0:random_point_1]+ ch1[random_point_1:random_point_2]+ch2[random_point_2:]
#
#     return off_spring_1,off_spring_2

########################################################################################################
def order_cross_over(ch1, ch2): #OX1
    k = len(ch1)
    random_point_1 = random.randrange(0, k - 1)
    random_point_2 = random.randrange(0, k - 1)
    while random_point_1 == random_point_2:
        random_point_2 = random.randrange(0, k - 1)
    if random_point_2 < random_point_1:
        random_point_1, random_point_2 = random_point_2, random_point_1
    off_spring_1 = [-1 for i in range(k)]
    off_spring_2 = [-1 for i in range(k)]
    substring1 = ch1[random_point_1:random_point_2 + 1]
    substring2 = ch2[random_point_1:random_point_2 + 1]
    off_spring_1[random_point_1:random_point_2 + 1]= substring2
    off_spring_2[random_point_1:random_point_2 + 1]= substring1
    # remain_ch1 = ch1[0:random_point_1] + ch1[random_point_2 + 1:]
    # remain_ch2 = ch2[0:random_point_1] + ch2[random_point_2 + 1:]
    for s in ch1:
        if s not in substring2:
            try:
                idx = off_spring_1.index(-1)
                off_spring_1[idx] = s
            except ValueError:
                break

    for s in ch2:
        if s not in substring1:
            try:
                idx = off_spring_2.index(-1)
                off_spring_2[idx] = s
            except ValueError:
                break

    return off_spring_1,off_spring_2
########################################################################################################
def position_based_cross_over(ch1, ch2):
    k = len(ch1)
    set_random_size = random.randrange(1, k//2 + 1)
    # print(set_random_size)
    rand_list = []; c = 1
    while c <= set_random_size:
        random_point = random.randrange(0, k - 1)
        if random_point not in rand_list:
            rand_list.append(random_point)
            c += 1
    # print(rand_list)
    off_spring_1 = [-1 for i in range(k)]
    off_spring_2 = [-1 for i in range(k)]

    ch1_list, ch2_list = [], []
    for r in rand_list:
        off_spring_1[r] = ch1[r]
        off_spring_2[r] = ch2[r]
        ch1_list.append(ch1[r])
        ch2_list.append(ch2[r])

    for s in ch2:
        if s not in ch1_list:
            try:
                idx = off_spring_1.index(-1)
                off_spring_1[idx] = s
            except ValueError:
                break

    for s in ch1:
        if s not in ch2_list:
            try:
                idx = off_spring_2.index(-1)
                off_spring_2[idx] = s
            except ValueError:
                break

    return off_spring_1,off_spring_2
########################################################################################################
def order_based_cross_over(ch1, ch2): #OX2
    k = len(ch1)
    set_random_size = random.randrange(1, k//2 + 1)
    # print(set_random_size)
    rand_list = []; c = 1
    while c <= set_random_size:
        random_point = random.randrange(0, k - 1)
        if random_point not in rand_list:
            rand_list.append(random_point)
            c += 1
    # print(rand_list)
    off_spring_1 = [-1 for i in range(k)]
    off_spring_2 = [-1 for i in range(k)]

    ch1_list, ch2_list = [], []
    for r in rand_list:
        ch1_list.append(ch1[r])
        ch2_list.append(ch2[r])

    j = 0; i=0
    for s in ch2:
        if s not in ch1_list:
            off_spring_1[j] = s
        else:
            off_spring_1[j] = ch1_list[i]
            i += 1
        j += 1

    j = 0; i=0
    for s in ch1:
        if s not in ch2_list:
            off_spring_2[j] = s
        else:
            off_spring_2[j] = ch2_list[i]
            i += 1
        j += 1

    return off_spring_1,off_spring_2
########################################################################################################
def modified_order_cross_over(ch1, ch2): #modified version of OX2
    k = len(ch1)
    rand_list = [i for i in range(k//2 , k)]
    # print(rand_list)

    off_spring_1 = [-1 for i in range(k)]
    off_spring_2 = [-1 for i in range(k)]

    ch1_list, ch2_list = [], []
    for r in rand_list:
        ch1_list.append(ch1[r])
        ch2_list.append(ch2[r])

    j = 0; i=0
    for s in ch2:
        if s not in ch1_list:
            off_spring_1[j] = s
        else:
            off_spring_1[j] = ch1_list[i]
            i += 1
        j += 1

    j = 0; i=0
    for s in ch1:
        if s not in ch2_list:
            off_spring_2[j] = s
        else:
            off_spring_2[j] = ch2_list[i]
            i += 1
        j += 1

    return off_spring_1,off_spring_2
########################################################################################################
def MPMX_cross_over(ch1, ch2): #MPMX: Modified Partially-Mapped Crossover
    k = len(ch1)
    random_point_1 = random.randrange(0, k - 1)
    random_point_2 = random.randrange(0, k - 1)
    while random_point_1 == random_point_2:
        random_point_2 = random.randrange(0, k - 1)
    if random_point_2 < random_point_1:
        random_point_1, random_point_2 = random_point_2, random_point_1
    # print(random_point_1)
    # print(random_point_2)
    off_spring_1 = [-1 for i in range(k)]
    off_spring_2 = [-1 for i in range(k)]

    substring1 = ch1[random_point_1:random_point_2 + 1]
    substring2 = ch2[random_point_1:random_point_2 + 1]
    off_spring_1[random_point_1:random_point_2 + 1]= substring2
    off_spring_2[random_point_1:random_point_2 + 1]= substring1
    remain_ch1 = ch1[0:random_point_1] + ch1[random_point_2 + 1:]
    remain_ch2 = ch2[0:random_point_1] + ch2[random_point_2 + 1:]

    for s in remain_ch1:
        idx = off_spring_1.index(-1)
        if s not in substring2:
            off_spring_1[idx] = s
        else:
            off_spring_1[idx] = -2

    for s in remain_ch2:
        idx = off_spring_2.index(-1)
        if s not in substring1:
            off_spring_2[idx] = s
        else:
            off_spring_2[idx] = -2

    set1 = list(set(remain_ch2).difference(set(off_spring_1)))
    set2 = list(set(remain_ch1).difference(set(off_spring_2)))
    # print(off_spring_1, off_spring_2)
    for idx in range(len(off_spring_1)):
        if off_spring_1[idx] == -2:
            a = random.choice(set1)
            idx_a = set1.index(a)
            set1.pop(idx_a)
            off_spring_1[idx] = a

    for idx in range(len(off_spring_2)):
        if off_spring_2[idx] == -2:
            a = random.choice(set2)
            idx_a = set2.index(a)
            set2.pop(idx_a)
            off_spring_2[idx] = a

    return off_spring_1,off_spring_2
########################################################################################################
def MPX_cross_over(ch1, ch2): #Maximal Preservation crossover(MPX)
    k = len(ch1)
    random_point = random.randrange(1, 1 + k//2)
    # print(random_point)
    li1 = ch1[0:random_point]
    remain_ch2 = [i for i in ch2 if i not in li1]

    li2 = ch2[0:random_point]
    remain_ch1 = [i for i in ch1 if i not in li2]

    off_spring_1 = (li1 + remain_ch2)[0:k]
    off_spring_2 = (li2 + remain_ch1)[0:k]

    return off_spring_1,off_spring_2