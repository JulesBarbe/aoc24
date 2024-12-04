def problem1(lines):
    l1, l2 = [], []
    for line in lines:
        line = line.split()
        l1.append(int(line[0]))
        l2.append(int(line[1]))
    l1.sort()
    l2.sort()
    r = sum([abs(x1 - x2) for (x1, x2) in zip(l1, l2)])
    print(r)

def problem2(lines): 
    d = {}
    s = set()
    for line in lines:
        line = line.split()
        l, r = int(line[0]), int(line[1])
        s.add(l)
        d[r] = d.get(r, 0) + 1
            
    print(sum([k * v for (k, v) in d.items() if k in s]))

if __name__ == "__main__":
    with open("day1.txt", 'r') as file:
        lines = file.read().splitlines()
        problem1(lines)
        problem2(lines) 