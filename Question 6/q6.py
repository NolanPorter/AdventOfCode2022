# Very easy

def part1():
    with open('input.txt') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            viewed = []
            for char in line:
                i += 1
                viewed += char
                if len(viewed) > 3 and len(set(viewed[-4:])) == 4:
                    print(i)
                    break

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            viewed = []
            for char in line:
                i += 1
                viewed += char
                if len(viewed) > 3 and len(set(viewed[-14:])) == 14:
                    print(i)
                    break
                

part1()
part2()
