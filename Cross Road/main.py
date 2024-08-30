from turtle import Screen
from player import Player
from carmanager import Cars
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Cross Road Game")
screen.tracer(0)

player = Player()
car_manager = Cars()  # Create an instance of the Cars class
score= Score()

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_back, 'Down')
screen.onkey(player.move_right, 'Right')
screen.onkey(player.move_left, 'Left')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()  # Create cars at random intervals
    car_manager.car_move()  # Move all cars across the screen

    if player.ycor() > 280 :
        player.penup()
        player.goto(0,-280)
        score.add_score()
        car_manager.faster_level()
    for car in car_manager.cars:
        if player.distance(car)<20:
            game_on=False
            score.game_over()







screen.exitonclick()
