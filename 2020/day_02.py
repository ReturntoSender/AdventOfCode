def read_input(file):
    data = []
    with open(file) as f:
        for line in f:
            count, letter, passw = line.split()
            low, high = [int(x) for x in count.split('-')]
            letter = letter[0]
            data.append((low, high, letter, passw))
    return data


def solve(data):
    counter = 0
    for set in data:
        if set[3].count(set[2]) >= set[0] and set[3].count(set[2]) <= set[1]:
            counter +=1
    return counter

def solve2(data):
    counter = 0
    for set in data:
        chars = set[3][set[0]-1] + set[3][set[1]-1]
        if chars.count(set[2]) == 1: counter += 1
    return counter


answer_1 = solve(read_input("input_02.txt"))
answer_2 = solve2(read_input("input_02.txt"))

print(f"Die Loesung 1: {answer_1} \nDie Loesung 2: {answer_2}")