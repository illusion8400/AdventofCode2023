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
    
    this_game = game_title.search(game) # print(this_game.group())
    # print(this_game.group())
    while True:
        for set in game.split(sep=";"):
            set = set.replace(str(this_game.group()),"")
            # print(set)
            for color in game_colors.findall(set):
                if "red" in color:
                    for x in color:
                        set_red = int(x)
                        if str(x).isdigit():
                            if int(x) > int(RED_MAX):
                                bad_games.append(this_game.group())
                                # print(bad_games)
                                break
                        break
                    break
        break
    while True:
        for set in game.split(sep=";"):
            set = set.replace(str(this_game.group()),"")
            # print(set)
            for color in game_colors.findall(set):
                if "green" in color:
                    for x in color:
                        set_red = int(x)
                        if str(x).isdigit():
                            if int(x) > int(GREEN_MAX):
                                bad_games.append(this_game.group())
                                # print(bad_games)
                                break
                        break
                    break
        break
    while True:
        for set in game.split(sep=";"):
            set = set.replace(str(this_game.group()),"")
            # print(set)
            for color in game_colors.findall(set):
                if "blue" in color:
                    for x in color:
                        set_red = int(x)
                        if str(x).isdigit():
                            if int(x) > int(BLUE_MAX):
                                bad_games.append(this_game.group())
                                # print(bad_games)
                                break
                        break
                    break
        break
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
print(final_total)
        
    
    
