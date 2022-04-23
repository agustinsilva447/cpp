# output = [-1, 2, -1, 2]

import math

def solution(list_b, queries):
    output = [0] * len(queries)
    for j,i in enumerate(queries):
        if i[0] == 1:
            list_b[i[1]] = True
            output[j] = i[1]
        elif i[0] == 2:
            k_min = min(len(list_b)-i[1], i[1])
            while k_min>0:
                if (list_b[k_min] == True):
                    v_min = math.abs(len(list_b)-i[1])
                    k_min = 0
                k_min -= 1

            k_max = max(len(list_b)-i[1], i[1])
            while k_max<len(queries):
                if (list_b[k_max] == True):
                    v_max = math.abs(len(list_b)-i[1])
                    k_max = len(queries)
                k_max += 1
        
            output[j] = min(v_min, v_max)
    return output

N = 5
list_b = [False] * N
queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
print(solution(list_b, queries))