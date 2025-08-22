from ammunition import Ammunition
import pygame
import os

# Initialize mixer if not already
pygame.mixer.init()

# Get path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(BASE_DIR, "sounds/swoosh.ogg")  # or swoosh.ogg

# Load swoosh sound once
swoosh_sound = pygame.mixer.Sound(sound_path)

class AmmoManager:
    def __init__(self, scoreboard):
        self.bullets = []
        self.scoreboard = scoreboard

    def fire(self, x, y):
        bullet = Ammunition(x, y)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            if bullet.isvisible():
                bullet.move_bullet()
            else:
                self.bullets.remove(bullet)

    def check_hits(self, aliens):
        # points = 0
        for bullet in self.bullets[:]:
            for alien in aliens[:]:
                if bullet.distance(alien) < 45:
                    swoosh_sound.play()
                    bullet.hideturtle()
                    alien.hideturtle()
                    self.bullets.remove(bullet)
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
                    elif alien.shape() == "src/alien7.gif":
                        points = 70
                    else:
                        points = 0

                    aliens.remove(alien)
                    self.scoreboard.update_score(points=points)
                    break  # Exit inner loop to avoid modifying list during iteration
