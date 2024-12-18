import random
import sys

def generate_map(n, m):
    lines = []
    for _ in range(n):
        line = [random.choices(population=['.', '#'], weights=[0.8, 0.2], k=m)][0]
        lines.append(line)
    start_row, start_col = random.randint(0, n-1), random.randint(0, m-1)
    lines[start_row][start_col] = '^'
    return '\n'.join([''.join(line) for line in lines])

def main():
    if len(sys.argv) != 3:
        print("give out only 2 integers")
        return
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    str_map = generate_map(n, m)

    with open("day6_example_map.txt", 'w') as file:
        file.write(str_map)

if __name__ == "__main__":
    main()
