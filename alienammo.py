from turtle import Turtle

class AlienAmmo(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.penup()
        self.goto(x, y)
        self.y_move = -12
        self.move_bullet()

    def move_bullet(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
        if self.ycor() > -300:  # stays on screen
            self.getscreen().ontimer(self.move_bullet, 50)
        else:
            self.hideturtle()
            self.clear()
