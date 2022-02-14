from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_cor=0
        self.y_cor=0
        self.mov_xunit = 10
        self.mov_yunit = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.mov_xunit
        y_cor = self.ycor() + self.mov_yunit
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.mov_yunit *= -1
        self.move_speed *= 0.9
        self.move()

    def bounce_x(self):
        self.mov_xunit *= -1
        self.move_speed *= 0.9
        self.move()

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
