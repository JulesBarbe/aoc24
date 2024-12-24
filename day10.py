def problem1(map):
    n, m = len(map), len(map[0])
    res = 0
    for row, line in enumerate(map):
        for col, height in enumerate(line):
            if height == 0:
                summits = set()
                res += find_next(row, col, 0, map, n, m, summits)
    print(res)

def problem2(map):
    n, m = len(map), len(map[0])
    res = 0
    for row, line in enumerate(map):
        for col, height in enumerate(line):
            if height == 0:
                res += find_next2(row, col, 0, map, n, m)
    print(res)

def find_next(row, col, num, map, n, m, summits):
    res = 0
    if row > 0:
        next = map[row-1][col]
        if next == num + 1:
            if (row-1, col) not in summits and next == 9:
                res += 1
                summits.add((row-1, col))
            else:
                res += find_next(row-1, col, num+1, map, n, m, summits)
    if row < n - 1:
        next = map[row+1][col]
        if next == num + 1:
            if (row+1, col) not in summits and next == 9:
                res += 1
                summits.add((row+1, col))
            else:
                res += find_next(row+1, col, num+1, map, n, m, summits)
    if col > 0:
        next = map[row][col-1]
        if next == num + 1:
            if (row, col-1) not in summits and next == 9:
                res += 1
                summits.add((row, col-1))
            else:
                res += find_next(row, col-1, num+1, map, n, m, summits)
    if col < m - 1:
        next = map[row][col+1]
        if next == num + 1:
            if (row, col+1) not in summits and next == 9:
                res += 1
                summits.add((row, col+1))
            else:
                res += find_next(row, col+1, num+1, map, n, m, summits)
    return res

def find_next2(row, col, num, map, n, m):
    res = 0
    if row > 0:
        next = map[row-1][col]
        if next == num + 1:
            if next == 9:
                res += 1
            else:
                res += find_next2(row-1, col, num+1, map, n, m)
    if row < n - 1:
        next = map[row+1][col]
        if next == num + 1:
            if next == 9:
                res += 1
            else:
                res += find_next2(row+1, col, num+1, map, n, m)
    if col > 0:
        next = map[row][col-1]
        if next == num + 1:
            if next == 9:
                res += 1
            else:
                res += find_next2(row, col-1, num+1, map, n, m)
    if col < m - 1:
        next = map[row][col+1]
        if next == num + 1:
            if next == 9:
                res += 1
            else:
                res += find_next2(row, col+1, num+1, map, n, m)
    return res


if __name__ == "__main__":
    with open("day10.txt", 'r') as file:
        map = [[int(n) for n in l] for l in file.read().splitlines()]
        problem1(map)
        problem2(map)


# could make cool directed graph solution, where nodes are neighbors when they differ by one ...