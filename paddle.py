from turtle import Turtle
WIDTH = 5
LENGTH = 1


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.color("white")
        self.goto(self.pos)

    def up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
