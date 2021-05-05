from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setpos(0, 0)
        self.penup()

    def move(self):
        x = self.xcor() + 20
        y = self.ycor() + 15
        self.setpos(x, y)
