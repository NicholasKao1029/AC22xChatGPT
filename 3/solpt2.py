# Read the input from the file input.txt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Parse the input to extract the rucksacks of each group
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

# For each group, find the item types that are common to all three members
group_badge_types = []
for group in groups:
    # Find the common item types by intersecting the set of unique characters in each rucksack
    common_item_types = set(group[0]) & set(group[1]) & set(group[2])
    # The common item types should only have one or more elements
    for badge_type in common_item_types:
        group_badge_types.append(badge_type)

# Compute the priority of each group's badge item type
priorities = []
for badge_type in group_badge_types:
    # Lowercase item types have priorities 1 through 26
    if badge_type.islower():
        priority = ord(badge_type) - ord('a') + 1
    # Uppercase item types have priorities 27 through 52
    else:
        priority = ord(badge_type) - ord('A') + 27
    priorities.append(priority)

# Add the priorities of all groups and return the result
result = sum(priorities)
print(result)