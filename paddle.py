from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('white')
        self.penup()
        self.setpos(pos)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)
