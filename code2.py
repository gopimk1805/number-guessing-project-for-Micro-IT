import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎯 Number Guessing Game")
        self.window.geometry("500x600")
        self.window.configure(bg="#1a1a2e")
        self.window.resizable(False, False)
        
        # Game variables
        self.min_num = 1
        self.max_num = 100
        self.max_attempts = 7
        self.reset_game()
        
        self.create_widgets()
        
    def reset_game(self):
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts_left = self.max_attempts
        self.game_over = False
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.window,
            text="🎯 NUMBER GUESSING GAME",
            font=("Arial", 24, "bold"),
            bg="#1a1a2e",
            fg="#00d4aa"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.window,
            text=f"Guess the number between {self.min_num} and {self.max_num}!",
            font=("Arial", 14),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        instructions.pack(pady=10)
        
        # Attempts counter
        self.attempts_label = tk.Label(
            self.window,
            text=f"Attempts left: {self.attempts_left}",
            font=("Arial", 16, "bold"),
            bg="#1a1a2e",
            fg="#ff6b6b"
        )
        self.attempts_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.window, bg="#1a1a2e")
        input_frame.pack(pady=20)
        
        tk.Label(
            input_frame,
            text="Your guess:",
            font=("Arial", 14),
            bg="#1a1a2e",
            fg="#ffffff"
        ).pack(side=tk.LEFT, padx=10)
        
        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=10,
            justify="center",
            bg="#16213e",
            fg="#ffffff",
            insertbackground="#ffffff",
            relief="flat",
            bd=5
        )
        self.guess_entry.pack(side=tk.LEFT, padx=10)
        self.guess_entry.bind("<Return>", lambda event: self.make_guess())
        
        # Guess button
        self.guess_button = tk.Button(
            self.window,
            text="🎲 GUESS",
            font=("Arial", 14, "bold"),
            bg="#4ecdc4",
            fg="#1a1a2e",
            activebackground="#00d4aa",
            activeforeground="#1a1a2e",
            relief="flat",
            width=15,
            height=2,
            command=self.make_guess
        )
        self.guess_button.pack(pady=20)
        
        # Feedback area
        self.feedback_label = tk.Label(
            self.window,
            text="Make your first guess!",
            font=("Arial", 16),
            bg="#1a1a2e",
            fg="#feca57",
            wraplength=400,
            justify="center"
        )
        self.feedback_label.pack(pady=20)
        
        # History area
        history_title = tk.Label(
            self.window,
            text="📊 Your Guesses:",
            font=("Arial", 14, "bold"),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        history_title.pack(pady=(20, 5))
        
        self.history_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 12),
            bg="#1a1a2e",
            fg="#a8a8a8",
            wraplength=400,
            justify="center"
        )
        self.history_label.pack(pady=5)
        
        # Control buttons frame
        control_frame = tk.Frame(self.window, bg="#1a1a2e")
        control_frame.pack(pady=30)
        
        # New game button
        self.new_game_button = tk.Button(
            control_frame,
            text="🔄 NEW GAME",
            font=("Arial", 12, "bold"),
            bg="#ff6b6b",
            fg="#ffffff",
            activebackground="#ff5252",
            activeforeground="#ffffff",
            relief="flat",
            width=12,
            command=self.new_game
        )
        self.new_game_button.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_button = tk.Button(
            control_frame,
            text="❌ QUIT",
            font=("Arial", 12, "bold"),
            bg="#6c5ce7",
            fg="#ffffff",
            activebackground="#5f3dc4",
            activeforeground="#ffffff",
            relief="flat",
            width=12,
            command=self.window.quit
        )
        quit_button.pack(side=tk.LEFT, padx=10)
        
        # Initialize history
        self.guess_history = []
        
    def make_guess(self):
        if self.game_over:
            return
            
        try:
            guess = int(self.guess_entry.get())
            
            if guess < self.min_num or guess > self.max_num:
                self.feedback_label.config(
                    text=f"⚠️ Please enter a number between {self.min_num} and {self.max_num}!",
                    fg="#ff6b6b"
                )
                return
                
            self.attempts_left -= 1
            self.guess_history.append(guess)
            
            if guess == self.secret_number:
                self.win_game()
            elif self.attempts_left == 0:
                self.lose_game()
            else:
                self.give_feedback(guess)
                
            self.update_display()
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            self.feedback_label.config(
                text="❌ Please enter a valid number!",
                fg="#ff6b6b"
            )
            
    def give_feedback(self, guess):
        if guess < self.secret_number:
            difference = self.secret_number - guess
            if difference <= 5:
                hint = "Very close! 🔥"
            elif difference <= 15:
                hint = "Getting warmer! 🌡️"
            else:
                hint = "Too cold! ❄️"
            self.feedback_label.config(
                text=f"📈 Too LOW! {hint}",
                fg="#74b9ff"
            )
        else:
            difference = guess - self.secret_number
            if difference <= 5:
                hint = "Very close! 🔥"
            elif difference <= 15:
                hint = "Getting warmer! 🌡️"
            else:
                hint = "Too cold! ❄️"
            self.feedback_label.config(
                text=f"📉 Too HIGH! {hint}",
                fg="#ff7675"
            )
            
    def win_game(self):
        self.game_over = True
        attempts_used = self.max_attempts - self.attempts_left
        self.feedback_label.config(
            text=f"🎉 CONGRATULATIONS! 🎉\nYou guessed it in {attempts_used} attempts!",
            fg="#00d4aa"
        )
        self.guess_button.config(state="disabled")
        
    def lose_game(self):
        self.game_over = True
        self.feedback_label.config(
            text=f"💀 GAME OVER! 💀\nThe number was {self.secret_number}",
            fg="#ff6b6b"
        )
        self.guess_button.config(state="disabled")
        
    def update_display(self):
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        history_text = " → ".join(map(str, self.guess_history))
        self.history_label.config(text=history_text)
        
    def new_game(self):
        self.reset_game()
        self.guess_history = []
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.feedback_label.config(
            text="Make your first guess!",
            fg="#feca57"
        )
        self.history_label.config(text="")
        self.guess_button.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
        
    def run(self):
        self.guess_entry.focus()
        self.window.mainloop()

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()