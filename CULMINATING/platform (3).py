# January 22, 2021
# Tara Prole
# platform.py
# To create a platform game using Turtle graphics.


# IMPORTING MODULES

import turtle
import random
import glob
import time
game = True
attempt = 0


# SETTING UP TURTLE WINDOW

win = turtle.Screen()
win.title("Debugging Disaster: Adventure through ICS3U") #displays the title of the game at the top of the window
win.colormode(255) #allows me to use rgb colours
win.setup(1195, 835) #size of background image


# STORING IMAGE FILE PATHS IN A DICTIONARY

filenames = glob.glob('./graphics/gif images/*.gif') #uses the glob module to create a list of all .gif images within the folder
keys = ['tara', 'sword', 'coin', 'sword-engaged', 'sword-neutral', 'cardinale-R', 'cardinale-4+', 'cardinale', 'backdrop', 'flip-sword-engaged', 'flip', 'flip-sword-neutral', 'skull'] #creating keys to access the images from
imageFiles = dict(zip(keys, filenames)) #creating a dictionary that allows me to reference image paths by a more memorable name
for file in imageFiles: #registers each filename as a shape for turtles to be created as
    win.register_shape(imageFiles[file])


# CREATING THE INSTRUCTIONS AT THE BOTTOM OF THE SCREEN

instructions = turtle.Turtle()
instructions.penup()
instructions.hideturtle()
instructions.color('white')
instructions.goto(-300, -400)
instructionstyle = ('Courier', 15, 'bold')
instructions.write("Arrow keys to change direction", font=instructionstyle, align='center')
instructions.goto(0, -400)
instructions.write("Space to jump", font=instructionstyle, align='center')
instructions.goto(195, -400)
instructions.write("K to attack", font=instructionstyle, align='center')


# CREATING A CLASS FOR THE MAIN CHARACTER

class Me(turtle.Turtle):
        def __init__(self):
            super().__init__()
            self.hideturtle()
            self.direction = "right"
            self.onPlatform = True
            self.shape(imageFiles['tara'])
            self.penup()
            self.swordEquipped = False
            self.jump = False
            self.movespeed = 1
            self.setposition(-450, -200)
            self.showturtle() 

        # is_on_platform()
        # @param: self
        # @return:
        # Checks if the character is on a platform, using if statements to compare the current x and y values with those stored in the platforms dictionary
        def is_on_platform(self):
            global mainY, mainX

            if mainY >= platforms['first_top_y']-5 and mainY <= platforms['first_top_y']+3 and mainX >= platforms['first_left_x'] and mainX <= platforms['first_right_x']: # First platform
                self.onPlatform = True
            elif mainY >= platforms['second_top_y']-5 and mainY <= platforms['second_top_y']+3 and mainX <= platforms['second_right_x'] and mainX >= platforms['second_left_x']: # Second platform
                self.onPlatform = True
            elif mainY >= platforms['third_top_y']-5 and mainY <= platforms['third_top_y']+3 and mainX <= platforms['third_right_x'] and mainX >= platforms['third_left_x']: # Third platform
                self.onPlatform = True
            elif mainY >= platforms['fourth_top_y']-5 and mainY <= platforms['fourth_top_y']+3 and mainX <= platforms['fourth_right_x'] and mainX >= platforms['fourth_left_x']: # Fourth platform
                self.onPlatform = True
            elif mainY >= platforms['fifth_top_y']-5 and mainY <= platforms['fifth_top_y']+3 and mainX <= platforms['fifth_right_x'] and mainX >= platforms['fifth_left_x']: # Fifth platform
                self.onPlatform = True
            elif mainY >= platforms['sixth_top_y']-5 and mainY <= platforms['sixth_top_y']+3 and mainX <= platforms['sixth_right_x'] and mainX >= platforms['sixth_left_x']: # Sixth platform
                self.onPlatform = True
            elif mainY >= platforms['seventh_top_y']-5 and mainY <= platforms['seventh_top_y']+3 and mainX <= platforms['seventh_right_x'] and mainX >= platforms['seventh_left_x']: # Sixth platform
                self.onPlatform = True
            elif mainY <= -210: # Bottom of screen
                self.onPlatform = True
            else:
                self.onPlatform = False

        # runProgram()
        # @param: self
        # @return:
        # Checks if the main character has reached the end of the final platform. If they have, writes a victory message with a text turtle and closes the while loop.
        def runProgram(self):
            global gameOn, mainY, mainX
            if mainY >= 290 and mainX >= 460:
                bigstyle = ('Courier', 200, 'bold')
                won.goto(0, 0)
                won.write('You Won', font=bigstyle, align='center')
                smallstyle = ('Courier', 50, 'bold')
                endtime = time.monotonic()
                timeTaken = endtime - startTime
                format_time = "{:.2f}".format(timeTaken)
                won.goto(0, -50)
                won.write('GLORIOUS! You took {} seconds'.format(format_time), font=smallstyle, align='center')
                print("WIN")
                gameOn = False

        # equipSword()
        # @param: self, sword
        # @return:
        # Takes in a sword turtle as a parameter, and checks that object's 'collected' attribute. If the sword has been collected, change the main character's image to one with a sword equipped.
        def equipSword(self, sword):
            if sword.collected == True:
                if self.direction == 'right':
                    self.shape(imageFiles['sword-neutral'])
                elif self.direction == 'left':
                    self.shape(imageFiles['flip-sword-neutral'])
                self.swordEquipped = True
                self.swordEngaged = False

        # gravity()
        # @param: self
        # @return:
        # Runs the is_on_platform function. Then, if the main character's onPlatform attribute is False, moves the character down by 3 pixels.
        def gravity(self):
            global mainY
            self.is_on_platform()
            if self.onPlatform != True:
                mainY = mainY - 3

        # dead()
        # @param: self, cardinale1, cardinale2
        # @return:
        # Checks if the Cardinales are in a dying state, in which case they should not affect the gameplay. If they are not in a dying state, compares the coordinates of the main character with those of the Cardinales. If they are colliding, triggers the game over sequence.
        def dead(self, cardinale1, cardinale2):
            global mainX, mainY, slash, gameOn
            if cardinale1.dying != True:
                if mainX <= cardinale1.x + 50 and mainX >= cardinale1.x - 50 and slash != True:
                    if mainY <= cardinale1.y + 25 and mainY >= cardinale1.y - 25:
                        gameOn = False
                        bigstyle = ('Courier', 200, 'bold')
                        won.goto(0, 0)
                        won.write('GAME OVER', font=bigstyle, align='center')
                        
                        won.goto(0, -50)
                        smallstyle = ('Courier', 50, 'bold')
                        endtime = time.monotonic()
                        timeTaken = endtime - startTime
                        format_time = "{:.2f}".format(timeTaken)
                        won.write('A GLORIOUS death!', font=smallstyle, align='center')
                        won.goto(0, -100)
                        won.write('You took {} seconds'.format(format_time), font=smallstyle, align='center')
                        print("LOSE")
            if cardinale2.dying != True:                     
                if mainX <= cardinale2.x + 50 and mainX >= cardinale2.x - 50 and slash != True:
                    if mainY <= cardinale2.y + 25 and mainY >= cardinale2.y - 25:
                        gameOn = False
                        won.goto(0, 0)
                        bigstyle = ('Courier', 200, 'bold')
                        won.write('GAME OVER', font=bigstyle, align='center')
                        
                        endtime = time.monotonic()
                        timeTaken = endtime - startTime
                        format_time = "{:.2f}".format(timeTaken)
                        won.goto(0, -50)
                        smallstyle = ('Courier', 50, 'bold')
                        won.write('A GLORIOUS death!', font=smallstyle, align='center')
                        won.goto(0, -100)
                        won.write('You took {} seconds'.format(format_time), font=smallstyle, align='center')
                        print("LOSE")
 

        # walls()
        # @param: self
        # @return:
        # Compares the main character's coordinates with the boundaries of the gameplay area. If they are colliding with a wall, moves the main character away from the wall.
        def walls(self):
            global mainX
            global mainY
            if mainX > platforms['right_wall']:
                mainX = mainX - 10
                self.direction = "left"
                if self.swordEquipped:
                    self.shape(imageFiles['flip-sword-neutral'])
                else:
                    self.shape(imageFiles['flip'])
            elif mainX < platforms['left_wall']:
                mainX = mainX + 10
                self.direction = "right"
                if self.swordEquipped:
                    self.shape(imageFiles['sword-neutral'])
                else:
                    self.shape(imageFiles['tara'])
            elif mainY >= platforms['top_wall']:
                mainY = mainY - 10


class Sword(turtle.Turtle):
        def __init__(self, character):
            super().__init__()
            self.penup()
            self.hideturtle()
            self.shape(imageFiles['sword'])
            self.setposition(200, -200)
            self.showturtle()
            self.x = 200
            self.y = -200
            self.character = character
            self.collected = False

        # checkCollected()
        # @param: self
        # @return:
        # Checks if the main character's coordinates are within 30 pixels to the left or right of the sword. If they are, changes the collected attribute to True, allowing the main character's equip sword function to run.
        def checkCollected(self):
            global mainX
            if self.x > mainX - 30 and self.x < mainX + 30:
                self.hideturtle()
                self.collected = True


class Cardinale(turtle.Turtle):
        def __init__(self, character, x, y, platform_left, platform_right, platform_y):
            super().__init__()
            self.penup()
            self.shape(imageFiles['cardinale-R'])
            self.direction = 'left'
            self.x = x
            self.y = y
            self.platform_left = platform_left
            self.platform_right = platform_right
            self.platform_y = platform_y
            self.setposition(self.x, self.y)
            self.character = character
            self.defeated = False
            self.movespeed = 2
            self.deathCount = 0
            self.dying = False

        # defeat()
        # @param: self
        # @return:
        # Checks if the defeated attribute has been set to True. If it has, change the image of the Cardinale to the 4+ image.
        def defeat(self):
            if self.defeated == True:
                self.dying = True
                self.shape(imageFiles['cardinale-4+'])

        # moveRight()
        # @param: self
        # @return:
        # Changes the Cardinale's x-coordinate positively by the movespeed.
        def moveRight(self):
            self.x = self.x + self.movespeed

        # moveLeft()
        # @param: self
        # @return:
        # Changes the Cardinale's x-coordinate negatively by the movespeed.
        def moveLeft(self):
            self.x = self.x - self.movespeed
        
        # prowl()
        # @param: self
        # @return:
        # This is the moving function for the Cardinale. Checks the set direction attribute and moves the turtle accordingly. Changes the direction attribute when the end of the platform being prowled upon is reached. If the deathCount attribute has escalated to 50 repetitions, changes the image to a skull and moves the Cardinale upwards away from the game screen.
        def prowl(self):
            if self.direction == 'left':
                self.moveLeft()
            elif self.direction == 'right':
                self.moveRight()
            if self.x >= self.platform_right:
                self.direction = 'left'
            elif self.x <= self.platform_left:
                self.direction = 'right'
            if self.deathCount == 50:
                self.shape(imageFiles['skull'])
                self.y = 600

    

class Coin(turtle.Turtle):
        def __init__(self, x, y):
            super().__init__()
            self.x = x
            self.y = y
            self.penup()
            self.hideturtle()
            self.goto(self.x, self.y)
            self.shape(imageFiles['coin'])
            self.showturtle()
            self.collected = False
        
        # collect()
        # @param: self
        # @return:
        # Checks for a collision between the coin and the main character. If a collision is detected, hides the coin, sets the collected attribute to True, moves the coin away from the game screen, and increases the score.
        def collect(self):
            global score, mainX, mainY
            if self.x <= mainX + 30 and self.x >= mainX - 30 and self.y >= mainY-10 and self.y <= mainY + 10:
                self.hideturtle()
                self.collected = True
                self.goto(0, 650)
                score = score + 1
                scorestamp.stamp()
                scoreturtle.write(score, font=style, align='center')
                # For testing purposes:
                # print(score)
                
# slash()
# @param:
# @return:
# Checks if the sword is equipped, then if it is, sets the slash variable to True, allowing the engageSword function to utilise the sword.
def slash():
        global slash
        if mainChar.swordEquipped:
            slash = True
            
# engageSword()
# @param:
# @return:
# Checks if the slash variable is true. If so, changes the skin to the engaged sword image. Then checks for a collision between the main character and the Cardinales, and calls the defeat function if one is detected. Then increases the slashCount by one, and if it reaches 30, resets the slashCount to 0 and sets slash to False, exiting the slashing phase.
def engageSword():
        global slash, slashCount, mainX, mainY
        if slash == True:
            if slashCount == 0:
                if mainChar.direction == 'right':
                    mainChar.shape(imageFiles['sword-engaged'])
                else:
                    mainChar.shape(imageFiles['flip-sword-engaged'])
            mainChar.swordEngaged = True
            if mainX <= cardinale1.xcor() + 100 and mainX >= cardinale1.xcor() - 100:
                if mainY <= cardinale1.ycor() + 100 and mainY >= cardinale1.ycor() - 100:
                    cardinale1.defeated = True
            if mainX <= cardinale2.xcor() + 100 and mainX >= cardinale2.xcor() - 100:
                if mainY <= cardinale2.ycor() + 100 and mainY >= cardinale2.ycor() - 100:
                    cardinale2.defeated = True
            slashCount + slashCount + 1
                
            if slashCount >= 30:
                slashCount = 0
                slash = False
                if mainChar.direction == 'right':
                    mainChar.shape(imageFiles['sword-neutral'])
                else:
                    mainChar.shape(imageFiles['flip-sword-neutral'])

# moveRight()
# @param:
# @return:
def moveRight():
        global mainX
        mainX = mainX + mainChar.movespeed
        
        
# moveLeft()
# @param:
# @return:
def moveLeft():
        global mainX
        mainX = mainX - mainChar.movespeed

        
# jump()
# @param:
# @return:
def jump():
        global mainY
        global mainX
        global jumpCount
        if not mainY >= platforms['top_wall'] and mainChar.jump == True:

            mainY = mainY + 10
            mainChar.movespeed = 10
        elif mainY >= platforms['top_wall']:
            jumpCount = 10
        if jumpCount >= 15:
            mainChar.jump = False
            jumpCount = 0
            mainChar.movespeed = 1
        
# documentcoords()
# @param:
# @return:
def documentcoords():
        print("X-coordinate: {} Y-coordinate: {}".format(mainChar.xcor(), mainChar.ycor()))

# moveChar()
# @param:
# @return:
def moveChar():
        global jumpCount, slashCount
        if mainChar.direction == "left":
            moveLeft()
        elif mainChar.direction == "right":
            moveRight()
        else:
            pass
        if mainChar.jump == True:
            jump()
            jumpCount = jumpCount + 1
        if slash == True:
            engageSword()
            slashCount = slashCount + 1

# triggerJump()
# @param:
# @return:
def triggerJump():
        if mainChar.onPlatform == True:
            mainChar.jump = True

# turnLeft()
# @param:
# @return:
def turnLeft():
        mainChar.direction = "left"
        if mainChar.swordEquipped == True:
            mainChar.shape(imageFiles['flip-sword-neutral'])
        else:
            mainChar.shape(imageFiles['flip'])

# turnRight()
# @param:
# @return:
def turnRight():
        mainChar.direction = "right"
        if mainChar.swordEquipped == True:
            mainChar.shape(imageFiles['sword-neutral'])
        else:
            mainChar.shape(imageFiles['tara'])

# stop()
# @param:
# @return:
def stop():
        mainChar.direction = "stop"


platforms = {
        'right_wall': 540,
        'left_wall': -500,
        'top_wall': 310,
        'first_left_x': 375,
        'first_right_x' : 540,
        'first_top_y' : -85,
        'second_left_x': -420,
        'second_right_x': 266,
        'second_top_y': -20,
        'third_right_x': 85,
        'third_left_x': -120,
        'third_top_y': 70,
        'fourth_top_y': 130,
        'fourth_left_x': 189,
        'fourth_right_x': 406,
        'fifth_top_y': 155,
        'fifth_right_x': -200,
        'fifth_left_x': -439,
        'sixth_left_x': -185,
        'sixth_right_x': 75,
        'sixth_top_y': 255,
        'seventh_left_x': 100,
        'seventh_right_x': 540,
        'seventh_top_y': 300
}

turtle.delay(0)
won = turtle.Turtle()
won.penup()
won.hideturtle()
style = ('Courier', 100, 'normal')
won.color('white')

highscore = 0

mainChar = Me()
sword = Sword(mainChar)
cardinale1 = Cardinale(mainChar, 100, 70, -120, 85, 70)
cardinale2 = Cardinale(mainChar, -300, 155, -439, -200, 155)
coins = []
coinLocations = [(-228, -211), (-92, -211), (34, -211), (509, -211), (379, -82), (513, -82), (157, -19), (26, -19), (-117, -19), (-251, -19), (-372, -19), (238, 131), (307, 131), (365, 131), (140, 301), (296, 301), (416, 301)]
for i in coinLocations:
    coin_x = i[0]
    coin_y = i[1]
    coins.append(Coin(coin_x, coin_y))
scoreturtle = turtle.Turtle()
highscoreturtle = turtle.Turtle()
highscorestamp = turtle.Turtle()
scorestamp = turtle.Turtle()
win.bgpic(imageFiles['backdrop'])


turtle.listen()
turtle.onkey(turnLeft, "Left")
turtle.onkey(turnRight, "Right")
turtle.onkey(stop, "Down")
turtle.onkey(triggerJump, "space")
turtle.onkey(documentcoords, "y")
turtle.onkey(slash, "k")

while game:
    attempt = attempt + 1
    
    
    
    turtle.delay(0)

    
    
    scoreturtle.hideturtle()
    scoreturtle.penup()
    scoreturtle.goto(400, 343)
    style = ('Courier', 30, 'bold')
    scoreturtle.color('white')
    scoreturtle.write('0', font=style, align='center')

    highscorestamp.shape('square')
    highscorestamp.shapesize(1, 10, 1)
    highscorestamp.color('#001735')
    highscorestamp.penup()
    highscorestamp.hideturtle()
    highscorestamp.goto(-335, 360)
    highscorestamp.stamp()

    highscorestyle = ('Courier', 20, 'bold')
    highscoreturtle.hideturtle()
    highscoreturtle.penup()
    highscoreturtle.goto(-335, 348)
    highscoreturtle.color('white')
    highscoreturtle.write('Highscore: {}'.format(highscore), font=highscorestyle, align='center')
    


    scorestamp.shape('square')
    scorestamp.shapesize(1, 2, 1)
    scorestamp.color('#001735')
    scorestamp.penup()
    scorestamp.hideturtle()
    scorestamp.goto(400, 360)
    scorestamp.showturtle()

    startTime = time.monotonic()
    mainX = -450
    mainY = -200
    if attempt > 1:
        cardinale1.x = 100
        cardinale1.y = 70
        cardinale1.defeated = False
        cardinale1.deathCount = 0
        cardinale1.shape(imageFiles['cardinale-R'])
        cardinale2.x = -300
        cardinale2.y = 155
        cardinale2.defeated = False
        cardinale2.deathCount = 0
        cardinale2.shape(imageFiles['cardinale-R'])
    jumpCount = 0

    mainChar.goto(mainX, mainY)

    cardinale1.dying = False
    cardinale1.showturtle()

    cardinale2.dying = False
    cardinale2.showturtle()
    
    sword.goto(200, -200)         

    score = 0
    gameOn = True

    slash = False
    slashCount = 0






    while gameOn:
        
        mainChar.dead(cardinale1, cardinale2)
        moveChar()
        mainChar.goto(mainX,mainY)
        mainChar.runProgram()
        cardinale1.prowl()
        cardinale2.prowl()
        cardinale1.goto(cardinale1.x, cardinale1.y)
        cardinale2.goto(cardinale2.x, cardinale2.y)
        mainChar.is_on_platform()
        if mainChar.jump != True:
            mainChar.gravity()
        mainChar.walls()
        if mainChar.swordEquipped != True:
            sword.checkCollected()
            mainChar.equipSword(sword)
        else: 
            engageSword()
            cardinale1.defeat()
            cardinale2.defeat()
        if cardinale1.dying == True:
            cardinale1.deathCount = cardinale1.deathCount + 1
        if cardinale2.dying == True:
            cardinale2.deathCount = cardinale2.deathCount + 1
        for coin in coins:
            if coin.collected == False:
                coin.collect()
                
    
    # For lag testing purposes...
    # print("There are currently {} turtles on the screen.".format(len(win.turtles())))


    if score > highscore: highscore = score

    gameInput = input("Would you like to play again? y for yes, n for no: ")
    if gameInput == "n":
        game = False
        turtle.bye()
    else:
        
        print("Starting again in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        won.clear()
        for num, i in enumerate(coins):
            location = coinLocations[num]
            i.x = location[0]
            i.y = location[1]
            i.collected = False
            i.goto(i.x, i.y)
            i.showturtle()