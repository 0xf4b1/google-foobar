def solution(n):
    val = int(n)

    steps = 0
    while val > 1:
        if val % 2 == 1:
            if bin(val + 1).count("1") <= bin(val - 1).count("1") and val != 3:
                val += 1
            else:
                val -= 1
        else:
            val /= 2

        steps += 1

    return steps


print(solution(15))
