from ammunition import Ammunition
from alienammo import AlienAmmo
from turtle import Turtle
import pygame
import os

pygame.mixer.init()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(BASE_DIR, "sounds/swoosh.ogg")
swoosh_sound = pygame.mixer.Sound(sound_path)


class AmmoManager:
    def __init__(self, scoreboard, spaceship):
        self.bullets = []
        self.alien_bullets = []
        self.scoreboard = scoreboard
        self.spaceship = spaceship

    def fire(self, x, y):
        bullet = Ammunition(x, y)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            if bullet.isvisible():
                bullet.move_bullet()
            else:
                self.bullets.remove(bullet)

        for bullet in self.alien_bullets[:]:
            if bullet.isvisible():
                bullet.move_bullet()
            else:
                self.alien_bullets.remove(bullet)

    def check_hits(self, aliens):
        # spaceship bullets hitting aliens
        for bullet in self.bullets[:]:
            for alien in aliens[:]:
                if bullet.distance(alien) < 45:
                    swoosh_sound.play()
                    bullet.hideturtle()
                    alien.hideturtle()
                    self.bullets.remove(bullet)

                    # scoring by alien type
                    if alien.shape() == "src/alien1.gif":
                        points = 10
                    elif alien.shape() == "src/alien2.gif":
                        points = 20
                    elif alien.shape() == "src/alien3.gif":
                        points = 30
                    elif alien.shape() == "src/alien4.gif":
                        points = 40
                    elif alien.shape() == "src/alien5.gif":
                        points = 50
                    elif alien.shape() == "src/alien6.gif":
                        points = 60
                    else:
                        points = 0

                    aliens.remove(alien)
                    self.scoreboard.update_score(points=points)
                    break

        # alien bullets hitting spaceship
        for bullet in self.alien_bullets[:]:
            if bullet.distance(self.spaceship) < 30:
                swoosh_sound.play()
                bullet.hideturtle()
                self.alien_bullets.remove(bullet)

                if self.spaceship.take_damage():
                    self.scoreboard.game_over()
