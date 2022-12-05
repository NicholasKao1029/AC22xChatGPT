# Read the input from the file input.txt
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Parse the input to extract the rucksacks of each group
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

# For each group, find the item type that is common to all three members
group_badge_types = []
for group in groups:
    # Find the common item type by intersecting the set of unique characters in each rucksack
    common_item_type = set(group[0].strip()) & set(group[1].strip()) & set(group[2].strip())
    # The common item type should only have one element, so take the first and only element
    print(common_item_type)
    badge_type = list(common_item_type)[0]
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
