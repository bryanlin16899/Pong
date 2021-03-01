from turtle import Turtle

class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(width=5)
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.right(90)
        self.speed("fastest")

    def draw_line(self):
        for _ in range(14):
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(20)
