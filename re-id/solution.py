def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return False
    return True


def solution(n):
    string = ""
    cur = 0
    while len(string) < 10005:
        if is_prime(cur):
            string += str(cur)
        cur += 1
    return string[n : n + 5]


print(solution(0))
print(solution(3))
