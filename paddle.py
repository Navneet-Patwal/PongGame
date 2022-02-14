from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super(Paddle, self).__init__()
        self.pos_x = pos_x
        self.shape("square")
        self.color("white")
        self.turtlesize(1, 4)
        self.penup()
        self.setheading(90)
        self.goto(pos_x, pos_y)

    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.pos_x, y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.pos_x, y_cor)

