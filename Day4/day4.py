#

with open("./Day4/day4input.txt","r") as day4input:
    day4input = day4input.readlines()

first_score = 1
bonus_multiplier = 2

winning_numbers = []
score = 0
scratch_card_count = 0
for line in day4input:
    scratch_card_count = scratch_card_count + 1
    card = line.split("|")[0]
    my_numbers = line.split("|")[1]
    card = card.split(":")[1]
    card = card.split()
    my_numbers = my_numbers.split()
    
    count = 0
    cur_score = 0
    for num in card:
        for num2 in my_numbers:
            if int(num2) == int(num):
                winning_numbers.append(num2)
                if count == 0: # first win
                    cur_score = 1
                    count += 1
                    break
                else: # bonus
                    cur_score = cur_score * 2
                    break
    score = score + cur_score

print(f"Winners: {winning_numbers}")
print(f"Score: {score}")
print(f"Card Count: {scratch_card_count}")
        