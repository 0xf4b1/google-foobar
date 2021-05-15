def solution(map):
    walls = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                walls.append((i, j))

    sols = []
    for wx, wy in walls:
        map[wx][wy] = 0
        lengths = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
        candidates = [(0, 0)]
        found = False
        while len(candidates) > 0 and not found:
            next = []
            for pos in candidates:
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    x, y = pos
                    if (
                        0 <= x + dx < len(map)
                        and 0 <= y + dy < len(map[0])
                        and map[x + dx][y + dy] == 0
                        and lengths[x + dx][y + dy] == 0
                    ):
                        if x + dx == len(map) - 1 and y + dy == len(map[0]) - 1:
                            sols.append(lengths[x][y] + 2)
                            found = True
                        lengths[x + dx][y + dy] = lengths[x][y] + 1
                        next.append((x + dx, y + dy))
            candidates = next

        map[wx][wy] = 1

    return min(sols)


print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))

print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
