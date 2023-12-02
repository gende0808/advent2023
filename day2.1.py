import re
values = []
with open("day2.txt") as file:
    for line in file:
        values.append(line.rstrip())
puzzle_answer = 0
game_number = 1
for game in values:
    game_is_valid = True
    for grabs in re.split(";",re.sub(r'^.*?: ', '', game)):
        blue =green = red = 0
        for grab in grabs.split(", "):
            if "blue" in grab:
                blue += int(re.sub('\\D','',grab))
            else:
                if "green" in grab:
                    green += int(re.sub('\\D','',grab))
                else:
                    red += int(re.sub('\\D','',grab))
            if blue > 14 or green > 13 or red > 12:
                game_is_valid = False
    if game_is_valid:
        puzzle_answer += game_number
    game_number += 1
print(puzzle_answer)