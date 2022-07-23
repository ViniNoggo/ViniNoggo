from turtle import Screen
from time import sleep
import snake as s
import food as f
import scoreboard as sc

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = s.Snake()
food = f.Food()
scoreboard = sc.ScoreBoard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_left, "Left")

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move_snake()

    # Detecting collision with food.
    if snake.head.distance(food) < 20:
        food.refresh_position()
        scoreboard.update_score()
        snake.extend_snake()

    # Detecting collision with wall.
    if ((snake.head.xcor() > 295) or (snake.head.xcor() < -295)) or \
            ((snake.head.ycor() > 295) or (snake.head.ycor() < -295)):
        scoreboard.game_over()
        game_on = False

    # Detecting collision with snake.
    #for segment in snake.snake_length:
        #if segment == snake.head:
            #pass
        #elif snake.head.distance(segment) < 20:
            #game_on = False
            #scoreboard.game_over()

screen.exitonclick()
