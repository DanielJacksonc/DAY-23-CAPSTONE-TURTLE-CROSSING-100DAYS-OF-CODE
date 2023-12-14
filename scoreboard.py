from turtle import Turtle
FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.level = 1
        self.level_up()


    def level_up(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.write(f"level : {self.level}", align="left", font=FONT)

    def level_increase(self):

        self.level += 1
        self.level_up()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="left", font=FONT)


