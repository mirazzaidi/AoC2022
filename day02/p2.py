from utils.utils import get_lines_from_file


LOSE, DRAW, WIN = 0, 3, 6
ROCK, PAPER, SCISSOR = 1, 2, 3


winner_combo = {
    ROCK: PAPER,
    PAPER: SCISSOR,
    SCISSOR: ROCK,
}

loser_combo = {
    ROCK: SCISSOR,
    PAPER: ROCK,
    SCISSOR: PAPER,
}

opponent_guide = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSOR,
}

player_guide = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN,
}

total_score = 0

test_input = get_lines_from_file('day02/input.txt')

for row in test_input:
    opponent_choice, player_choice = row.split()
    score = 0
    if player_guide[player_choice] == DRAW:
        score += DRAW
        score += opponent_guide[opponent_choice]

    elif player_guide[player_choice] == WIN:
        score += WIN
        score += winner_combo[opponent_guide[opponent_choice]]

    elif player_guide[player_choice] == LOSE:
        score += LOSE
        score += loser_combo[opponent_guide[opponent_choice]]
    total_score += score

print(total_score)
