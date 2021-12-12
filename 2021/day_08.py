def read_input(file):
    with open(file) as f:
        data = f.read().strip().split('\n')

    return data


def solve(data):

    lines = []
    digits = [2, 3, 4, 7]
    counter = 0

    for line in data:
        line = (line.split(' | ')[1]).split()
        lines.append(line)
    for line in lines:
        for digit in line:
            if len(digit) in digits:
                counter += 1

    return counter


def sortLength(item):
            return len(item)


def solve2(data):

    lines = []
    digit_list = []

    for line in data:
        wire = line.split(' ')[:10]
        code = line.split(' ')[-4:]        
        wire.sort(key = sortLength)
        print(f'{wire} - {code}')


    return sum(digit_list)


#answer_1 = solve(read_input('input_08.txt'))
answer_2 = solve2(read_input("input_klein_08.txt"))


#print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
