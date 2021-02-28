from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "W")
screen.onkey(l_paddle.down, "S")

is_on = True
while is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bonce()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.hit_paddle()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit_paddle()







screen.exitonclick()