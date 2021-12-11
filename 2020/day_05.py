def read_input(file):
    with open(file) as f:
        data = [(line.strip().replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')) for line in f]
    return data

def solve(data):
    possible = []
    for seat in data:
        row = int(seat[:-3], 2)
        possible.append(row*8 + int(seat[-3:], 2))
    return possible


def solve2(data):
    data.sort()
    plane = [c for c in range(min(data), max(data)+1)]
    for seat in data:
        if seat in plane:
            plane.remove(seat)
    return plane[0]
    



answer_1 = max(solve(read_input("input_05.txt")))
answer_2 = solve2(solve(read_input("input_05.txt")))

print(f"Die Loesung 1: {answer_1} \nDie Loesung 2: {answer_2}")
