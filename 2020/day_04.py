import string


def read_input(file):
    with open(file) as f:
        data = f.read().split("\n\n")
        data = [passport.split() for passport in data]
    return [dict(item.split(":") for item in passport) for passport in data]


def solve(data):
    valid_1 = []
    exp_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for d in data:
        if all([x in d for x in exp_fields]):
            valid_1.append(d)
    return valid_1


def solve2(data):
    valid_2 = []
    for incredential in data:
        if not 1920 <= int(incredential["byr"]) <= 2002:
            continue
        if not 2010 <= int(incredential["iyr"]) <= 2020:
            continue
        if not 2020 <= int(incredential["eyr"]) <= 2030:
            continue
        if incredential["hgt"][-2:] not in ("cm", "in"):
            continue
        elif (
            incredential["hgt"][-2:] == "cm"
            and not 150 <= int(incredential["hgt"][:-2]) <= 193
        ):
            continue
        elif (
            incredential["hgt"][-2:] == "in"
            and not 59 <= int(incredential["hgt"][:-2]) <= 76
        ):
            continue
        if len(incredential["hcl"]) < 7 or not (
            all(c in string.hexdigits for c in incredential["hcl"][1:])
        ):
            continue
        if not incredential["ecl"] in "amb blu brn gry grn hzl oth".split():
            continue
        if len(incredential["pid"]) != 9 or not (
            all(c in string.digits for c in incredential["pid"])
        ):
            continue
        valid_2.append(incredential)
    return valid_2


answer_1 = len(solve(read_input("input_04.txt")))
answer_2 = len(solve2(solve(read_input("input_04.txt"))))

print(f"Die Loesung 1: {answer_1} \nDie Loesung 2: {answer_2}")
