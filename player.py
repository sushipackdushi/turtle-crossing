from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.pu()
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
        self.speed(self.move_speed * 1.1)




