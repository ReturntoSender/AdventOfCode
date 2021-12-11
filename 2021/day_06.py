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
    super_long_cycle = 128
    for i in range(super_long_cycle):
        new_data = []
        for fish in data:
            if fish == 0:
                fish = 6
                data.append(9)
            else:
                fish -= 1
            new_data.append(fish)
        data = new_data
        print(f'Tag {i+1} - {len(new_data)}')
    return len(data)


#answer_1 = solve(read_input('input_06.txt'))
answer_2 = solve2(read_input("input_klein_06.txt"))


#print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
