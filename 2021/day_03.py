def read_input(file):
    with open(file) as f:
        data = [line.strip() for line in f]
    return data


def solve(data):
    result = ''
    for i in range(len(data[0])):
        pos = []
        for line in data:
            if line[i] == '1':
                pos.append(1)
            else:
                pos.append(0)
        if sum(pos) < len(pos) / 2:
            result += str(1)
        else:
            result += str(0)

    gamma_rate = int(result, 2)
    epsilon_rate = (2**len(result)-1) - gamma_rate

    return gamma_rate * epsilon_rate


def solve2(data):
    result = int(sort_out(data, 'ogr'), 2) * int(sort_out(data, 'cor'), 2)
    return result


def sort_out(data, rating):

    for i in range(len(data[0])):
        pos = []
        lst1 = []
        lst0 = []
        for line in data:
            if line[i] == '1':
                pos.append(1)
                lst1.append(line)
            else:
                pos.append(0)
                lst0.append(line)
        if sum(pos) >= len(pos) / 2:
            if rating == 'ogr':
                data = lst1
            else:
                data = lst0
        else:
            if rating == 'ogr':
                data = lst0
            else:
                data = lst1
        if len(data) == 1:
            return data[0]

    return sort_out(data, rating)


answer_1 = solve(read_input("input_03.txt"))
answer_2 = solve2(read_input("input_03.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
