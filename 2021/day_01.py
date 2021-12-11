def read_input(file):
    with open(file) as f:
        data = [int(line.strip()) for line in f]
    return data


def solve(data):
    count = -1
    vorher = 0
    for z in data:
        if vorher < z:
            count += 1
        vorher = z
    return count


def solve2(data):
    count = -1
    vorher = 0
    window = []
    for z in data:
        window.append(z)
        if len(window) < 3:
            continue
        if sum(window) > vorher:
            count += 1
        vorher = sum(window)
        window.pop(0)

    return count


answer_1 = solve(read_input("input_01.txt"))
answer_2 = solve2(read_input("input_01.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
