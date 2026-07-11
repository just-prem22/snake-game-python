from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 23, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        file_path = os.path.join(os.path.dirname(__file__), "data.txt")

        # Read high score safely
        try:
            with open(file_path, "r") as data:
                self.high_score = int(data.read())
        except:
            self.high_score = 0

        self.file_path = file_path

        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        # Update high score if needed
        if self.score > self.high_score:
            self.high_score = self.score

            # Save to file
            with open(self.file_path, "w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()