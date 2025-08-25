import time
import random
from turtle import Screen
from spaceship import Spaceship
from scoreboard import Scoreboard
from ammomanager import AmmoManager
from aliens import Alien

# ----------------- Setup -----------------
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders Turtle Edition")
screen.tracer(0)  # Turn off automatic updates

# Register shapes for spaceship + aliens
screen.register_shape("src/spaceship.gif")
for i in range(1, 8):
    screen.register_shape(f"src/alien{i}.gif")

# Initialize main game objects
spaceship = Spaceship()
scoreboard = Scoreboard(spaceship)  # ✅ pass spaceship into Scoreboard
ammo = AmmoManager(scoreboard)

# Aliens setup
alien_list = []
x_positions = [-350, -250, -150, -50, 50, 150, 250, 350]
y_positions = [200, 150, 100, 50]

for y in y_positions:
    for i, x in enumerate(x_positions):
        alien_type = (i % 7) + 1
        alien = Alien(x, y, f"src/alien{alien_type}.gif")
        alien_list.append(alien)

# ----------------- Controls -----------------
screen.listen()
screen.onkey(spaceship.go_left, "Left")
screen.onkey(spaceship.go_right, "Right")
screen.onkey(lambda: ammo.fire(spaceship.xcor(), spaceship.ycor()), "space")


# ----------------- Game Loop -----------------
def game_loop():
    """Runs one frame of the game and reschedules itself."""
    # Move aliens + random alien firing
    for alien in alien_list[:]:
        alien.move()

        # If alien collides with spaceship → instant game over
        if alien.distance(spaceship) < 30:
            scoreboard.game_over()
            return  # stop scheduling new frames

        # Alien random firing
        if random.randint(1, 150) == 1:
            ammo.alien_fire(alien.xcor(), alien.ycor())

    # Prevent spaceship from leaving top boundary
    if spaceship.ycor() > 280:
        spaceship.reset_player()

    # Update bullets (both spaceship + aliens)
    ammo.update_bullets()

    # Check bullet hits (on aliens + spaceship)
    ammo.check_hits(alien_list, spaceship)

    # Update health bar
    scoreboard.update_health_bar()

    # If spaceship health reaches 0 → game over
    if spaceship.health <= 0:
        scoreboard.game_over()
        return

    # Refresh screen + schedule next frame
    screen.update()
    screen.ontimer(game_loop, 30)  # 30ms ≈ 33 FPS


# ----------------- Start Game -----------------
screen.update()
game_loop()
screen.mainloop()
