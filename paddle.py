from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(5, 1)
        self.penup()
        self.speed("fastest")
        self.goto(x, y)

    def paddle_bot_move(self):
        self.speed(1)
        self.goto(350, 250)
        self.goto(350, -250)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
