import re

# Read the input from a text file
with open("input.txt") as f:
    input = f.readlines()

# Compile a regular expression to extract the section IDs
pattern = re.compile(r"(\d+)-(\d+)")
pairs = []
for line in input:
    # Match the regular expression against each line
    match = pattern.match(line)
    if match:
        # Extract the section IDs and store them as a pair
        pairs.append((int(match.group(1)), int(match.group(2))))

# Count the number of pairs where one range fully contains the other
count = 0
for a, b in pairs:
    for x, y in pairs:
        if a <= x and b >= y and (a, b) != (x, y):
            count += 1

# Print the result
print(count)
