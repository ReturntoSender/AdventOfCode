def read_input(file):
    with open(file) as f:
        numbers, *boards = f.read().split('\n\n')
        numbers = numbers.split(',')
        boards = [[row.split() for row in board.strip().split('\n')]
                  for board in boards]
    return numbers, boards


def checkBingo(board, draw_numbers, draw_number):
    row_cols = [{n for n in row} for row in board]
    row_cols += [{n for n in col} for col in zip(*board)]
    for s in row_cols:
        if s.issubset(draw_numbers):
            all_numbers = {n for row in board for n in row}
            return sum(int(n) for n in (all_numbers - draw_numbers)) * int(draw_number)


def solve(numbers, boards):
    draw_numbers, results = set(), []
    for draw_number in numbers:
        draw_numbers.add(draw_number)
        for board in boards:
            if (bingo := checkBingo(board, draw_numbers, draw_number)):
                results.append(bingo)
                del boards[boards.index(board)]
    return results[0]


def solve2(numbers, boards):
    draw_numbers, results = set(), []
    for draw_number in numbers:
        draw_numbers.add(draw_number)
        for board in boards:
            if (bingo := checkBingo(board, draw_numbers, draw_number)):
                results.append(bingo)
                del boards[boards.index(board)]
    return results[-1]


answer_1 = solve(*read_input("input_04.txt"))
answer_2 = solve2(*read_input("input_04.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
