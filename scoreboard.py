from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 35, "normal")

# screen.tracer(0)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.upgrade_scoreboard()

    def upgrade_scoreboard(self):
        self.clear()
        self.goto(-150, 240)
        self.write(f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(150, 240)
        self.write(f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.upgrade_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.upgrade_scoreboard()