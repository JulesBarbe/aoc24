with open("day1.txt", 'r') as lists:
    # x = lists.read().splitlines()
    # l1, l2 = [], []
    # for line in x:
    #     line = line.split()
    #     l1.append(int(line[0]))
    #     l2.append(int(line[1]))
    # l1.sort()
    # l2.sort()
    # r = sum([abs(x1 - x2) for (x1, x2) in zip(l1, l2)])
    # print(r)
    lines = lists.read().splitlines()
    d = {}
    s = set()
    for line in lines:
        line = line.split()
        l, r = int(line[0]), int(line[1])
        print(l, r)
        s.add(l)
        d[r] = d.get(r, 0) + 1
            
    print(sum([k * v for (k, v) in d.items() if k in s]))



  