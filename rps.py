import tkinter as tk
from PIL import Image, ImageTk
import random

# Dictionary to map choices to their respective images
CHOICE_IMAGES = {
    "rock": "rock.png",
    "paper": "paper.png",
    "scissors": "scissor.png",
}

# Dictionary to map choices to their respective outcomes
CHOICE_OUTCOMES = {
    "rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"},
}

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("400x400")

        # Create labels for player and computer choices
        self.player_choice_label = tk.Label(self.master, text="Your choice:")
        self.player_choice_label.pack()

        self.computer_choice_label = tk.Label(self.master, text="Computer's choice:")
        self.computer_choice_label.pack()

        # Create images for player and computer choices
        self.player_choice_image = self.create_image_label()
        self.player_choice_image.pack()

        self.computer_choice_image = self.create_image_label()
        self.computer_choice_image.pack()

        # Create label to display game outcome
        self.outcome_label = tk.Label(self.master, text="")
        self.outcome_label.pack()

        # Create buttons for player choices
        self.rock_button = tk.Button(self.master, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side="top")

        self.paper_button = tk.Button(self.master, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side="top")

        self.scissors_button = tk.Button(self.master, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side="top")

    def create_image_label(self):
        # Create empty image label
        image_label = tk.Label(self.master)
        image_label.image = None
        return image_label

    def play(self, player_choice):
        # Choose a random computer choice
        computer_choice = random.choice(list(CHOICE_IMAGES.keys()))

        # Load player and computer choice images
        player_image = self.load_image(CHOICE_IMAGES[player_choice])
        computer_image = self.load_image(CHOICE_IMAGES[computer_choice])

        # Update player and computer choice images
        self.update_image_label(self.player_choice_image, player_image)
        self.update_image_label(self.computer_choice_image, computer_image)

        # Determine game outcome and display it
        outcome = CHOICE_OUTCOMES[player_choice][computer_choice]
        self.outcome_label.config(text=f"You {outcome}!")

    def load_image(self, filename):
        # Load image from file and resize it to fit in the GUI
        image = Image.open(filename)
        image = image.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def update_image_label(self, image_label, image):
        # Update image in image label
        image_label.config(image=image)
        image_label.image = image

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
