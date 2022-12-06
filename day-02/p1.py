from utils.utils import get_lines_from_file

LOSE, DRAW, WIN = 0, 3, 6
ROCK, PAPER, SCISSOR = 1, 2, 3


player_guide = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSOR,
}

opponent_guide = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSOR,
}

total_score = 0

test_input = get_lines_from_file('day-02/input.txt')
for row in test_input:
    opponent_choice, player_choice = row.split()
    score = 0
    score = player_guide[player_choice]

    if player_guide[player_choice] == opponent_guide[opponent_choice]:
        score += DRAW
    elif any(
        (player_guide[player_choice] == ROCK and opponent_guide[opponent_choice] == SCISSOR),
        (player_guide[player_choice] == SCISSOR and opponent_guide[opponent_choice] == PAPER),
        (player_guide[player_choice] == PAPER and opponent_guide[opponent_choice] == ROCK),
    ):
        score += WIN
    total_score += score

print(total_score)
