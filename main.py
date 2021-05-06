from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

ball = Ball()
score = Score()

game_on = True
while game_on:
    time.sleep(ball.delay)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce(1)

    # Detect collision with right paddle
    if ball.xcor() == 330 and r_paddle.ycor() + 55 > ball.ycor() > r_paddle.ycor() - 55:
        ball.delay *= .8
        ball.bounce(0)

    # Detect collision with left paddle
    if ball.xcor() == -330 and l_paddle.ycor() + 55 > ball.ycor() > l_paddle.ycor() - 55:
        ball.delay *= .8
        ball.bounce(0)

    # Detect out of bounds for right paddle
    if ball.xcor() >= 420:
        ball.reset_pos()
        score.l_point()

    # Detect out of bounds for left paddle
    if ball.xcor() <= -420:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
