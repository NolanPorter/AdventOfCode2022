# easy

def part1():
    with open('input.txt') as f:
        max = 0
        current = 0
        for line in f.readlines():
            if line != "\n":
                current += int(line)
            else:
                if current > max:
                    max = current
                current = 0
        print(max)

def part2():
    with open('input.txt') as f:
        elves = []
        current = 0
        for line in f.readlines():
            if line != "\n":
                current += int(line)
            else:
                elves.append(current)
                current = 0
        print(sum(sorted(elves)[-3:]))

part1()
part2()