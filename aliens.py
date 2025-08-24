from turtle import Turtle
import random
from alienammo import AlienAmmo

alien_shapes = ["src/alien1.gif", "src/alien2.gif", "src/alien3.gif",
                "src/alien4.gif", "src/alien5.gif", "src/alien6.gif"]

class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(random.choice(alien_shapes))
        self.setheading(270)
        self.goto(random.randint(-280, 280), random.randint(250, 700))

    def move(self):
        self.forward(random.randint(0, 5))

    def maybe_fire(self, alien_ammo_list):
        """Random chance for alien to fire a bullet"""
        if random.randint(1, 200) == 1:  # 1/200 chance per tick
            bullet = AlienAmmo(self.xcor(), self.ycor())
            alien_ammo_list.append(bullet)
