import timeit
def problem1(lines):
    sum = 0
    for line in lines:
        res, values = line.split(':')
        res = int(res)
        values = [int(num) for num in values.split()]
        n = len(values)
        stack = []
        curr_index = 1
        curr_val = values[0]
        stack.append((curr_index, curr_val, ""))
        while stack:
            curr = stack.pop()
            curr_index = curr[0]
            if curr_index >= n:
                continue
            curr_val = curr[1]
            new_val = values[curr_index]
            res1 = curr_val + new_val
            res2 = curr_val * new_val
            if res in (res1, res2) and curr_index == n-1:
                sum += res
                break
            curr_op = curr[2]
            if res1 <= res:
                stack.append((curr_index + 1, res1, curr_op + f"+{new_val}"))
            if res2 <= res:
                stack.append((curr_index + 1, res2, curr_op + f"*{new_val}"))
    return sum

def problem2(lines):
    sum = 0
    for line in lines:
        res, values = line.split(':')
        res = int(res)
        values = [int(num) for num in values.split()]
        n = len(values)
        stack = []
        curr_index = 1
        curr_val = values[0]
        stack.append((curr_index, curr_val, ""))
        while stack:
            curr = stack.pop()
            curr_index = curr[0]
            if curr_index >= n:
                continue
            curr_val = curr[1]
            new_val = values[curr_index]
            res1 = curr_val + new_val
            res2 = curr_val * new_val
            res3 = int(str(curr_val) + str(new_val))
            if res in (res1, res2, res3) and curr_index == n-1:
                sum += res
                break
            curr_op = curr[2]
            if res1 <= res:
                stack.append((curr_index + 1, res1, curr_op + f"+{new_val}"))
            if res2 <= res:
                stack.append((curr_index + 1, res2, curr_op + f"*{new_val}"))
            if res3 <= res:
                stack.append((curr_index + 1, res3, curr_op + f"||{new_val}"))
    return sum

    #     res1 = values[0] + values[1]
    #     res2 = values[0] * values[1]
    #     res3 = int(str(values[0]) + str(values[1]))
    #     if res in (res1, res2, res3) and len(values) == 2:
    #         sum += res
    #         continue
    #     # (next value index, result, operation up to now)
    #     stack.append((2, res1, f"{values[0]}+{values[1]}"))
    #     stack.append((2, res2, f"{values[0]}*{values[1]}"))
    #     stack.append((2, res3, f"{values[0]}||{values[1]}"))
    #     while stack:
    #         curr = stack.pop()
    #         curr_index = curr[0]
    #         curr_res = curr[1]
    #         if curr_index >= n:
    #             continue
    #         new_val = values[curr_index]
    #         res1 = curr_res + new_val
    #         res2 = curr_res * new_val
    #         res3 = int(str(curr_res) + str(new_val))
    #         if res in (res1, res2, res3) and curr_index == n-1:
    #             # print(f"{curr} -> {new_val}, {len(values)}")
    #             sum += res
    #             break
    #         if res1 < res:
    #             stack.append((curr_index + 1, res1, curr[2] + f"+{new_val}"))
    #         if res2 < res:
    #             stack.append((curr_index + 1, res2, curr[2] + f"*{new_val}"))
    #         if res3 < res:
    #             stack.append((curr_index + 1, res3, curr[2] + f"||{new_val}"))
    # return sum


if __name__ == "__main__":
    with open('day7.txt', 'r') as file:
        lines = file.read().splitlines()
    print("Result 1: ", problem1(lines))
    print("Result 2: ", problem2(lines))
    