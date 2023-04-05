# Import turtle module
import turtle

# initialize window
window = turtle.Screen()  # initialize Window for the Game.
window.title("BingPong by Goondy")  # make a title for the window
window.bgcolor("black")  # set background color for the window
window.setup(width=800, height=600)  # set dimensions for the window
window.tracer(0)  # stops window from updating automatically

# madrab1
madrab1 = turtle.Turtle()  # initialize Turtle object
madrab1.speed(0)  # set the speed of madrab to be maximum
madrab1.shape("square")  # select shape of madrab to be square
madrab1.color("blue")  # select color of madrab to be blue
madrab1.penup()  # stop madrab from drawing lines
madrab1.goto(-350, 0)  # initialize position of madrab1 on the screen
madrab1.shapesize(stretch_wid=6, stretch_len=1)  # stretch shape to get proper size

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("green")
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=6, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

# score:
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)


# functions:
def madrab1_up():
    y = madrab1.ycor()  # get y coordinate of madrab1
    y += 20  # increased y by 20 to move up
    madrab1.sety(y)  # set value of new y


def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keyboard bindings:
window.listen()  # tell window to expect input
window.onkeypress(madrab1_up, "w")  # when press "w" madrab1 moving up
window.onkeypress(madrab1_down, "s")
window.onkeypress(madrab2_up, "Up")
window.onkeypress(madrab2_down, "Down")

# main game loop:
while True:
    window.update()  # Update screen every time loop run
    # movement of the ball
    ball.setx(ball.xcor() + ball.dx)  # ball will move dx on x-axis every run of loop
    ball.sety(ball.ycor() + ball.dy)  # ball will move dy on y-axis every run of loop

    # border check:
    if ball.ycor() > 290:  # if ball reaches border of window
        ball.sety(290)
        ball.dy *= -1  # reverse direction of ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)  # return ball to origin
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player1 : {}    player2 : {} ".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player1 : {}    player2 : {} ".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))

    # ball collision
    if 340 < ball.xcor() < 350 and madrab2.ycor() - 50 < ball.ycor() < madrab2.ycor() + 50:
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and madrab1.ycor() - 50 < ball.ycor() < madrab1.ycor() + 50:
        ball.setx(-340)
        ball.dx *= -1
