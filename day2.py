def problem1(reports):
    count = 0
    for report in reports:
        levels = [int(x) for x in report.split()]
        good = True
        inc = (levels[1] > levels[0])
        diff = abs(levels[1] - levels[0])
        if diff < 1 or diff > 3:
            continue
        for i, level in enumerate(levels[1:]):
            diff = abs(level - levels[i])
            if diff == 0 or diff > 3:
                good = False
            elif inc and level < levels[i]:
                good = False
            elif (not inc) and  level > levels[i]:
                good = False
        if good:
            count += 1
    print(count)

def problem2(reports):
    count = 0
    for report in reports:
        # full levels
        levels = [int(x) for x in report.split()]
        good = True
        inc = (levels[1] > levels[0])
        diff = abs(levels[1] - levels[0])
        if diff < 1 or diff > 3:
            good = False
        for i, level in enumerate(levels[1:]):
            diff = abs(level - levels[i])
            if diff == 0 or diff > 3:
                good = False
            elif inc and level < levels[i]:
                good = False
            elif (not inc) and  level > levels[i]:
                good = False
        if good:
            count += 1
        # - 1 level
        else:
            for j in range(len(levels)):
                new_levels = [x for (i, x) in enumerate(levels) if i != j]
                good = True
                inc = (new_levels[1] > new_levels[0])
                diff = abs(new_levels[1] - new_levels[0])
                if diff < 1 or diff > 3:
                    continue
                for i, level in enumerate(new_levels[1:]):
                    diff = abs(level - new_levels[i])
                    if diff == 0 or diff > 3:
                        good = False
                    elif inc and level < new_levels[i]:
                        good = False
                    elif (not inc) and  level > new_levels[i]:
                        good = False
                if good:
                    count += 1
                    break
    print(count)

if __name__ == "__main__":
    with open("day2.txt", 'r') as file:
        lines = file.read().splitlines()
        problem1(lines)
        problem2(lines)
        
        
        
        
        