import random
import time
import turtle



delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake game by Raman")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates
 
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.direction = "stop"

segmets = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.4("Score: 0   High Score:0", align="center", font=("Courier", 24,  "normal"))

#functions
def go_up():
    head.direction != "down"
    head.direction = "up"
     
def go_down():
    head.direction != "up"
    head.direction = "down"

def go_left():
    head.direction != "right"
    head.direction = "left"

def go_right():
    head.direction != "left"
    head.direction = "right"            

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)  

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with th border
    if head.xcor()>290 or head.xcor()<-290 or head .ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segmets:
            segment.goto(1000, 1000)

        # Clear the segments list
        segment.clear()

        # Reset the score
        score = 0 

        # Update the score display
        pen.clear()
        #pen.write("Score: 0   High Score:0", align="center", font=("Courier", 24,  "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segmets.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 5

        if score > high_score:
            score = score
        pen.clear()
        pen.write("Score: {} High Score {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



    # Move the end segments first in reverse order
    for index in range(len(segmets)-1, 0, -1):
        x = segmets[index-1].xcor()
        y = segmets[index-1].ycor()
        segmets[index].goto(x, y)

    # Move segament 0 to where the head is
    if len(segmets) > 0:
        x = head.xcor()
        y = head.ycor()
        segmets[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segmets:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

        # Clear the segments list
        segment.clear()     

    time.sleep(delay)

wn.mainloop()
