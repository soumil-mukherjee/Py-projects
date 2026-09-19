import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Aishitemasu Eien ni")

# Create the turtle
t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.penup()
t.color("#ffb6c1")  # Light pink

# Draw the heart using multiple scales
for scale in range(11, 17):
    for i in range(120):

        # Calculate the angle
        angle = i * (2 * math.pi) / 120

        # Heart equation
        x = 16 * (math.sin(angle) ** 3) * scale

        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale

        # Move to the position and write the text
        t.goto(x, y)
        t.write(
            "Aishitemasu",
            align="center",
            font=("Arial", 8, "bold")
        )

# Keep the window open
turtle.done()