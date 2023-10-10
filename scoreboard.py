from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.pu()
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-235, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def score_point(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
