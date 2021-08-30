def solution(h, q):
    mapping = {}

    def post_order(v, h):
        if h == 1:
            return v + 1
        left = post_order(v, h - 1)
        right = post_order(left, h - 1)
        mapping[left] = right + 1
        mapping[right] = right + 1
        return right + 1

    post_order(0, h)
    return [mapping.get(i, -1) for i in q]


print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))
