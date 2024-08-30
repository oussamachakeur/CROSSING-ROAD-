from turtle import Turtle
import random

class Cars:

    def __init__(self):
        self.cars = []
        self.DISTANCE =10

    def create_car(self):
        # Randomly decide when to create a new car
        random_chance = random.randint(1, 2)
        if random_chance == 1:
            random_color = ['blue', 'yellow', 'orange', 'pink', 'red', 'green']
            y_positions = [0, 70, 110, 180, 210, 230, -30, -70, -110, -180, -210, -230]
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.penup()
            y_pos = random.choice(y_positions)
            car.color(random.choice(random_color))
            car.goto(300, y_pos)  # Start from the right edge
            self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.backward(self.DISTANCE)  # Move car to the left
            if car.xcor() < -320:  # Remove cars that go off-screen
                car.hideturtle()
                self.cars.remove(car)

    def faster_level(self):
        self.DISTANCE+=5



