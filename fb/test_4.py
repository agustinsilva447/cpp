def better_solution(num):
    if num<0:
        return -1
    if num==1:
        return 1
    low = 0
    high = num
    while (low + 1 < high):
        mid = (low + high) // 2
        square = mid ** 2
        if square == num:
            return mid
        elif square < num:
            low = mid 
        else:
            high = mid
    return low 

for i in range(200):
    print(i, better_solution(i))
