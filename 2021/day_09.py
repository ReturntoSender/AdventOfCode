def read_input(file):
    with open(file) as f:
        data = f.read()
        data = [[x.split()] for x in data.split('\n')]
        return data


def solve(data):
    return data


def solve2(data):
    return -1


answer_1 = solve(read_input('input_klein_09.txt'))
answer_2 = solve2(read_input('input_klein_09.txt'))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
