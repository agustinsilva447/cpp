def avg_solution(A):
    sol_list = []
    left_i = 0
    righ_i = 0
    tot = sum(A)
    while (left_i < len(A)):
        par = sum(A[left_i:righ_i+1])
        avg_par = par / (righ_i - left_i + 1)

        if (len(A) - (righ_i - left_i + 1)) == 0:
            avg_rem = 0
        else:
            avg_rem = (tot - par)/(len(A) - (righ_i - left_i + 1))

        if avg_par > avg_rem:
            print(avg_par, avg_rem)
            sol_list.append([left_i + 1, righ_i + 1])
            
        righ_i += 1
        if righ_i >= len(A):
            left_i += 1
            righ_i = left_i
    return sol_list

A = [3, 4, 2]
print(A)
print(avg_solution(A))