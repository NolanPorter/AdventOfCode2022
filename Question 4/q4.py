def part1():
    with open('input.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            left, right = [part.strip() for part in line.split(',')]
            l1, l2 = left.split('-')
            r1, r2 = right.split('-')
            l1, l2, r1, r2 = [int(x) for x in [l1, l2, r1, r2]]
            if (l1 >= r1 and l2 <= r2) or (r1 >= l1 and r2 <= l2):
                total += 1

        print(total)

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            left, right = [part.strip() for part in line.split(',')]
            l1, l2 = left.split('-')
            r1, r2 = right.split('-')
            l1, l2, r1, r2 = [int(x) for x in [l1, l2, r1, r2]]

            if (l1 >= r1 and l1 <= r2) or (r1 >= l1 and r1 <= l2):
                total += 1

        print(total)

part1()
part2()