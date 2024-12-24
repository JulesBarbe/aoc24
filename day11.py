from collections import Counter

def problem1(stones, blinks):
    for i in range(blinks):
        new_stones = []
        for stone in stones:
            if int(stone) == 0:
                new_stones.append('1')
            elif len(stone) % 2 == 0:
                new_stones.append(str(int(stone[:len(stone)//2])))
                new_stones.append(str(int(stone[len(stone)//2:])))
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones
    print(len(stones))

def problem2(stones, blinks):
    stone_count = Counter(stones)
    for i in range(blinks):
        next_stone_count = Counter()
        for stone_str, count in stone_count.items():
            stone_length = len(stone_str)
            stone_int = int(stone_str)
            if stone_int == 0:
                next_stone_count['1'] += count
            elif stone_length % 2 == 0:
                x = stone_length // 2
                next_stone_count[str(int(stone_str[:x]))] += count
                next_stone_count[str(int(stone_str[x:]))] += count
            else:
                next_stone_count[str(stone_int * 2024)] += count
        stone_count = next_stone_count
    print(sum(stone_count.values()))
            
if __name__ == "__main__":
    with open("day11.txt", 'r') as file:
        data = file.read().split()
        problem1(data, 25)
        problem2(data, 75)