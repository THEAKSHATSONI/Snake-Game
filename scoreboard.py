from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.score =0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=("Arial", 25, 'normal'))

    def incrace_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()


