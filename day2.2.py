import re
values = []
with open("day2.txt") as file:
    for line in file:
        values.append(line.rstrip())
puzzle_answer = 0
for game in values:
    game_is_valid = True
    blue = green = red = 0
    for grabs in re.split(";",re.sub(r'^.*?: ', '', game)):
        for grab in grabs.split(", "):
            value = int(re.sub('\\D','',grab))
            if "blue" in grab:
                if value > blue:
                    blue = value
            else:
                if "green" in grab:
                    if value > green:
                        green = value
                else:
                    if value > red:
                        red = value
    puzzle_answer += blue * green * red
print(puzzle_answer)