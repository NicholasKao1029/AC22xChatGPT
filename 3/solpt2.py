# NOT CREATED BY ChatGPT
## Read the games from the input file
with open('input.txt') as f:
  games = f.readlines()

def get_inverse(dct):
    return {v: k for k, v in dct.items()}

# Simulate the tournament
num_rounds = len(games)
total_score = 0
for round in range(1, num_rounds+1):
  # Choose the moves for this round
  opponent_move = games[round-1].strip()[0]
  reported_outcome = games[round-1].strip()[2]

  outcome_dict = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
  }

  outcome = outcome_dict[reported_outcome]

  op_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
  }

  your_map = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
  }

  your_map_inverse = get_inverse(your_map)

  beat_map = {
      "rock": "scissors",
      "paper": "rock",
      "scissors": "paper",
  }

  your_move = None
  op_move = op_map[opponent_move]

  # Update the total score
  if outcome == 'draw':
    your_move = your_map_inverse[op_move]
    total_score += 3
  elif outcome == 'win':
    your_move = your_map_inverse[get_inverse(beat_map)[op_move]]
    total_score += 6
  else:
    your_move = your_map_inverse[beat_map[op_move]]
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
