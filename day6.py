from collections import defaultdict
import copy

def next_pos(row, col, direction):
    match direction:
        case '^':
            return (row-1, col)
        case '>':
            return (row, col+1)
        case 'v':
            return (row+1, col)
        case '<':
            return (row, col-1)

def turn(direction):
    match direction:
        case '^':
            return ('>')
        case '>':
            return ('v')
        case 'v':
            return ('<')
        case '<':
            return ('^')
        
def map_symbol(previous_dirs, curr_dir):
    if curr_dir in ('^', 'v'):
        return '+' if ('>' in previous_dirs or '<' in previous_dirs) else '|'
    else:
        return '+' if ('^' in previous_dirs or 'v' in previous_dirs) else '-'
        
def curr_pos_loops(start_row, start_col, start_dir, map, max_row, max_col, obst_row, obst_col):
    curr_dir = turn(start_dir)
    row, col = start_row, start_col
    travels = defaultdict(set)
    debug_map = copy.deepcopy(merp)
    debug_map[obst_row][obst_col] = 'O'
    while True:
        debug_map[row][col] = curr_dir
        if curr_dir in travels[(row, col)] or (row, col, curr_dir) == (start_row, start_col, start_dir):
            print(f"Found loop with obstacle at {obst_row}, {obst_col}")
            with open('debug_map.txt', 'w') as file:
                s = ""
                for l in debug_map:
                    s += ''.join(l) + '\n'
                file.write(s)
            return True
        travels[(row, col)].add(curr_dir)
        next_row, next_col = next_pos(row, col, curr_dir)
        if next_row < 0 or next_col < 0 or next_row >= max_row or next_col >= max_col:
            return False
        if map[next_row][next_col] == '#' or (next_row, next_col) == (obst_row, obst_col):
            row, col, curr_dir = row, col, turn(curr_dir)
        else:
            row, col = next_row, next_col

def solve(merp):
    n = len(merp)
    m = len(merp)
    start_row, start_col = 0, 0 
    travels = defaultdict(set)
    guard_path = []

    # find starting position
    for r in range(n):
        for c in range(m):
            if merp[r][c] == '^':
                start_row, start_col = r, c
                merp[r][c] = '.'

    # simulate guard path 
    row, col, curr_dir = start_row, start_col, '^'
    while True:
        guard_path.append((row, col, curr_dir))
        travel_dirs = travels[(row, col)]
        merp[row][col] = map_symbol(travel_dirs, curr_dir)
        travels[(row, col)].add(curr_dir)
        next_row, next_col = next_pos(row, col, curr_dir)
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m:
            break
        if merp[next_row][next_col] == '#':
            row, col, curr_dir = row, col, turn(curr_dir)
        else:
            row, col = next_row, next_col

    # result for problem 1, and visualized guard path
    print(f"Guard traveled through {len(travels)} distinct positions")
    print(f"Guard path visualized in guard_path.txt")
    with open('guard_path.txt', 'w') as file:
        merp[start_row][start_col] = '^'
        s = ""
        for l in merp:
            s += ''.join(l) + '\n'
        file.write(s)

    print(guard_path)
    # try placing an obstacle at every position through guard path
    row, col, curr_dir = start_row, start_col, '^'
    obstacle_count = 0
    attempted = set()
    obstacle_merp = copy.deepcopy(merp)
    for row, col, curr_dir in guard_path:
        next_row, next_col = next_pos(row, col, curr_dir)
        # obstacle is in the map, is not already an obstacle, was not already attempted, is not at the guard's starting position, and causes a loop.
        if 0 <= next_row < n and 0 <= next_col < m and merp[next_row][next_col] != '#' and (next_row, next_col) not in attempted and (next_row, next_col) != (start_row, start_col) and curr_pos_loops(row, col, curr_dir, merp, n, m, next_row, next_col):
            obstacle_count += 1
            obstacle_merp[next_row][next_col] = 'O'
        attempted.add((next_row, next_col))

    print(f"{obstacle_count} positions in the map can lead to a loop.")
    print(f"All looping obstacle positions visualized in loop_obstacles.txt")
    with open('loop_obstacles.txt', 'w') as file:
        obstacle_merp[start_row][start_col] = '^'
        s = ""
        for l in obstacle_merp:
            s += ''.join(l) + '\n'
        file.write(s)
        
if __name__ == "__main__":
    with open('day6.txt', 'r') as file:
        merp = [list(l) for  l in file.read().splitlines()]
        solve(merp)