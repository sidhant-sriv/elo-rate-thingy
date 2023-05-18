import math


def calculate_elo_rating(winner_rating, loser_rating, k_factor=32):
    expected_win_probability = get_expected_win_probability(
        winner_rating, loser_rating)
    winner_new_rating = winner_rating + \
        k_factor * (1 - expected_win_probability)
    loser_new_rating = loser_rating + k_factor * (0 - expected_win_probability)
    return int(winner_new_rating), int(loser_new_rating)


def get_expected_win_probability(player_rating, opponent_rating):
    return 1 / (1 + math.pow(10, (opponent_rating - player_rating) / 400))

