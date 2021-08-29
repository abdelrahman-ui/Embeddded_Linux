# ========================================================================= #
# ===================   * - Ping_Bong_App               =================== #
# ===================   * - Author : Abdelrahman_Magdy  =================== #
# ===================   * - Created: 5 / 5 / 2021       =================== #
# ========================================================================= #

# Imported Turtle Module
import turtle

# Creat Screen
wind = turtle.Screen()

# Name The Screen
wind.title("Ping Bong By Abdelrahman ")

# Color of backgroun of Screen
wind.bgcolor("black")

# Size Of Screen
wind.setup(width=800,height=600)

# Stop updating Atomatically
wind.tracer(0)

# Madrab_1
madrab1=turtle.Turtle()                                     # Madrab_1 is Turtel object
madrab1.speed(0)                                            # Speed Too Fast No delay
madrab1.shape("square")                                     # Shap is square
madrab1.color("blue")                                       # Color
madrab1.penup()                                             # No Drawing when move
madrab1.goto(-350,0)                                        # The Position of madrab_1
madrab1.shapesize(stretch_wid=5,stretch_len=1)              # Size of shape

# Madrab_2
madrab2=turtle.Turtle()                                     # Madrab_1 is Turtel object
madrab2.speed(0)                                            # Speed Too Fast No delay
madrab2.shape("square")                                     # Shap is square
madrab2.color("red")                                        # Color
madrab2.penup()                                             # No Drawing when move
madrab2.goto(350,0)                                         # The Position of madrab_2
madrab2.shapesize(stretch_wid=5,stretch_len=1)              # Size of shape

# Ball
Ball=turtle.Turtle()                                     # Madrab_1 is Turtel object
Ball.speed(0)                                            # Speed Too Fast No delay
Ball.shape("circle")                                     # Shap is square
Ball.color("white")                                      # Color
Ball.penup()                                             # No Drawing when move
Ball.goto(0,0)                                           # The Position of Ball
Ball.dx = 0.19                                           # Change in x by value pics
Ball.dy = 0.19                                           # Change in y by value pics

# Score
Score_Player_1=0
Score_Player_2=0
Score=turtle.Turtle()
Score.speed(0)
Score.color("white")
Score.penup()
Score.hideturtle()
Score.goto(0,260)
Score.write("Player_1 : 0 Player_2 : 0",align="center",font=("Courier",24,"normal"))

#functions
def Madrab1_up():
    y=madrab1.ycor()                      # The y Coordinatein the screen
    y += 20                               # to go up 20 pics
    madrab1.sety(y)                       # the new coordinate of madrab 1 in y

def Madrab1_Down():
    y=madrab1.ycor()                      # The y Coordinatein the screen
    y -= 20                               # to go up 20 pics
    madrab1.sety(y)
    # the new coordinate of madrab 1 in y

def Madrab2_up():
    y = madrab2.ycor()                        # The y Coordinatein the screen
    y += 20                                   # to go up 20 pics
    madrab2.sety(y)                           # the new coordinate of madrab 1 in y

def Madrab2_Down():
    y=madrab2.ycor()                       # The y Coordinatein the screen
    y -= 20                                # to go up 20 pics
    madrab2.sety(y)                        # the new coordinate of madrab 1 in y



# keyboard bindings ---> madrab move up and down
wind.listen()                                   # wait the press from keyboard
wind.onkeypress(Madrab1_up,"w")                 # When you have w from keyboard do func of up
wind.onkeypress(Madrab1_Down,"s")               # When you have S from keyboard do func of Dowen
wind.onkeypress(Madrab2_up,"Up")                # When you have Up from keyboard do func of up
wind.onkeypress(Madrab2_Down,"Down")            # When you have Down from keyboard do func of Dowen

# Move The Ball inside screen on x and y





# GAME loop
while True :
    # Updata Screen to not close every time loop run
    wind.update()

    # move ball
    Ball.setx(Ball.xcor() + Ball.dx)                # Set the new position after change in x
    Ball.sety(Ball.ycor() + Ball.dy)                # Set the new position after change in y

    # border check to not go out of screen
    # in y
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy *=-1                    #Reverse Direction

    if Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy *=-1

    # in x
    if Ball.xcor()>390:
        Ball.goto(0,0)                  # return to center
        Ball.dx *=-1
        Score_Player_1 += 1
        Score.clear()                       # Delet the old text
        Score.write("Player_1 : {} Player_2 : {}".format(Score_Player_1,Score_Player_2), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor()<-390:
        Ball.goto(0,0)
        Ball.dx *=-1
        Score_Player_2 += 1
        Score.clear()
        Score.write("Player_1 : {} Player_2 : {}".format(Score_Player_1, Score_Player_2), align="center",font=("Courier", 24, "normal"))


    # Ball with madrab2
    if (Ball.xcor()>340 and Ball.xcor() <350) and (Ball.ycor() < madrab2.ycor() + 40 and Ball.ycor() >madrab2.ycor() -40  ):
        Ball.setx(340)
        Ball.dx *=-1

   # Ball with madrab1
    if (Ball.xcor()<-340 and Ball.xcor() >-350) and (Ball.ycor() < madrab1.ycor() + 40 and Ball.ycor() >madrab1.ycor() -40  ):
        Ball.setx(-340)
        Ball.dx *=-1



