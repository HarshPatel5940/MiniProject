import tkinter
from tkinter import filedialog, Text
import os

root= tkinter.Tk()
root.geometry('330x460')
root.title("Game Bar")
# asteroid rules page
def ast():
        import tkinter
        from tkinter import filedialog, Text
        import os
        root= tkinter.Tk()
        root.geometry('470x470')
        root.title("ASTEROIDS")
        
        canvas = tkinter.Canvas(root, height=450, width=450,bg="Blue")
        canvas.place(x=10, y=10)
        label_widget=tkinter.Label(root,text="Move Front= UP Key \n Move Back= DOWN Key \n Move Left= LEFT Key\n Move Right= RIGHT key \n Press space to shoot the asteroids. \n To direct the ship press LEFT or RIGHT\n To increase speed press UP \n When the asteroid clashes with the ship, you lose 1 life \n Losing 3 lives will mean you lose and the game ends",fg="White", width=61, height=23, bg= "Black",bd='5')
        label_widget.place(x=17,y=17)
        button_widget= tkinter.Button(root,text="PROCEED", width=20, height=3, bd='5',command=run1)
        button_widget.place(x=160, y=380)
        root.mainloop()
# snake game rules page
def snk():
        import tkinter
        from tkinter import filedialog, Text
        import os
        root= tkinter.Tk()
        root.geometry('470x470')
        root.title("SNAKE GAME")

        canvas = tkinter.Canvas(root, height=450, width=450, bg="Red")
        canvas.place(x=10, y=10)
        label_widget=tkinter.Label(root,text="Move Front= W Key \n Move Back= S Key \n Move Left= A Key\n Move Right= D key \n Each time the snake eats the food it grows longer \n If snake's head touches its body, tail or the walls the game ends and you lose",fg="White" ,width=61, height=23, bg= "Black",bd='5')
        label_widget.place(x=17,y=17)
        button_widget= tkinter.Button(root,text="PROCEED", width=20, height=3, bd='5',command=run2)
        button_widget.place(x=160, y=380)
        root.mainloop()
        
# asteroid code
def run1():
        import turtle
        import math
        import random

        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Asteroids")
        wn.setup(800, 600)
        wn.tracer(0)

        pen = turtle.Turtle()
        pen.penup()
        pen.speed(0)

        class Sprite():
            def __init__(self):
                self.x = 0
                self.y = 0
                self.heading = 0
                self.dx = 0
                self.dy = 0
                self.shape = "square"
                self.color = "white"
                self.size = 1.0
                self.active = True
                
            def update(self):
                if self.active:
                    self.x += self.dx
                    self.y += self.dy
                    
                    if self.x > 400:
                        self.x = -400
                    elif self.x < -400:
                        self.x = 400
                        
                    if self.y > 300:
                        self.y = -300
                    elif self.y < -300:
                        self.y = 300
                
            def render(self, pen):
                if self.active:
                    pen.goto(self.x, self.y)
                    pen.setheading(self.heading)
                    pen.shape(self.shape)
                    pen.shapesize(self.size, self.size, 0)
                    pen.color(self.color)
                    pen.stamp()
                    
            def is_collision(self, other):
                x = self.x-other.x
                y = self.y-other.y
                distance = ((x**2) + (y**2)) ** 0.5
                if distance < ((10 * self.size) + (10 * other.size)):
                    return True
                else:
                    return False
                    
            def goto(self, x, y):
                self.x = x
                self.y = y
                
                
        class Player(Sprite):
            def __init__(self):
                Sprite.__init__(self)
                self.shape = "triangle"
                self.lives = 3
                self.score = 0
        
            def rotate_left(self):
                self.heading += 30
                
            def rotate_right(self):
                self.heading -= 30
                
            def accelerate(self):
                ax = math.cos(math.radians(self.heading))
                ay = math.sin(math.radians(self.heading))
                self.dx += ax * 0.1
                self.dy += ay * 0.1
                
            def render(self, pen):
                if self.active:
                    pen.goto(self.x, self.y)
                    pen.setheading(self.heading)
                    pen.shape(self.shape)
                    pen.shapesize(self.size/2.0, self.size, 0)
                    pen.color(self.color)
                    pen.stamp()

        class Asteroid(Sprite):
            def __init__(self):
                Sprite.__init__(self)
                self.shape = "circle"

        class Missile(Sprite):
            def __init__(self):
                Sprite.__init__(self)
                self.shape = "circle"
                self.size = 0.2
                self.active = False

            def update(self):
                if self.active:
                    self.x += self.dx
                    self.y += self.dy
                    
                    if self.x > 400:
                        self.active = False
                    elif self.x < -400:
                        self.active = False
                        
                    if self.y > 300:
                        self.active = False
                    elif self.y < -300:
                        self.active = False
                
            def fire(self):
                if not self.active:
                    self.active = True
                    self.x = player.x
                    self.y = player.y
                    self.heading = player.heading
                    self.dx = math.cos(math.radians(self.heading)) * 1
                    self.dy = math.sin(math.radians(self.heading)) * 1

        # sprites list
        sprites = []

        # instances
        player = Player()
        sprites.append(player)

        missile = Missile()
        sprites.append(missile)
 
        # asteroid creation
        for _ in range(5):
            asteroid = Asteroid()
            x = random.randint(-375, 375)
            y = random.randint(-275, 275)
            asteroid.goto(x, y)
            dx = random.randint(-5, 5) / 20.0
            dy = random.randint(-5, 5) / 20.0 
            asteroid.dx = dx
            asteroid.dy = dy
            size = random.randint(10, 30) / 10.0
            asteroid.size = size
            sprites.append(asteroid)

        # keybinds
        wn.listen()
        wn.onkeypress(player.rotate_left, "Left")
        wn.onkeypress(player.rotate_right, "Right")
        wn.onkeypress(player.accelerate, "Up")
        wn.onkeypress(missile.fire, "space")

        # main loop for asteroid
        while True:
            # screen update
            wn.update()

            # clear pen action
            pen.clear()

            # draw score and lives
            #pen.goto is (-350,250)
            
            for i in range(player.lives):
                pen.goto(-350 + 30 * i, 225)
                pen.shape("triangle")
                pen.shapesize(0.7, 0.7, 0)
                pen.setheading(90)
                pen.stamp()
        

    
            # render and updatinng
            for sprite in sprites:
                sprite.update()
                sprite.render(pen)

            import sys
            # checking for collisions
            for sprite in sprites:
                if isinstance(sprite, Asteroid):
                    if player.is_collision(sprite):
                        player.lives -= 1
                        print(f"Lives: {player.lives}")
                        player.goto(0, 0)
                        sprite.goto(100, 100)
                        
                        if player.lives <= 0:
                            print("PLAYER DIES")
                            print('Use CTRL-D to exit')
                            print(exit)
                            exit()
                        
                    if missile.active and missile.is_collision(sprite):
                        print("ASTEROID DIES")
                        missile.active = False
                        player.score += 10
                        print(f"Player Score: {player.score}")
                        sprite.goto(100, 100)



    
    
        wn.mainloop()

# snake game code
def run2():
        def jls_extract_def():
            import turtle
            import time
            import random
            
            return turtle, time, random


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


# canvas 
canvas = tkinter.Canvas(root, height=430, width=300, bg="Purple")
canvas.place(x=15, y=15)
# mainpage buttons
button_widget= tkinter.Button(root,text="SNAKE GAME", width=30, height=5, bd='10',command=snk)
button_widget.place(x=50, y=50)
button_widget= tkinter.Button(root,text="ASTEROIDS", width=30, height=5, bd='10',command=ast)
button_widget.place(x=50, y=180)
button_widget= tkinter.Button(root,text="EXIT", width=3, height=1, bd='15',command=exit)
button_widget.place(x=50, y=375)

root.mainloop()
