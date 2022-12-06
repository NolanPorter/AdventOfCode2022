import re

# 80% of this code is just parsing the input properly
# Overall not too bad

def part1():
    with open('input.txt') as file:
        lines = [line.strip() for line in file.readlines()]
        i = 0
        all_letters = []
        stacks = []
        while lines[i][0] != '1':
            letters = [part.strip().strip('[').strip(']') for part in list(chunks(lines[i], 4))]
            all_letters.append(letters)
            stacks.append([])
            i += 1
        stacks.append([])
        i += 2
        for row in all_letters:
            j = 0
            for letter in row:
                if letter != '':
                    stacks[j].append(letter)
                j += 1

        lines = lines[i:]
        for line in lines:
            m, f, t = [int(n) for n in re.findall(r'\d+', line)]
            f -= 1
            t -= 1
            move_block = stacks[f][:m]
            stacks[f] = stacks[f][m:]
            stacks[t] = list(reversed(move_block)) + stacks[t]


        print([stack[0] for stack in stacks])

def part2():
    with open('input.txt') as file:
        lines = [line.strip() for line in file.readlines()]
        i = 0
        all_letters = []
        stacks = []
        while lines[i][0] != '1':
            letters = [part.strip().strip('[').strip(']') for part in list(chunks(lines[i], 4))]
            all_letters.append(letters)
            stacks.append([])
            i += 1
        stacks.append([])
        i += 2
        for row in all_letters:
            j = 0
            for letter in row:
                if letter != '':
                    stacks[j].append(letter)
                j += 1

        lines = lines[i:]
        for line in lines:
            m, f, t = [int(n) for n in re.findall(r'\d+', line)]
            f -= 1
            t -= 1
            move_block = stacks[f][:m]
            stacks[f] = stacks[f][m:]
            stacks[t] = move_block + stacks[t]

        print([stack[0] for stack in stacks])

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

part1()
part2()