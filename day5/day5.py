from collections import defaultdict
def problem1(orderings, updates):
    d = defaultdict(list)
    for ordering in orderings:
        ordering = [int(n) for n in ordering.split("|")]
        d[ordering[0]].append(ordering[1])
    tot = 0
    tot_2 = 0
    for update in updates:
        good = True
        s = set()
        update = [int(n) for n in update.split(',')]
        for u in update:
            s.add(u)
            for v in d[u]:
                if v in s:
                    good = False
                    break
        if good:
            tot += update[len(update) // 2]
        else:
            counts = {v: 0 for v in s}
            for u in update:
                for v in d[u]:
                    if v in s:
                        counts[v] += 1
            count_groups = defaultdict(list)
            for page, count in counts.items():
                count_groups[count].append(page)
            sorted_counts = sorted(count_groups.items(), key=lambda item: item[0])
            res = [x[1][0] for x in sorted_counts]
            tot_2 += res[len(res) // 2]
    return tot, tot_2

if __name__ == "__main__":
    with open('day5.txt', 'r') as file:
        lines = file.read()
        orderings, updates = lines.split("\n\n")
        res1, res2 = problem1(orderings.splitlines(), updates.splitlines())
        print("result 1: ", res1)
        print("result 2: ", res2)

        
        
