import random

def roll_dice():
    # Roll a six-sided dice and return the result
    return random.randint(1, 6)

def play_game():
    # Get player names
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    print(f"\nWelcome, {player1} and {player2}!\n")

    # Initialize scores
    score1 = 0
    score2 = 0

    # Play five rounds
    for i in range(5):
        print(f"Round {i+1}:")
        # Player 1's turn
        input(f"{player1}, press enter to roll the dice.")
        roll1 = roll_dice()
        print(f"{player1} rolled a {roll1}!\n")
        score1 += roll1

        # Player 2's turn
        input(f"{player2}, press enter to roll the dice.")
        roll2 = roll_dice()
        print(f"{player2} rolled a {roll2}!\n")
        score2 += roll2

    # Determine the winner
    if score1 > score2:
        print(f"{player1} wins with a score of {score1}!")
    elif score2 > score1:
        print(f"{player2} wins with a score of {score2}!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
