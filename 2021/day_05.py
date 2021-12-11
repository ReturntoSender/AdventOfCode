def read_input(file):
    with open(file) as f:
        data = []
        line = f.read().strip().split('\n')
        coords = [[p.split(',') for p in cord.split(' -> ')]
                  for cord in line]
    return coords


def count_board(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 2:
                count += 1
    return count


def solve(data):
    grid = [[0 for i in range(1000)]for j in range(1000)]
    for point in data:
        if point[0][0] == point[1][0]:
            for i in range(min(int(point[0][1]), int(point[1][1])), max(
                    int(point[0][1]), int(point[1][1]))+1):
                grid[i][int(point[0][0])] += 1
        if point[0][1] == point[1][1]:
            for i in range(min(int(point[0][0]), int(point[1][0])), max(
                    int(point[0][0]), int(point[1][0]))+1):
                grid[int(point[0][1])][i] += 1
    return count_board(grid)


def solve2(data):
    grid = [[0 for i in range(1000)]for j in range(1000)]
    for point in data:
        if point[0][0] == point[1][0]:
            for i in range(min(int(point[0][1]), int(point[1][1])), max(
                    int(point[0][1]), int(point[1][1]))+1):
                grid[i][int(point[0][0])] += 1
        elif point[0][1] == point[1][1]:
            for i in range(min(int(point[0][0]), int(point[1][0])), max(
                    int(point[0][0]), int(point[1][0]))+1):
                grid[int(point[0][1])][i] += 1
        else:
            dx = int(point[1][0]) - int(point[0][0])
            dy = int(point[1][1]) - int(point[0][1])
            x = int(point[0][0])
            y = int(point[0][1])
            grid[y][x] += 1
            while abs(dx) > 0:
                if dx < 0:
                    dx += 1
                    x -= 1
                else:
                    dx -= 1
                    x += 1
                if dy < 0:
                    dy += 1
                    y -= 1
                else:
                    dy -= 1
                    y += 1
                grid[y][x] += 1
    return count_board(grid)


answer_1 = solve(read_input('input_05.txt'))
answer_2 = solve2(read_input("input_05.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
