import random

moves = ["rock", "paper", "scissors"]
def ai_move(player_history):
    if not player_history:
        return random.choice(moves)
    last = player_history[-1]
    if last == "rock":
        return "paper"
    elif last == "paper":
        return "scissors"
    else:
        return "rock"

def winner(player, ai):
    if player == ai:
        return "Draw"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        return "Player"
    else:
        return "AI"


player_history = []
print("Rock Paper Scissors Game")
print("Type 'exit' to quit")

while True:
    player = input("Enter rock, paper, or scissors: ").lower()

    if player == "exit":
        print("Thanks for playing!")
        break

    if player not in moves:
        print("Invalid move! Try again.\n")
        continue

    ai = ai_move(player_history)
    player_history.append(player)

    print(f"AI chose: {ai}")

    result = winner(player, ai)

    if result == "Draw":
        print("It's a draw!")
    elif result == "Player":
        print("You win!")
    else:
        print("AI wins! ")
