from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(5, 1)
        self.penup()
        self.speed("fastest")

    def bot_position(self):
        self.setposition(350, 0)

    def user_position(self):
        self.setposition(-350, 0)

    def paddle_bot_move(self):
        self.speed(1)
        is_on = True
        while is_on:
            self.goto(350, 250)
            self.goto(350, -250)
