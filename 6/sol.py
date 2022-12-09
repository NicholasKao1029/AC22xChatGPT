def find_start_of_packet(input_buffer):
  # Initialize the last four characters buffer with four dummy characters
  last_four = ['d', 'd', 'd', 'd']

  # Process the input buffer one character at a time
  for i in range(len(input_buffer)):
    # Shift the last four characters buffer and add the next character
    last_four = last_four[1:] + [input_buffer[i]]

    # If the last four characters are all different, report the current position
    # and exit
    if len(set(last_four)) == 4:
      return i + 1

# Read the input buffer from the input.txt file
with open('input.txt', 'r') as f:
  input_buffer = f.read()

# Find the first start-of-packet marker in the input buffer
result = find_start_of_packet(input_buffer)

# Print the result
print(result)