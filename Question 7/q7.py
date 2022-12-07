def part1():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

        dir_sizes = {}
        dir_stack = []

        for line in lines:
            if line[0] == "$":
                if line[2:4] == "cd":
                    dir = line[5:]
                    if dir != "..":
                        dir_stack.append(dir)
                        dir_sizes[''.join(dir_stack)] = 0
                    else:
                        dir_stack.pop()
            else:
                size, name = line.split(' ')
                if size != "dir":
                    for dir in range(len(dir_stack), 0, -1):
                        dir_sizes[''.join(dir_stack[:dir])] += int(size)

        d = dict((k, v) for k, v in dir_sizes.items() if v <= 100000)
        print(sum(d.values()))

def part2():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

        dir_sizes = {}
        dir_stack = []

        for line in lines:
            if line[0] == "$":
                if line[2:4] == "cd":
                    dir = line[5:]
                    if dir != "..":
                        dir_stack.append(dir)
                        dir_sizes[''.join(dir_stack)] = 0
                    else:
                        dir_stack.pop()
            else:
                size, name = line.split(' ')
                if size != "dir":
                    for dir in range(len(dir_stack), 0, -1):
                        dir_sizes[''.join(dir_stack[:dir])] += int(size)

        possible = [v for v in dir_sizes.values() if dir_sizes["/"]-v <= 40000000]
        print(min(possible))


part1()
part2()