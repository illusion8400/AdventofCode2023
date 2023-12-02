import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

game_title = re.compile(r"(\w+) (\d+):")
game_colors = re.compile(r"(\d+) (\w+)")

good_games = []
bad_games = []
final_bad_games = []
numbers_to_add = []
final_total = 0
powers_to_add = []

with open("./Day2/day2input.txt", "r") as day2input:
    day2input = day2input.readlines()


for game in day2input:
    this_game = game_title.search(game)
    red_max_game = []
    green_max_game = []
    blue_max_game = []
    while True:
        for set in game.split(sep=";"):
            set = set.replace(str(this_game.group()),"")
            # print(set)
            for color in game_colors.findall(set):
                if "red" in color:
                    red_max = []
                    for x in color:
                        set_red = int(x)
                        red_max.append(int(set_red))
                        if str(x).isdigit():
                            if int(x) > int(RED_MAX):
                                bad_games.append(this_game.group())
                                # print(bad_games)
                                break
                        break
                    red_max_game.append(red_max)
                    break
        break
    while True:
        for set in game.split(sep=";"):
            set = set.replace(str(this_game.group()),"")
            # print(set)
            for color in game_colors.findall(set):
                if "green" in color:
                    green_max = []
                    for x in color:
                        set_red = int(x)
                        green_max.append(int(set_red))
                        if str(x).isdigit():
                            if int(x) > int(GREEN_MAX):
                                bad_games.append(this_game.group())
                                # print(bad_games)
                                break
                        break
                    green_max_game.append(green_max)
                    break
        break
    while True:
        for set in game.split(sep=";"):
            set = set.replace(str(this_game.group()),"")
            # print(set)
            for color in game_colors.findall(set):
                if "blue" in color:
                    blue_max = []
                    for x in color:
                        set_red = int(x)
                        blue_max.append(int(set_red))
                        if str(x).isdigit():
                            if int(x) > int(BLUE_MAX):
                                bad_games.append(this_game.group())
                                # print(bad_games)
                                break
                        break
                    blue_max_game.append(blue_max)
                    break
        break
    print(max(red_max_game),max(green_max_game),max(blue_max_game))
    game_sum = int(max(red_max_game)[0]) * int(max(green_max_game)[0]) * int(max(blue_max_game)[0])
    powers_to_add.append(game_sum)
    for x in bad_games:
        if str(x) in str(game):
            final_bad_games.append(this_game.group())
            break
            # print(f"BAD: {game}")
    else: 
        good_games.append(this_game.group())

for x in good_games:
    numbers_to_add.append(int(re.search(r"\d+", x).group()))

for num in numbers_to_add:
    final_total += int(num)
print(f"final: {final_total}")

print(f'powers_to_add: {powers_to_add}')

power_total_sum = 0
for i in powers_to_add:
    power_total_sum += i
print(f"power_total_sum: {power_total_sum}")

        
    
    
