from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)

screen.listen()
screen.onkey(l_paddle.Up, "Up")
screen.onkey(l_paddle.Down, "Down")

is_on = True
while is_on:
    screen.update()









screen.exitonclick()