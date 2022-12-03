# Open the input file and read in the input
with open('input.txt', 'r') as f:
    calorie_list = f.readlines()

# Loop through the list, keep a running total of the number of Calories
# each Elf is carrying, and track the Elf with the highest total
highest_total = 0
highest_elf = None
current_elf = None
current_total = 0
for line in calorie_list:
    line = line.strip()  # Remove any leading or trailing whitespace
    if line == '':
        # We have reached the end of an Elf's inventory
        if current_total > highest_total:
            # This Elf has the highest total number of Calories so far
            highest_total = current_total
            highest_elf = current_elf
        # Reset the running total for the next Elf
        current_total = 0
    else:
        # This is an item in an Elf's inventory
        if current_elf is None:
            # This is the first item in an Elf's inventory
            current_elf = line
        current_total += int(line)

# Print the Elf with the highest total number of Calories and the total number of Calories they are carrying
print('Elf', highest_elf, 'is carrying the most Calories with a total of', highest_total)