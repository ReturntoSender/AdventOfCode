def read_input(file):
    with open(file) as f:
        data = f.read().strip().split(',')
        data = [int(fish) for fish in data]
    return data


def solve(data):
    short_cycle = 18
    long_cycle = 80
    for i in range(long_cycle):
        new_data = []
        for fish in data:
            if fish == 0:
                fish = 6
                data.append(9)
            else:
                fish -= 1
            new_data.append(fish)
        data = new_data

    return len(data)


def solve2(data):
    stats = []
    short_cycle = 10
    long_cycle = 256
    for i in range(short_cycle):
        new_data = []
        for fish in data:
            if fish == 0:
                fish = 6
                data.append(9)
            else:
                fish -= 1
            new_data.append(fish)
        data = new_data

        stats.append(len(data))
    for i in range(long_cycle - short_cycle):
        stats.append(stats[-7] + stats[-9])
    return stats[-1]


answer_1 = solve(read_input('input_06.txt'))
answer_2 = solve2(read_input("input_06.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
