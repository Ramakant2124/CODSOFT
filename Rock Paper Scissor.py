import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors || Devloper By Ramakant Chaudhari")
root.geometry("600x450")
root.resizable(False, False)
root.configure(bg="#f7dc6f")

# Title
tk.Label(root, text="Rock-Paper-Scissors",bg="#f7dc6f",font=("Arial", 18, "bold")).pack(pady=10)

# Instructions
tk.Label(root, text="First to 3 points wins. Choose your move:",bg="#f7dc6f", font=("Arial", 12)).pack(pady=5)

# Game logic
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "User"
    else:
        return "Computer"

# When user clicks a choice button
def play(user_choice):
    global user_score, computer_score
    
    computer_choice = get_computer_choice()
    winner = decide_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer choice: {computer_choice}")

    if winner == "Tie":
        result_label.config(text="It's a tie!")
    elif winner == "User":
        user_score += 1
        result_label.config(text="You win this round!")
    else:
        computer_score += 1
        result_label.config(text="Computer wins this round!")

    score_label.config(text=f"Score — You: {user_score}  Computer: {computer_score}")

    # Check if game over
    if user_score == 3 or computer_score == 3:
        if user_score > computer_score:
            final_result = "You won the game! Congratulations!"
        else:
            final_result = "Computer won the game! Better luck next time."
        result_label.config(text=final_result)
        # Disable buttons after game ends
        rock_btn.config(state='disabled')
        paper_btn.config(state='disabled')
        scissors_btn.config(state='disabled')
        play_again_btn.pack(pady=10)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer choice: ")
    result_label.config(text="Make your move!")
    score_label.config(text="Score — You: 0  Computer: 0")
    rock_btn.config(state='normal')
    paper_btn.config(state='normal')
    scissors_btn.config(state='normal')
    play_again_btn.pack_forget()



# Buttons for choices
btn_frame = tk.Frame(root,bg="#f7dc6f")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, font=("Arial", 18),bg="#e9004a",
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, font=("Arial", 18),bg="#2fb5e6",
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, font=("Arial", 18),bg="#c549aa",
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Display choices and results
user_choice_label = tk.Label(root, text="Your choice: ",bg="#f7dc6f", font=("Arial", 25))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer choice: ",bg="#f7dc6f", font=("Arial", 25))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 18, "bold"),bg="#f7dc6f", fg="blue")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score — You: 0  Computer: 0",bg="#f7dc6f", font=("Arial", 18))
score_label.pack(pady=5)

# Play again button (hidden initially)
play_again_btn = tk.Button(root, text="Play Again", font=("Arial", 18), command=reset_game)

root.mainloop()
