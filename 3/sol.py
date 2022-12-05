# Read the games from the input file
with open('input.txt') as f:
  games = f.readlines()

# Simulate the tournament
num_rounds = len(games)
total_score = 0
for round in range(1, num_rounds+1):
  # Choose the moves for this round
  opponent_move = games[round-1].strip()[0]
  your_move = games[round-1].strip()[2]

  # Determine the outcome of the round
  if (opponent_move == 'A' and your_move == 'X') or (opponent_move == 'B' and your_move == 'Y') or (opponent_move == 'C' and your_move == 'Z'):
    outcome = 'draw'
  elif (opponent_move == 'A' and your_move == 'Y') or (opponent_move == 'B' and your_move == 'Z') or (opponent_move == 'C' and your_move == 'X'):
    outcome = 'win'
  else:
    outcome = 'lose'

  # Update the total score
  if outcome == 'draw':
    total_score += 3
  elif outcome == 'win':
    total_score += 6
  else:
    total_score += 0

  # Add the score for your move
  if your_move == 'X':
    total_score += 1
  elif your_move == 'Y':
    total_score += 2
  elif your_move == 'Z':
    total_score += 3

# Print the total score
print(total_score)
