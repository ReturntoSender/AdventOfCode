def read_input(file):
    with open(file) as f:
        data = f.read().strip().split(',')
        data = [int(horizon) for horizon in data]
    return data


def solve(data):
    minimum = min(data)
    maximum = max(data)
    counter = []
    for i in range(maximum-minimum):
        count = 0
        for height in data:
            count += abs(maximum - i - height)
        counter.append(count)
    return min(counter)


def solve2(data):
    minimum = min(data)
    maximum = max(data)
    counter = []
    for i in range(maximum-minimum):
        count = 0
        for height in data:
            difference = abs(maximum - i - height)
            fuel = int((difference * (difference + 1)) / 2)
            count += fuel
        counter.append(count)
    return min(counter)


answer_1 = solve(read_input('input_07.txt'))
answer_2 = solve2(read_input("input_07.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
