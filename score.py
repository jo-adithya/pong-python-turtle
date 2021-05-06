from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_screen()

    def update_score(self, score, pos):
        self.setpos(pos)
        self.write(score, align='center', font=('Courier', 80, 'normal'))

    def update_screen(self):
        self.clear()
        self.update_score(self.l_score, (-100, 200))
        self.update_score(self.r_score, (100, 200))

    def l_point(self):
        self.l_score += 1
        self.update_screen()

    def r_point(self):
        self.r_score += 1
        self.update_screen()
