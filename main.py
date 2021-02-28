from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")

paddle_user = Paddle()
paddle_user.user_position()
paddle_bot = Paddle()
paddle_bot.bot_position()

paddle_bot.paddle_bot_move()




screen.exitonclick()