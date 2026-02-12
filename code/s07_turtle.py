import turtle

def draw_square(turtle_obj, size = 100):
    '''Draw a square with a given size
    '''
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)

def draw_spiral(t):
    '''
    Draw one square, turn an angle, then draw another square and so on
    '''

    for i in range(36):
        draw_square(t, 50 + i * 2)
        t.left(10)

def main():
    t = turtle.Turtle()
    t.speed(0)
    draw_spiral(t)
    turtle.mainloop()

if __name__ == "__main__":
    main()


'''
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
'''