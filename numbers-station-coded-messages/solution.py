def solution(l, t):
    for i in range(len(l)):
        for j in range(len(l) - i + 1):
            if sum(l[i : i + j]) == t:
                return [i, i + j - 1]
    return [-1, -1]


print(solution([4, 3, 10, 2, 8], 12))
