
import pgzrun
import random

WIDTH = 600
HEIGHT = 500

cookie = Actor("cookie")
cookie.pos = (300, 250)

score = 0


def draw():
    screen.fill((245, 222, 179))
    cookie.draw()
    screen.draw.text("score "+str(score), (20, 20), fontsize=40, color="black")


def on_mouse_down(pos):
    global score

    if cookie.collidepoint(pos):
        score += 1
        cookie.x = random.randint(50, 550)
        cookie.y = random.randint(50, 450)
    else:
        score -= 1


pgzrun.go()