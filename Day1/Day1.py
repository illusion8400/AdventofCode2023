# # Day 1


with open("./Day1/day1input.txt", "r") as day1input:
    day1input = day1input.readlines()
    
numbers_to_letters = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
# to_replace = {"eight": "e8t", "three": "t3e", "two": "t2o"}
to_replace = {"one": "o1e", "two": "t2o", "three":"t3e","four":"f4r","five":"f5e","six":"s6x","seven":"s7n","eight":"e8t","nine":"n9e"}
cal_values = day1input
cal_value_end = []

for cal in cal_values:
    found_numbers = []
    new_numbers = []
    for key, value in reversed(numbers_to_letters.items()):
        # count = 0
        for key1, value1 in to_replace.items():
            if key1 in cal:
                cal = str(cal).replace(key1, str(value1))
        if key in cal:
            new_numbers.append((
                cal.index(key), value
                ))
            if min(new_numbers):
                cal = str(cal).replace(key, value)
                continue
            if max(new_numbers):
                cal = str(cal).replace(key, value)
                continue
    for letter in cal:
        if letter.isdigit():
            found_numbers.append(letter)
    cal_value_end.append(found_numbers[0]+found_numbers[-1])

print(cal_value_end)

final_cal = 0
for item in cal_value_end:
    final_cal += int(item)

print(final_cal)