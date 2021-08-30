from itertools import permutations


def solution(l):
    maxi = 0
    for length in range(len(l), 0, -1):
        for candidate in permutations(l, length):
            cur = sum(
                [
                    candidate[i] * 10 ** (len(candidate) - 1 - i)
                    for i in range(len(candidate))
                ]
            )
            if cur % 3 == 0:
                maxi = max(maxi, cur)
        if maxi:
            return maxi
    return 0


print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))
