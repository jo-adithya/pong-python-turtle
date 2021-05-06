from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setpos(0, 0)
        self.penup()
        self.delay = .1
        self.direction = [10, 10]

    def move(self):
        y = self.ycor() + self.direction[1]
        x = self.xcor() + self.direction[0]
        self.setpos(x, y)

    def bounce(self, index):
        self.direction[index] *= -1

    def reset_pos(self):
        self.delay = .1
        self.setpos(0, 0)
        self.bounce(0)
