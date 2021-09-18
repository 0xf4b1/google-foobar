def solution(x, y):
    m = int(x)
    f = int(y)
    cycles = 0
    while m > 1 or f > 1:
        if m == f:
            break
        if f > m:
            count = f // m
            if m == 1:
                count -= 1
            f -= m * count
            if f == 0:
                break
        else:
            count = m // f
            if f == 1:
                count -= 1
            m -= f * count
            if m == 0:
                break
        cycles += count

    return str(cycles) if m == 1 and f == 1 else "impossible"


print(solution("4", "7"))
print(solution("2", "1"))
