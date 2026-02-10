import turtle
t = turtle.Turtle()
t.speed(0)

def draw_square():
    for i in range (4):
        t.forward(100)
        t.left(90)

def main():
    for i in range (36):
        draw_square()
        t.left(10)