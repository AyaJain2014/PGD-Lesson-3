import random, pgzrun

WIDTH = 500
HEIGHT = 500
TITLE = "Alien Shooter"

alien = Actor("alien2")
alien.pos = (50, 100)
message = "Welcome to Alien Shooter"

def draw():
    screen.clear()
    screen.fill("red")
    alien.draw()
    screen.draw.text(message, center =(250,20), fontsize = 30, color = "black")

def move():
    alien.x = random.randint(50, 450)
    alien.y = random.randint(50, 450)

#mouse event
def on_mouse_down(pos):
    print("Hi !")
    global message
    if alien.collidepoint(pos):
        message = "You touched the alien"
        move()
    else:
        message = "Try again"




















pgzrun.go()