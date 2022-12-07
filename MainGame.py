import tkinter
from tkinter import filedialog, Text
import os

root= tkinter.Tk()
root.geometry('470x470')
root.title("SNAKE GAME")

def jls_extract_def():
            import turtle
            import time
            import random
            
            return turtle, time, random

def run():
        turtle, time, random = jls_extract_def()
        delay = 0.1
        
        level = 1
        # scores
        score = 0
        high_score = 0

        # screen set up
        wn = turtle.Screen()
        wn.title("Snake Game ")
        wn.bgcolor("black")
        wn.setup(width=600, height=600)
        wn.tracer(0) # screen updates off

        # snakes head
        head = turtle.Turtle()
        head.speed(0)
        head.shape("circle")
        head.color("orange")
        head.penup()
        head.goto(0,0)
        head.direction = "stop"

        # food
        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(0,100)
        segments = []

        # pen        
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("triangle")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Score: 0  High Score: 0  Level: 1", align="center", font=("Courier", 16, "normal"))


        # snake game functions
        def go_up():
            if head.direction != "down":
                head.direction = "up"

        def go_down():
            if head.direction != "up":
                head.direction = "down"

        def go_left():
            if head.direction != "right":
                head.direction = "left"

        def go_right():
            if head.direction != "left":
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


        # keybinda
        wn.listen()

        wn.onkeypress(go_up, "w")
        wn.onkeypress(go_down, "s")
        wn.onkeypress(go_left, "a")
        wn.onkeypress(go_right, "d")


        # snake game main loop
        while True:
            wn.update()

            # checking for collision border
            if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                # hiding segment                
                for segment in segments:
                    segment.goto(1000, 1000)

                # segment list clear
                segments.clear()

                # score reset
                score = 0
                # delay reset
                delay = 0.1
                # level reset
                level = 1
                pen.clear()
                pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center", font=("Courier", 16, "normal"))


            # checking for collision food            
            if head.distance(food) < 20:
                # moving food to random spot
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                food.goto(x,y)

                # segemnt addition                
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("triangle")
                new_segment.color("red")
                new_segment.penup()
                segments.append(new_segment)

                # shorting the delay
                delay -= 0.001

                # score increase
                score += 10

                if score > high_score:
                    high_score = score

                pen.clear()
                pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center", font=("Courier", 16, "normal"))


            # moving end segemnts first in reverse            
            for index in range(len(segments)-1, 0, -1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x, y)

            # moving segemnt 0 to head            
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x,y)

            move()

            # checking for head body collision            
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"

                    # hiding segments
                    for segment in segments:
                        segment.goto(1000, 1000)

                    # clearing segment list
                    segments.clear()
                    # score reset
                    score = 0
                    # delay reset
                    delay = 0.1
                    # level reset
                    level = 1
                    # updating score
                    pen.clear()

                    pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center", font=("Courier", 16, "normal"))

            # levels
            if level == 1 and score == 50:
                level += 1
                delay *= 0.9
            if level == 2 and score == 100:
                level += 1
                delay *= 0.9
            if level == 3 and score == 150:
                level += 1
                delay *= 0.9
            time.sleep(delay) 
        wn.mainloop()
        return(run)

canvas = tkinter.Canvas(root, height=465, width=450, bg="Red")
canvas.place(x=10, y=10)
label_widget=tkinter.Label(root,text="Move Front= W Key \n Move Back= S Key \n Move Left= A Key\n Move Right= D key \n\n Each time the snake eats the food it grows longer \n\n If snake's head touches its body, tail or the walls the game ends and you lose",fg="White" ,width=61, height=23,bg= "Black",bd='5')
label_widget.place(x=18,y=18)
label_widget=tkinter.Label(root,text="\nSNAKE GAME", width=26, height=2,bg="Black",bd='10',font=("Arial",20))
label_widget.place(x=18,y=23)
button_widget= tkinter.Button(root,text="PROCEED", width=20, height=3, bd='5',command = run)
button_widget.place(x=160, y=390)

try:
    root.mainloop()
except KeyboardInterrupt:
    pass

