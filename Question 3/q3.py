# Simple and clean

def part1():
    with open('input.txt') as f:
        total = 0
        for line in f.readlines():
            shared = ''.join(set(line[:len(line)//2]).intersection(line[len(line)//2:]))
            for char in shared:
                val = ord(char)
                if 65 <= val <= 90:
                    val -= 38
                else:
                    val -= 96
                total += val

        print(total)


def part2():
    with open('input.txt') as f:
        total = 0
        for i in list(chunks(f.readlines(), 3)):
            shared = ''.join(set(i[0]).intersection(i[1]).intersection(i[2])).strip()
            for char in shared:
                val = ord(char)
                if 65 <= val <= 90:
                    val -= 38
                else:
                    val -= 96
                total += val

        print(total)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

part1()
part2()