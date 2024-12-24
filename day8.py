from collections import defaultdict
from itertools import combinations

def problem1(lines):
    # store all antenna positions
    antennas = defaultdict(list)
    n = len(lines)
    m = len(lines[0])
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                antennas[char].append((i, j))

    # assign 2 anti-node locations for every pair of antennas of the same frequency
    antinode_locations = set()
    for frequency, locations in antennas.items():
        for antenna1, antenna2 in combinations(locations, 2):
            dist_x = antenna2[0] - antenna1[0]
            dist_y = antenna2[1] - antenna1[1]
            node1 = (antenna2[0] + dist_x, antenna2[1] + dist_y)
            node2 = (antenna1[0] - dist_x, antenna1[1] - dist_y)
            if 0 <= node1[0] < n and 0 <= node1[1] < m:
                antinode_locations.add(node1)
            if 0 <= node2[0] < n and 0 <= node2[1] < m:
                antinode_locations.add(node2)

    print(f"Unique antinode locations: {len(antinode_locations)}")

def problem2(lines):
    # store all antenna positions
    antennas = defaultdict(list)
    n = len(lines)
    m = len(lines[0])
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                antennas[char].append((i, j))

    # assign anti-node locations to every position in the line created by every pair of antennas of the same frequency
    antinode_locations = set()
    for frequency, locations in antennas.items():
        for antenna1, antenna2 in combinations(locations, 2):
            dist_x = antenna2[0] - antenna1[0]
            dist_y = antenna2[1] - antenna1[1]

            # line in first direction
            curr_x, curr_y = antenna2[0], antenna2[1]
            while 0 <= curr_x < n and 0 <= curr_y < m:
                antinode_locations.add((curr_x, curr_y))
                curr_x += dist_x
                curr_y += dist_y
            
            # second direction
            curr_x, curr_y = antenna1[0], antenna1[1]
            while 0 <= curr_x < n and 0 <= curr_y < m:
                antinode_locations.add((curr_x, curr_y))
                curr_x -= dist_x
                curr_y -= dist_y

    print(f"Unique antinode locations: {len(antinode_locations)}")
    
if __name__ == "__main__":
    with open("day8.txt", 'r') as file:
        lines = file.read().splitlines()
        problem1(lines)
        problem2(lines)