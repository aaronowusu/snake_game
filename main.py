from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# User Interface Set-Up #
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Begins the game by generating a snake, food and scoreboard object and waits for keys to be pressed. #
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

# Game Controls #
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")

game_is_on = True
while game_is_on:
    # This ensures that the snake automatically moves in the direction its head is pointing towards.
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
