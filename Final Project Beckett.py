Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Author: Jeffrey Beckett
# Date: 2024-05-03
# Description: 2-Player Dice Game, where players compete to reach 20 points using two six-sided dice.

import random

def roll_dice():
    """Return a tuple of two random numbers between 1 and 6."""
    return random.randint(1, 6), random.randint(1, 6)

def compare_rolls(roll1, roll2):
    """Compare rolls of two players and assign points based on the game rules."""
    points1, points2 = 0, 0
    if max(roll1) > max(roll2):
        points1 += 2
    elif max(roll1) < max(roll2):
        points2 += 2

    if min(roll1) > min(roll2):
        points1 += 1
    elif min(roll1) < min(roll2):
        points2 += 1

    return points1, points2

def display_results(score_player1, score_player2, roll1, roll2, points1, points2):
    """Display the results of each round."""
    print(f"Player 1 rolled: {roll1}")
    print(f"Player 2 rolled: {roll2}")
    print(f"Points this round - Player 1: {points1}, Player 2: {points2}")
    print(f"Current Score - Player 1: {score_player1}, Player 2: {score_player2}")

def game_loop():
    score_player1, score_player2 = 0, 0
    while score_player1 < 20 and score_player2 < 20:
        input("Player 1, press Enter to roll the dice...")
        roll1 = roll_dice()
        input("Player 2, press Enter to roll the dice...")
        roll2 = roll_dice()

        points1, points2 = compare_rolls(roll1, roll2)
        score_player1 += points1
        score_player2 += points2

        display_results(score_player1, score_player2, roll1, roll2, points1, points2)

        if score_player1 >= 20 or score_player2 >= 20:
            winner = "Player 1" if score_player1 > score_player2 else "Player 2"
            print(f"{winner} wins the game!")
            if input("Do you want to play again? (yes/no): ").lower() == 'yes':
                score_player1, score_player2 = 0, 0
            else:
                break

if __name__ == "__main__":
    game_loop()
