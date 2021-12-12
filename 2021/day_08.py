def read_input(file):
    with open(file) as f:
        patterns, outputs = [], []
        for row in f:
            left, right = row.split('|')
            patterns.append({len(x): set(x) for x in left.split()})
            outputs.append([set(x) for x in right.split()])

    return patterns, outputs


def solve(patterns, outputs):
    return sum([len(n) in {2, 4, 3, 7} for row in outputs for n in row])


def gen_sig():
    example = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'.split()
    example = [set(x) for x in example]
    pattern = {len(x): x for x in example}
    return {get_sig(x, pattern): str(i) for i, x in enumerate(example)}


def get_sig(x, pattern):
    a, b, c, d = len(x), x & pattern[2], x & pattern[3], x & pattern[4]
    return a, len(b), len(c), len(d)


def solve2(patterns, outputs):
    result = 0
    signatures = gen_sig()
    for pattern, output in zip(patterns, outputs):
        result += int(''.join(signatures[get_sig(x, pattern)] for x in output))
    return result


answer_1 = solve(*read_input('input_08.txt'))
answer_2 = solve2(*read_input("input_08.txt"))


print(f"Die Loesung 1: {answer_1}")
print(f"Die Loesung 2: {answer_2}")
