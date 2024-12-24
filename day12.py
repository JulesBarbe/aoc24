from collections import deque, defaultdict

# bfs, add one to area on encountering new of group, add 1 to perimeter per neighbor attempted when not in group
def problem1(garden):
    n = len(garden)
    m = len(garden[0])
    res = 0
    explored = set()
    for g_row, line in enumerate(garden):
        for g_col, plot in enumerate(line):
            if (g_row, g_col) in explored:
                continue
            area, perim = 0, 0
            queue = deque()
            queue.append((g_row, g_col))
            explored.add((g_row, g_col))

            while queue:
                row, col = queue.popleft()
                # print((row, col), garden[row][col])
                area += 1

                if row > 0 and garden[row-1][col] == plot and (row-1, col) not in explored:
                    queue.append((row-1, col))
                    explored.add((row-1, col))
                elif row == 0 or garden[row-1][col] != plot:
                    # print('p up')
                    perim += 1

                if row < n-1 and garden[row+1][col] == plot and (row+1, col) not in explored:
                    queue.append((row+1, col))
                    explored.add((row+1, col))
                elif row == n-1 or garden[row+1][col] != plot:
                    perim += 1
                    # print('p down')

                if col > 0 and garden[row][col-1] == plot and (row, col-1) not in explored:
                    queue.append((row, col-1))
                    explored.add((row, col-1))
                elif col == 0 or garden[row][col-1] != plot:
                    perim += 1
                    # print('p left')

                if col < m-1 and garden[row][col+1] == plot and (row, col+1) not in explored:
                    queue.append((row, col+1))
                    explored.add((row, col+1))
                elif col == m-1 or garden[row][col+1] != plot:
                    perim +=1 
                    # print('p right')
                    
            # print(explored)
            # print(area, perim)
            res += area * perim

    print(res)

def problem2(garden):
    n = len(garden)
    m = len(garden[0])
    res = 0
    explored = set()
    for g_row, line in enumerate(garden):
        for g_col, plot in enumerate(line):
            if (g_row, g_col) in explored:
                continue
            area = 0
            sides_u = defaultdict(list)
            sides_d = defaultdict(list)
            sides_l = defaultdict(list)
            sides_r = defaultdict(list)

            queue = deque()
            queue.append((g_row, g_col))
            explored.add((g_row, g_col))

            while queue:
                row, col = queue.popleft()
                # print((row, col), garden[row][col])
                area += 1

                if row > 0 and garden[row-1][col] == plot and (row-1, col) not in explored:
                    queue.append((row-1, col))
                    explored.add((row-1, col))
                elif row == 0 or garden[row-1][col] != plot:
                    sides_u[row-1].append(col)

                if row < n-1 and garden[row+1][col] == plot and (row+1, col) not in explored:
                    queue.append((row+1, col))
                    explored.add((row+1, col))
                elif row == n-1 or garden[row+1][col] != plot:
                    sides_d[row+1].append(col)

                if col > 0 and garden[row][col-1] == plot and (row, col-1) not in explored:
                    queue.append((row, col-1))
                    explored.add((row, col-1))
                elif col == 0 or garden[row][col-1] != plot:
                    sides_l[col-1].append(row)

                if col < m-1 and garden[row][col+1] == plot and (row, col+1) not in explored:
                    queue.append((row, col+1))
                    explored.add((row, col+1))
                elif col == m-1 or garden[row][col+1] != plot:
                    sides_r[col+1].append(row)

            num_sides = 0
            for row in sides_u.values():
                row.sort()
                num_sides += 1
                for u1, u2 in zip(row, row[1:]):
                    if u2 != u1 + 1:
                        num_sides += 1
            for row in sides_d.values():
                row.sort()
                num_sides += 1
                for d1, d2 in zip(row, row[1:]):
                    if d2 != d1 + 1:
                        num_sides += 1
            for row in sides_l.values():
                row.sort()
                num_sides += 1

                for d1, d2 in zip(row, row[1:]):
                    if d2 != d1 + 1:
                        num_sides += 1
            for row in sides_r.values():
                row.sort()
                num_sides += 1

                for d1, d2 in zip(row, row[1:]):
                    if d2 != d1 + 1:
                        num_sides += 1
            res += area * num_sides
    print(res)
            
if __name__ == "__main__":
    with open("day12.txt", 'r') as file:
        data = file.read().splitlines()
        problem1(data)
        problem2(data)