from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('My Turtle Game')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True
scoreboard = Scoreboard()

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Coillison with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.incrace_score()

    # Detecting the coillison with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
        print('Game Over')
        is_game_on = False

    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False
            print('game over')



game_over_text = Turtle()
game_over_text.color('white')
game_over_text.hideturtle()
game_over_text.write(arg="Game Over",align='center',font=("Arial",20,"normal"))








screen.exitonclick()
