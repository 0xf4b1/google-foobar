def compare(x, y):
    first = [int(i) for i in x.split(".")]
    second = [int(i) for i in y.split(".")]

    for i in range(min(len(first), len(second))):
        if first[i] < second[i]:
            return -1
        elif first[i] > second[i]:
            return 1

    if len(x) < len(y):
        return -1
    else:
        return 1


def solution(l):
    return sorted(l, cmp=compare)


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
