def read_input(file):
    with open(file) as f:
        data = [line for line in f]
    return data


def solve(data):
    aim = x = y = 0
    for line in data:
        direction, distance = line.split()
        if direction == 'forward':
            x += int(distance)
        elif direction == 'down':
            y += int(distance)
        elif direction == 'up':
            y -= int(distance)
    product = x * y
    return product


def solve2(data):
    aim = x = y = 0
    for line in data:
        direction, distance = line.split()
        if direction == 'forward':
            x += int(distance)
            y += aim * int(distance)
        elif direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)
    product = x * y
    return product


answer_1 = solve(read_input("input_02.txt"))
answer_2 = solve2(read_input("input_02.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
