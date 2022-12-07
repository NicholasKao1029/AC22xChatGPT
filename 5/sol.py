# Initialize the stacks of crates
stacks = [
    ["F", "H", "B", "V", "R", "Q", "D", "P"],  # Stack 1
    ["L", "D", "Z", "Q", "W", "V"],  # Stack 2
    ["H", "L", "Z", "Q", "G", "R", "P", "C"],  # Stack 3
    ["R", "D", "H", "F", "J", "V", "B"],  # Stack 4
    ["Z", "W", "K", "C"],  # Stack 5
    ["J", "R", "P", "N", "T", "G", "V", "M"],  # Stack 6
    ["J", "R", "L", "V", "M", "B", "S"],  # Stack 7
    ["D", "P", "J"],  # Stack 8
    ["D", "C", "N", "W", "V"],  # Stack 9
]

# Read the rearrangement procedure from the text file (starting from line 11)
procedure = []
with open("input.txt") as f:
    for i, line in enumerate(f):
        if i < 10:
            continue
        num_crates, source, destination = map(int, line.strip().split()[1::2])
        procedure.append((num_crates, source, destination))

# Apply each step of the rearrangement procedure
for step in procedure:
    # Unpack the step tuple
    num_crates, source, destination = step

    # Remove the specified number of crates from the source stack
    moved_crates = stacks[source - 1][-num_crates:]
    stacks[source - 1] = stacks[source - 1][:-num_crates]

    # Add the crates to the destination stack
    stacks[destination - 1].extend(moved_crates[::-1])

# Concatenate the top crate of each stack to create the final message
message = "".join(stacks[i][-1] for i in range(len(stacks)))
print(message)  # Output: "CMZ"
