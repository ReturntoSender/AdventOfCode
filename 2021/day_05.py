def read_input(file):
    with open(file) as f:
        line = f.read().split('\n')
        coords = [cord.split(' -> ') for cord in line]
    return coords


def solve(data):
    return data


def solve2(data):
    return data


answer_1 = solve(read_input("input_klein_05.txt"))
#answer_2 = solve2(*read_input("input_klein_05.txt"))


print(f"Die Loesung 1: {answer_1}")
#print(f"Die Loesung 2: {answer_2}")
