
def get_calibration_value(word: str) -> int:
    i = 0
    j = len(word)-1

    while not word[i].isdigit():
        i += 1

    while not word[j].isdigit():
        j -= 1

    return int("{}{}".format(word[i], word[j]))

WORD_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_proper_calibration_value(word: str) -> int:
    first = 0
    i = 0
    while True:
        if word[i].isdigit():
            first = int(word[i])
            break

        if len(word[:i+1]) >= 3:
            for w in WORD_MAP:
                if word[:i+1].endswith(w):
                    first = WORD_MAP[w]
                    break
            if first:
                break

        i += 1

    second = 0
    j = len(word)-1
    while True:
        if word[j].isdigit():
            second = int(word[j])
            break

        if len(word[j:]) >= 3:
            for w in WORD_MAP:
                if word[j:].startswith(w):
                    second = WORD_MAP[w]
                    break
            if second:
                break


        j -= 1

    return int("{}{}".format(first, second))

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        ans = 0
        ans2 = 0
        for line in lines:
            line = line.strip()
            ans += get_calibration_value(line)
            ans2 += get_proper_calibration_value(line)

        print(ans)
        print(ans2)
