from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        # Obtains the previous high score from the data.txt file and displays it on screen.
        super().__init__()
        self.score = 0
        with open("data.txt") as self.previous_high_score:
            self.high_score = int(self.previous_high_score.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        # Displays the current and high score in the specified alignment and font.
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # Resets the score to 0 and updates the high score if the previous one has been beat.
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as self.previous_high_score:
            self.previous_high_score.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    def update_score(self):
        # Updates the users current score.
        self.score += 1
        self.display_score()
