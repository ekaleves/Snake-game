from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

score = 0
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with the food
    if snake.head.distance(food) < 15:
        score += 1
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.score_points(score)

    # detect collision with the walls
    if snake.head.xcor() > 284 or snake.head.xcor() < -284 or snake.head.ycor() > 284 or snake.head.ycor() < -284:
        game_is_on = False
        scoreboard.game_over(score)

    # Detect collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over(score)


screen.exitonclick()
