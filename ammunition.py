from turtle import Turtle


class Ammunition(Turtle):
    def __init__(self, x, y):
        super().__init__()
        # self.color("white")
        self.shape("src/bullet.gif")
        self.penup()
        self.goto(x, y)
        self.y_move = 17
        self.move_bullet()

    def move_bullet(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
        # Keep moving every 50 milliseconds
        if self.ycor() < 300:  # Stop bullet when it leaves the screen
            self.getscreen().ontimer(self.move_bullet, 50)
        else:
            self.hideturtle()
            self.clear()
