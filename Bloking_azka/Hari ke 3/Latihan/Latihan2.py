import turtle

def draw_rectangle(ttl, x, y, width, height, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.end_fill()
    ttl.penup()

def draw_triangle(ttl, x1, y1, x2, y2, x3, y3, color):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.end_fill()
    ttl.penup()

def draw_trapezoid(ttl, x1, y1, x2, y2, x3, y3, x4, y4, color):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x4, y4)
    ttl.goto(x1, y1)
    ttl.end_fill()
    ttl.penup()

def draw_parallelogram(ttl, x1, y1, x2, y2, x3, y3, x4, y4, color):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x4, y4)
    ttl.goto(x1, y1)
    ttl.end_fill()
    ttl.penup()

def draw_pentagon(ttl, x, y, size, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(5):
        ttl.forward(size)
        ttl.right(72)
    ttl.end_fill()
    ttl.penup()

turtle.setup(800, 600)
screen = turtle.Screen()
screen.bgcolor("white")

joe = turtle.Turtle()
joe.speed(1)  # Set the drawing speed

# Draw the shapes
draw_rectangle(joe, -200, 100, 100, 50, "red")
draw_triangle(joe, -50, 50, 0, 150, 50, 50, "yellow")
draw_trapezoid(joe, 100, 50, 150, 150, 250, 150, 200, 50, "green")
draw_parallelogram(joe, -200, -150, -100, 0, 0, -50, -100, -200, "blue")
draw_pentagon(joe, 100, -150, 80, "purple")

joe.hideturtle()
turtle.done()