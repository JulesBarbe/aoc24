
# 1 pass 2 pointer solution: O(n) time O(1) space (except for debug string)
def problem1(disk_map):
    left, right = 0, len(disk_map) - 1
    is_file_left, is_file_right = True, right % 2 == 0
    space_idx, checksum = 0, 0
    debug_str = []
    while left <= right:
        # print(f"left {left} right {right}")
        if is_file_left:
            file_size = disk_map[left]
            mem_id = left // 2
            for _ in range(file_size):
                checksum += space_idx * mem_id
                space_idx += 1
                debug_str.append(mem_id)
            # print('l', debug_str)
        else:
            mem_space = disk_map[left]
            # print('mem space: ', mem_space)
            while mem_space > 0 and left < right:
                if is_file_right:
                    file_size = disk_map[right]
                    mem_id = right // 2
                    # print(f"r file size id {mem_id} size {file_size}")
                    while file_size > 0:
                        checksum += space_idx * mem_id
                        space_idx += 1
                        file_size -= 1
                        mem_space -= 1
                        debug_str.append(mem_id)
                        if mem_space == 0:
                            # print('r memory stop', debug_str)
                            disk_map[right] = file_size
                            break
                    else:
                        # print('r next')
                        # print('r', debug_str)
                        right -= 1
                        is_file_right = not is_file_right
                else:
                    # print('r skip')
                    right -= 1
                    is_file_right = not is_file_right
        left += 1
        is_file_left = not is_file_left
    print(checksum)
    # print("".join([str(d) for d in debug_str]))

import heapq
# fuck it tried a cool heap solution but nah
# sorted on leftmost, O(n^2) time, O(n) space
# still feel like O(nlogn) possible with some sort of tree like structure for both leftmost property and size ranges
def problem2(disk_map):
    spaces = []
    debug_str = ['*'] * 100
    mem = {}
    space_idx = 0
    for idx, mem_size in enumerate(disk_map):
        if idx % 2 != 0:
            spaces.append([mem_size, idx, space_idx])
        else:
            mem[idx] = space_idx
        space_idx += mem_size
    checksum = 0
    for idx, file_size in reversed(list((i, n) for i, n in enumerate(disk_map) if i % 2 == 0)):
        mem_idx = mem[idx]
        for space in spaces:
            if space[0] >= file_size and space[1] < idx:
                mem_idx = space[2]
                space[0] -= file_size
                space[2] += file_size
                break
        # debug_str[mem_idx:mem_idx+file_size] = [idx // 2] * file_size
        for i in range(file_size):
            checksum += (idx // 2) * (mem_idx + i)
        # print("".join([str(d) for d in debug_str]))
    print(checksum)

if __name__ == "__main__":
    with open('day9.txt', 'r') as file:
        data = [int(d) for d in file.read()]
        # problem1(data)
        problem2(data)
        