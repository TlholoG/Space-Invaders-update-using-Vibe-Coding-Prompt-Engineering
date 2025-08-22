from turtle import Screen
from spaceship import Spaceship
from scoreboard import ScoreBoard
from aliens import Alien
from ammomanager import AmmoManager
import time
import pygame
import os

# Initialize Pygame mixer
pygame.mixer.init()
# Get the directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(BASE_DIR, "sounds/swoosh.ogg")
swoosh_sound = pygame.mixer.Sound(sound_path)
swoosh_sound.play()

screen = Screen()
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False,False)
screen.tracer(0)
screen.bgpic("src/Galaxy.gif")

screen.addshape("src/spaceship.gif")
screen.addshape("src/bullet.gif")
alien_gifs = ["src/alien1.gif", "src/alien2.gif", "src/alien3.gif", "src/alien4.gif", "src/alien5.gif", "src/alien6.gif"]
for gif in alien_gifs:
    screen.addshape(gif)

spaceship = Spaceship()
scoreboard = ScoreBoard()
alien_list = [Alien() for _ in range(30)]
ammo = AmmoManager(scoreboard)


def fire_bullet():
    x, y = spaceship.position()
    ammo.fire(x, y)


screen.listen()
screen.onkey(spaceship.move_forward, "Up")
screen.onkey(spaceship.move_back, "Down")
screen.onkey(spaceship.left_shift, "Left")
screen.onkey(spaceship.right_shift, "Right")
screen.onkey(fire_bullet, "space")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.level_speed)
    screen.update()

    for alien in alien_list:
        alien.move()
        if alien.distance(spaceship) < 30:
            scoreboard.game_over()
            game_is_on = False

    if spaceship.ycor() > 280:
        scoreboard.update_score()
        spaceship.reset_player()

    ammo.update_bullets()
    ammo.check_hits(alien_list)

screen.exitonclick()
