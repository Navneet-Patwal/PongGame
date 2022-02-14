from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_lscore()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_rscore()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        is_game_on = False
screen.exitonclick()