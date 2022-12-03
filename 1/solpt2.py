# Open the input file and read in the input
with open('input.txt', 'r') as f:
    calorie_list = f.readlines()

# Loop through the list, keep a running total of the number of Calories
# each Elf is carrying, and track the top three Elves with the highest totals
highest_total_1 = 0
highest_elf_1 = None
highest_total_2 = 0
highest_elf_2 = None
highest_total_3 = 0
highest_elf_3 = None
current_elf = None
current_total = 0
for line in calorie_list:
    line = line.strip()  # Remove any leading or trailing whitespace
    if line == '':
        # We have reached the end of an Elf's inventory
        if current_total > highest_total_1:
            # This Elf has the highest total number of Calories so far
            highest_total_3 = highest_total_2
            highest_elf_3 = highest_elf_2
            highest_total_2 = highest_total_1
            highest_elf_2 = highest_elf_1
            highest_total_1 = current_total
            highest_elf_1 = current_elf
        elif current_total > highest_total_2:
            # This Elf has the second-highest total number of Calories so far
            highest_total_3 = highest_total_2
            highest_elf_3 = highest_elf_2
            highest_total_2 = current_total
            highest_elf_2 = current_elf
        elif current_total > highest_total_3:
            # This Elf has the third-highest total number of Calories so far
            highest_total_3 = current_total
            highest_elf_3 = current_elf
        # Reset the running total for the next Elf
        current_total = 0
    else:
        # This is an item in an Elf's inventory
        if current_elf is None:
            # This is the first item in an Elf's inventory
            current_elf = line
        current_total += int(line)

# Print the top three Elves and the total number of Calories they are carrying
print('The top three Elves are:')
print('1. Elf', highest_elf_1, 'with', highest_total_1, 'Calories')
print('2. Elf', highest_elf_2, 'with', highest_total_2, 'Calories')
print('3. Elf', highest_elf_3, 'with', highest_total_3, 'Calories')
print('These three Elves are carrying a total of', highest_total_1 + highest_total_2 + highest_total_3, 'Calories')
