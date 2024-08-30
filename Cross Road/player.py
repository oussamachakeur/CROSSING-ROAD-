from turtle import Turtle


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(0, -280)
        self.right(280)

    def move_forward(self):
        new_y = self.ycor()+20
        self.goto(self.xcor() , new_y)

    def move_back(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() +20
        self.goto(new_x , self.ycor())

    def move_left(self):
        new_x = self.xcor() -20
        self.goto(new_x , self.ycor())

