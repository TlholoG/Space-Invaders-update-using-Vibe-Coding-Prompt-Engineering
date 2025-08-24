from turtle import Turtle

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("src/spaceship.gif")
        self.setheading(90)
        self.goto(0, -260)
        self.health = 3   # <-- NEW: spaceship starts with 3 health

    def move_forward(self):
        self.forward(15)

    def move_back(self):
        self.forward(-15)

    def right_shift(self):
        if self.xcor() <= 280:
            self.goto(self.xcor() + 20, self.ycor())

    def left_shift(self):
        if self.xcor() >= -280:
            self.goto(self.xcor() - 20, self.ycor())

    def reset_player(self):
        self.goto(0, -280)

    def take_damage(self):
        """Reduce health by 1 when hit by alien bullet"""
        self.health -= 1
        if self.health <= 0:
            return True  # spaceship destroyed
        return False
