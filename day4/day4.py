def problem1(lines):
    n = len(lines)
    m = len(lines[0])
    count = 0
    for i in range(n):
        for j in range(m):
            char = lines[i][j]
            if char == "X":
                count += check(i, j)
    print(count)

def check(i, j):
    count = 0
    try: 
        if j >= 3 and lines[i][j-1] + lines[i][j-2] + lines[i][j-3] == "MAS":
            count += 1
    except IndexError:
        pass
    try:
        if lines[i][j+1] + lines[i][j+2] + lines[i][j+3] == "MAS":
            count += 1
    except IndexError:
        pass
    try:
        if i >= 3 and lines[i-1][j] + lines[i-2][j] + lines[i-3][j] == "MAS":
            count += 1
    except IndexError:
        pass
    try:
        if lines[i+1][j] + lines[i+2][j] + lines[i+3][j] == "MAS":
            count += 1
    except IndexError:
        pass
    try:
        if i >= 3 and j >= 3 and lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3] == "MAS":
            count += 1
    except IndexError:
        pass
    try:
        if i >= 3 and lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3] == "MAS":
            count += 1
    except IndexError:
        pass
    try:
        if j >= 3 and lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] == "MAS":
            count += 1
    except IndexError:
        pass
    try:
        if lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] == "MAS":
            count += 1
    except IndexError:
        pass
    return count

def problem2(lines):
    n = len(lines)
    m = len(lines[0])
    count = 0
    for i in range(n):
        for j in range(m):
            char = lines[i][j]
            if char == "A" and 1 <= i < n-1 and 1 <= j < m-1:
                count += check2(i, j)
    print(count)

def check2(i, j):
    return 1 if (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M' or lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S') and (lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M' or lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S') else 0
    
    

if __name__ == "__main__":
    with open("day4.txt", 'r') as file:
        lines = file.read().splitlines()
        problem1(lines)
        problem2(lines)