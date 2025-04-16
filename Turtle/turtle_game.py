import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.title("Catch the Turtle Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Score variable
score = 0

# Turtle for displaying score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 24, "bold"))

# Game turtle
game_turtle = turtle.Turtle()
game_turtle.shape("turtle")
game_turtle.color("darkgreen")
game_turtle.penup()
game_turtle.speed(0)

# Function to move turtle randomly
def move_turtle():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    game_turtle.goto(x, y)
    screen.ontimer(move_turtle, 1000)  # Call again every second

# Function to update score
def catch(x, y):
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

# Start game
game_turtle.onclick(catch)
move_turtle()

# Exit when clicked anywhere else
screen.exitonclick()
