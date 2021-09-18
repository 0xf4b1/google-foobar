def xor_row(begin, end):
    if end - begin == 0:
        return 0

    return reduce(lambda x, y: x ^ y, range(begin, end))


def solution(start, length):
    row = []
    for h in range(length):
        begin = h * length + start
        end = h * length + start + length - h
        row.append(xor_row(begin, begin / 4 * 4 + 4) ^ xor_row(end / 4 * 4, end))

    return reduce(lambda x, y: x ^ y, row)


print(solution(0, 3))
print(solution(17, 4))
