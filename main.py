from turtle import Screen
from spaceship import Spaceship
from scoreboard import ScoreBoard
from aliens import Alien
from ammomanager import AmmoManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)
screen.bgpic("src/Galaxy.gif")

screen.addshape("src/spaceship.gif")
screen.addshape("src/bullet.gif")
alien_gifs = ["src/alien1.gif", "src/alien2.gif", "src/alien3.gif",
              "src/alien4.gif", "src/alien5.gif", "src/alien6.gif"]
for gif in alien_gifs:
    screen.addshape(gif)

spaceship = Spaceship()
scoreboard = ScoreBoard(spaceship)
alien_list = [Alien() for _ in range(30)]
ammo = AmmoManager(scoreboard, spaceship)


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

    # move aliens and check for collision with spaceship
    for alien in alien_list:
        alien.move()
        if alien.distance(spaceship) < 30:
            scoreboard.game_over()
            game_is_on = False

    # spaceship reaches top
    if spaceship.ycor() > 280:
        scoreboard.update_score(0)
        spaceship.reset_player()

    # move bullets and check hits
    ammo.update_bullets()
    ammo.check_hits(alien_list)

    # update health bar
    scoreboard.update_health_bar()

    # game over if spaceship health 0
    if spaceship.health <= 0:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
