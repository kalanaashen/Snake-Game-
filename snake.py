from turtle import Screen
from snake_1 import Snake
from food import Food
from scoreborad import Scoreboard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My sna")
snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if snake.head.distance(food)<15:
        food.refresh()
        score.marks()
        snake.new_part()

    #collation of wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        score.defeat_logo()


    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_on=False
            score.defeat_logo()












screen.exitonclick()