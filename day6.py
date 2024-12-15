import copy

def problem1(merp):
    n = len(merp)
    m = len(merp[0])
    row, col = 0, 0
    for r in range(n):
        for c in range(m):
            if merp[r][c] == '^':
                row, col = r, c
    encountered = {}
    count = 1
    count2 = 0
    merp2 = copy.deepcopy(merp)
    p = '^'
    while 0 <= row < n and 0 <= col < m:
        if merp[row][col] == '.':
            count += 1
        match p:
            case '^':
                if row > 0 and merp[row-1][col] == '#':
                    merp[row][col] = '+'
                    p = '>'
                    encountered[(col, '^')] = row - 1
                    col += 1
                else:
                    if (row, '>') in encountered:
                        hitcol = encountered[(row, '>')]
                        curcol = col
                        print(f"v point {(row, col)}, going to hitrow {hitrow}")
                        while curcol < hitcol:
                            if merp[row][curcol] == '#':
                                break
                            curcol += 1
                        else:
                            merp2[row-1][col] = 'O'
                            count2 += 1
                    merp[row][col] = '|'
                    row -= 1
            case '>':
                if col < m-1 and merp[row][col+1] == '#':
                    merp[row][col] = '+'
                    p = 'v'
                    encountered[(row, '>')] = col + 1
                    row += 1
                else:
                    if (col, 'v') in encountered:
                        hitrow = encountered[(col, 'v')]
                        currow = row
                        print(f"v point {(row, col)}, going to hitrow {hitrow}")
                        while currow < hitrow:
                            if merp[currow][col] == '#':
                                break
                            currow += 1
                        else:
                            merp2[row][col+1] = 'O'
                            count2 += 1
                    merp[row][col] = '-'
                    col += 1
            case 'v':
                if row < n-1 and merp[row+1][col] == '#':
                    merp[row][col] = '+'
                    p = '<'
                    encountered[(col, 'v')] = row + 1
                    col -= 1
                else:
                    if (row, '<') in encountered:
                        hitcol = encountered[(row, '<')]
                        curcol = col
                        print(f"< point {(row, col)}, going to hitrow {hitrow}")
                        while curcol > hitcol:
                            if merp[row][curcol] == '#':
                                break
                            curcol -= 1
                        else:
                            merp2[row+1][col] = 'O'
                            count2 += 1

                    merp[row][col] = '|'
                    row += 1
            case '<':
                if col > 0 and merp[row][col-1] == '#':
                    merp[row][col] = '+'
                    p = '^'
                    encountered[(row, '<')] = col - 1
                    row -= 1
                else:
                    if (col, '^') in encountered:
                        hitrow = encountered[(col, '^')]
                        currow = row
                        print(f"^ point {(row, col)}, going to hitrow {hitrow}")
                        while currow > hitrow:
                            if merp[currow][col] == '#':
                                break
                            currow -= 1
                        else:
                            merp2[row][col-1] = 'O'
                            count2 += 1
                    merp[row][col] = '-'
                    col -= 1


    with open('dayy6.txt', 'w') as file:
        s = ""
        for l in merp:
            s += ''.join(l) + '\n'
        file.write(s)
    with open('dayyy6.txt', 'w') as file:
        s = ""
        for l in merp2:
            s += ''.join(l) + '\n'
        file.write(s)
    return count, count2


if __name__ == "__main__":
    with open('day6.txt', 'r') as file:
        merp = [list(l) for  l in file.read().splitlines()]
        res1, res2 = problem1(merp)
        print("result 1: ", res1)
        print("result 2: ", res2)