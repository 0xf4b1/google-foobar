def solution(x, y):
    x.sort()
    y.sort()

    first = False
    if len(x) > len(y):
        first = True

    for i in range(len(y) if first else len(x)):
        if x[i] != y[i]:
            return x[i] if first else y[i]

    return x[-1] if first else y[-1]


print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))
