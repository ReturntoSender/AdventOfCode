def read_input(file):
    data = []
    with open(file) as f:
        data = [line.strip() for line in f]
    return data


def solve(data, dx, dy):
    way = ""
    posX = posY = 0
    while posY + dy < len(data):
        posX += dx
        posY += dy
        way += data[posY][posX % len(data[posY])]

    return way.count("#")


def solve2(data):
    multi = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for dx, dy in slopes:
        trees = solve(data, dx, dy)
        multi *= trees
    return multi


answer_1 = solve(read_input("input_03.txt"), 3, 1)
answer_2 = solve2(read_input("input_03.txt"))

print(f"Die Loesung 1: {answer_1} \nDie Loesung 2: {answer_2}")
