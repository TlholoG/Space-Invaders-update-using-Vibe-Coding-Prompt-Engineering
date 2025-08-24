from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, spaceship):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.level_speed = 0.1
        self.spaceship = spaceship

        # Health bar turtle
        self.health_bar = Turtle()
        self.health_bar.hideturtle()
        self.health_bar.penup()
        self.health_bar.goto(-280, 280)  # top-left

        self.update_score(0)
        self.update_health_bar()

    def update_score(self, points):
        self.clear()
        self.score += points
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def update_health_bar(self):
        self.health_bar.clear()
        self.health_bar.color("green")
        self.health_bar.begin_fill()
        width = 100 * (self.spaceship.health / 100)
        self.health_bar.goto(-280, 280)
        self.health_bar.pendown()
        self.health_bar.forward(width * 2)  # scale width
        self.health_bar.right(90)
        self.health_bar.forward(20)
        self.health_bar.right(90)
        self.health_bar.forward(width * 2)
        self.health_bar.right(90)
        self.health_bar.forward(20)
        self.health_bar.right(90)
        self.health_bar.end_fill()
        self.health_bar.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
