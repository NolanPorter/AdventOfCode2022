#Yes I know there is some fancy math you can do here to shorten this code significantly,
#but I didn't care to think about it or research how to do it.

def play_part1():
    with open('input.txt') as f:
        lines = f.readlines()
        scores = {
            'A': 1,
            'B': 2,
            'C': 3,
            'X': 1,
            'Y': 2,
            'Z': 3
        }
        total = 0
        for line in lines[:]:
            them = get_play_part1(line[0])
            us = get_play_part1(line[2])
            
            total += scores.get(line[2])

            if (us == "rock" and them == "scissors") or (us == "paper" and them == "rock") or (us == "scissors" and them == "paper"):
                total += 6
            elif us == them:
                total += 3
        

        print(total)



def get_play_part1(char):
    if char == 'A' or char == 'X':
        return "rock"
    elif char == 'B' or char == 'Y':
        return "paper"
    else:
        return "scissors"

play_part1()


def play_part2():
    with open('input.txt') as f:
        lines = f.readlines()
        scores = {
            'A': 1,
            'B': 2,
            'C': 3,
            'X': 1,
            'Y': 2,
            'Z': 3,
            'rock': 1,
            'paper': 2,
            'scissors': 3
        }
        total = 0
        for line in lines[:]:
            them = get_play_part2(line[0])
            
            us = get_response_part2(them, line[2])
            
            total += scores.get(us)

            if (us == "rock" and them == "scissors") or (us == "paper" and them == "rock") or (us == "scissors" and them == "paper"):
                total += 6
            elif us == them:
                total += 3

        print(total)

def get_play_part2(char):
    if char == 'A' or char == 'X':
        return "rock"
    elif char == 'B' or char == 'Y':
        return "paper"
    else:
        return "scissors"

def get_response_part2(them, res):
    play = ""
    
    if them == "rock":
        if res == "X":
            play = "scissors"
        elif res == "Y":
            play = "rock"
        else:
            play = "paper"
    elif them == "paper":
        if res == "X":
            play = "rock"
        elif res == "Y":
            play = "paper"
        else:
            play = "scissors"
    else:
        if res == "X":
            play = "paper"
        elif res == "Y":
            play = "scissors"
        else:
            play = "rock"
    return play


play_part2()