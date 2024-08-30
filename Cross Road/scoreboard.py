from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score=0
        self.updatescore()


    def updatescore(self):
        self.clear()
        self.goto(-150, 270)
        self.write(f'Level: {self.score}', align="center" , font=("courier", 15 , "bold"))

    def add_score(self):
        self.score+=1
        self.updatescore()


    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.write("game over.", align="center", font=("Arial", 18, "normal"))