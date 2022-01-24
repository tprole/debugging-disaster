# January 22, 2021
# Tara Prole
# platform.py
# To create a platform game using Turtle graphics.


# IMPORTING MODULES

import turtle
import random
import glob
import time
import csv
game = True
attempt = 0


# SETTING UP TURTLE WINDOW

win = turtle.Screen()
win.title("Debugging Disaster: Adventure through ICS3U") #displays the title of the game at the top of the window
win.colormode(255) #allows me to use rgb colours
win.setup(1195, 835) #size of background image


#READING IMAGE PATHS FROM A CSV AND STORING THEM IN A DICTIONARY

reader = csv.reader(open('image_paths.csv', 'r'))
imageFiles = {}
for row in reader:
   k, v = row
   imageFiles[k] = v


# for testing purposes
# print(imageFiles)


#REGISTERING EACH SHAPE TO THE TURTLE WINDOW

for file in imageFiles: #registers each filename as a shape for turtles to be created as
    win.register_shape(imageFiles[file])


# WRITING THE INSTRUCTIONS AT THE BOTTOM OF THE SCREEN

instructions = turtle.Turtle() #creating the instructions turtle
instructions.penup() #so it doesn't draw lines under itself
instructions.hideturtle() #so there's no triangle shown
instructions.color('white')
instructions.goto(-450, -400)
instructionstyle = ('Courier', 15, 'bold') #creating the font for the instructions
#writing the instructions
instructions.write("Arrow keys to change direction", font=instructionstyle, align='center')
instructions.goto(-200, -400)
instructions.write("Space to jump", font=instructionstyle, align='center')
instructions.goto(0, -400)
instructions.write("K to attack", font=instructionstyle, align='center')
instructions.goto(350, -400)
instructions.write("Try to run the program from the top right corner!", font=instructionstyle, align='center')


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
            if mainY >= 290 and mainX >= 460: #coordinates of top right corner, which is the objective
                bigstyle = ('Courier', 200, 'bold')
                won.goto(0, 0)
                won.write('You Won', font=bigstyle, align='center') #massive YOU WON in middle of screen
                smallstyle = ('Courier', 50, 'bold')
                endtime = time.monotonic()
                timeTaken = endtime - startTime #super long decimal answer!
                format_time = "{:.2f}".format(timeTaken) #formats down to 2 decimal points.
                won.goto(0, -50)
                won.write('GLORIOUS! You took {} seconds'.format(format_time), font=smallstyle, align='center') #prints out time as a success metric for the game
                print("WIN") #prints win in terminal as part of the game log
                gameOn = False #ends while loop

        # equipSword()
        # @param: self, sword
        # @return:
        # Takes in a sword turtle as a parameter, and checks that object's 'collected' attribute. If the sword has been collected, change the main character's image to one with a sword equipped.
        def equipSword(self, sword):
            if sword.collected == True: #if the sword has been collected, then set the image to the correct orientation
                if self.direction == 'right':
                    self.shape(imageFiles['sword-neutral'])
                elif self.direction == 'left':
                    self.shape(imageFiles['flip-sword-neutral'])
                self.swordEquipped = True #sword is in hand
                self.swordEngaged = False #sword isn't being used

        # gravity()
        # @param: self
        # @return:
        # Runs the is_on_platform function. Then, if the main character's onPlatform attribute is False, moves the character down by 3 pixels.
        def gravity(self):
            global mainY
            self.is_on_platform() #check if the main character is on the platform
            if self.onPlatform != True: #if it's not, then change the mainY by -3
                mainY = mainY - 3

        # dead()
        # @param: self, cardinale1, cardinale2
        # @return:
        # Checks if the Cardinales are in a dying state, in which case they should not affect the gameplay. If they are not in a dying state, compares the coordinates of the main character with those of the Cardinales. If they are colliding, triggers the game over sequence.
        def dead(self, cardinale1, cardinale2):
            global mainX, mainY, slash, gameOn
            if cardinale1.dying != True: #only runs this if the Cardinale isn't dying. avoids unwanted collisions from after killing the Cardinales so that the main character doesn't die
                if mainX <= cardinale1.x + 50 and mainX >= cardinale1.x - 50 and slash != True: #detecting collisions between the main character and Cardinale1
                    if mainY <= cardinale1.y + 25 and mainY >= cardinale1.y - 25:
                        gameOn = False #exiting the while loop
                        bigstyle = ('Courier', 200, 'bold') #big style for giant "GAME OVER" text
                        won.goto(0, 0)
                        won.write('GAME OVER', font=bigstyle, align='center')
                        
                        won.goto(0, -50)
                        smallstyle = ('Courier', 50, 'bold') #small style for the small print after GAME OVER
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
            if mainX > platforms['right_wall']: #if the x is greater than the coords of the right wall, it's hit the right wall and moves back 10x
                mainX = mainX - 10
                self.direction = "left" #sets the direction to left so it bounces
                if self.swordEquipped: 
                    self.shape(imageFiles['flip-sword-neutral']) #flips the image to match the direction
                else:
                    self.shape(imageFiles['flip'])
            elif mainX < platforms['left_wall']: #if the x is less than the coords of the left wall, it's hit the left wall and moves forward 10x
                mainX = mainX + 10
                self.direction = "right" #sets the direction to right so it bounces
                if self.swordEquipped:
                    self.shape(imageFiles['sword-neutral']) #flips the image to match the direction
                else:
                    self.shape(imageFiles['tara'])
            elif mainY >= platforms['top_wall']: #if the y is greater than the coords of the top wall, it's hit the top wall and moves down 10y
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
            self.penup() #so they don't draw a line behind them for the entire game!
            self.shape(imageFiles['cardinale-R']) #shape to the R image
            self.direction = 'left' #the Cardinales start out going left
            self.x = x #the starting x-coordinate determined in the parameters of the class
            self.y = y #the starting y-coordinate determined in the parameters of the class
            self.platform_left = platform_left #the x-cooredinate of the left hand side of the platform the Cardinale will be prowling
            self.platform_right = platform_right #the x-coordinate of the right hand side of the platform the Cardinale will be prowling
            self.platform_y = platform_y #the y-coordinate of the platform the Cardinale will be prowling
            self.setposition(self.x, self.y) #moving the cardinale to its initial position
            self.character = character #the character that the enemy will be interacting with
            self.defeated = False #the enemy has not been defeated yet, so its interactions have consequence
            self.movespeed = 2 #speed of the enemy
            self.deathCount = 0 #used for keeping the enemy on the screen for a short period of time after defeated; right now, the enemy has not been defeated so this is 0
            self.dying = False #also used for keeping the enemy on the screen. False as the character has not defeated the enemy

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
            if self.direction == 'left': #moves in the correct direction according to the attribute
                self.moveLeft()
            elif self.direction == 'right':
                self.moveRight()
            if self.x >= self.platform_right: #changes direction if it hits the end of the platform
                self.direction = 'left'
            elif self.x <= self.platform_left:
                self.direction = 'right'
            if self.deathCount == 50: #when it dies the image changes to a skull and it moves upwards
                self.shape(imageFiles['skull'])
                self.y = 600

    

class Coin(turtle.Turtle):
        def __init__(self, x, y):
            super().__init__()
            self.x = x #the x-coordinate the coin will start at
            self.y = y #the y-coordinate the coin will start at
            self.penup()
            self.hideturtle()
            self.goto(self.x, self.y) #going to the starting position
            self.shape(imageFiles['coin']) #setting correct image
            self.showturtle()
            self.collected = False #has not been collected yet, this allows it to be collected right now
        
        # collect()
        # @param: self
        # @return:
        # Checks for a collision between the coin and the main character. If a collision is detected, hides the coin, sets the collected attribute to True, moves the coin away from the game screen, and increases the score.
        def collect(self):
            global score, mainX, mainY
            if self.x <= mainX + 30 and self.x >= mainX - 30 and self.y >= mainY-10 and self.y <= mainY + 10: #detecting collision with main character
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
            if mainX <= cardinale1.xcor() + 100 and mainX >= cardinale1.xcor() - 100: #collision between main character and cardinale1
                if mainY <= cardinale1.ycor() + 100 and mainY >= cardinale1.ycor() - 100:
                    cardinale1.defeated = True
            if mainX <= cardinale2.xcor() + 100 and mainX >= cardinale2.xcor() - 100: #collision between main character and cardinale2
                if mainY <= cardinale2.ycor() + 100 and mainY >= cardinale2.ycor() - 100:
                    cardinale2.defeated = True
            slashCount + slashCount + 1
                
            if slashCount >= 30: #if the slashCount exceeds 30, exit from the slashing state and revert to a neutral sword state
                slashCount = 0
                slash = False
                if mainChar.direction == 'right':
                    mainChar.shape(imageFiles['sword-neutral'])
                else:
                    mainChar.shape(imageFiles['flip-sword-neutral'])

# moveRight()
# @param:
# @return:
# Adds the main character's movespeed to the main x coordinate. This will allow the character to move right when the goto() command is triggered in the animation loop.
def moveRight():
        global mainX
        mainX = mainX + mainChar.movespeed
        
        
# moveLeft()
# @param:
# @return:
# Subtracts the main character's movespeed from the main x coordinate. This will allow the character to move left when the goto() command is triggered in the animation loop.
def moveLeft():
        global mainX
        mainX = mainX - mainChar.movespeed

        
# jump()
# @param:
# @return:
# If the main character's jumping attribute is true, increases the mainY by 10. This allows the character to move upwards when the goto() command is triggered in the animation loop.
def jump():
        global mainY, mainX, jumpCount
        if not mainY >= platforms['top_wall'] and mainChar.jump == True:
            mainY = mainY + 10 #increase mainY to move up on next moving phase
            mainChar.movespeed = 10 #increases the speed to allow jumping between platforms
        elif mainY >= platforms['top_wall']: #if the character hits the top wall, stop jumping
            jumpCount = 15
        if jumpCount >= 15: #when the jump is finished, change speed back and stop jumping
            mainChar.jump = False
            jumpCount = 0
            mainChar.movespeed = 1
        
# documentcoords()
# @param:
# @return:
# Function mainly drafted for testing purposes, prints out the x and y coordinates of the main character.
def documentcoords():
        print("X-coordinate: {} Y-coordinate: {}".format(mainChar.xcor(), mainChar.ycor()))

# moveChar()
# @param:
# @return:
# Combines all movement-related functions into one easily callable function. If the main character's direction attribute is left, moveLeft is called. Likewise for moveRight. If the jump attribute is true, triggers the jump command and increases the jumpCount by 1, allowing the jump sequence to be finite yet smooth.
def moveChar():
        global jumpCount, slashCount
        if mainChar.direction == "left":
            moveLeft()
        elif mainChar.direction == "right":
            moveRight()
        if mainChar.jump == True:
            jump()
            jumpCount = jumpCount + 1
        if slash == True:
            engageSword()
            slashCount = slashCount + 1

# triggerJump()
# @param:
# @return:
# Checks if the onPlatform attribute is true, and if so changes the jump attribute to True. Allows the moveChar function to smoothly move the character upwards during the movement phase of the animation loop.
def triggerJump():
        if mainChar.onPlatform == True:
            mainChar.jump = True

# turnLeft()
# @param:
# @return:
# Sets the main character's direction to left, and changes the turtle image accordingly.
def turnLeft():
        mainChar.direction = "left"
        if mainChar.swordEquipped == True:
            mainChar.shape(imageFiles['flip-sword-neutral'])
        else:
            mainChar.shape(imageFiles['flip'])

# turnRight()
# @param:
# @return:
# Sets the main character's direction to right, and changes the turtle image accordingly.
def turnRight():
        mainChar.direction = "right"
        if mainChar.swordEquipped == True:
            mainChar.shape(imageFiles['sword-neutral'])
        else:
            mainChar.shape(imageFiles['tara'])

# stop()
# @param:
# @return:
# Sets the main character's direction to stop. This ceases movement of the character.
def stop():
        mainChar.direction = "stop"


platforms = { #a dictionary used for storing coordinates of platforms in a more memorable way
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

turtle.delay(0) #Removes default lag on the turtle window.

won = turtle.Turtle() #Creates a turtle for displaying ending sequence text.
won.penup()
won.hideturtle()
won.color('white')

style = ('Courier', 100, 'normal') #Creates a style for the text turtles to use.


highscore = 0 #Sets the initial highscore to 0. This is changed at the end of each game if the score is higher than this variable's contents.

# CREATING CHARACTER TURTLES
mainChar = Me() #Creates a main character turtle from the class Me
sword = Sword(mainChar) #Creates a sword turtle from the class Sword
cardinale1 = Cardinale(mainChar, 100, 70, -120, 85, 70) #Creates the first Cardinale turtle at x 100 and y 70 from the class Cardinale
cardinale2 = Cardinale(mainChar, -300, 155, -439, -200, 155) #Creates the first Cardinale turtle at x -300 and y 155 from the class Cardinale
coins = [] #Creating a list to store coin turtles in

#A list of location tuples for each of the coins to reset to
coinLocations = [(-228, -211), (-92, -211), (34, -211), (509, -211), (379, -82), (513, -82), (157, -19), (26, -19), (-117, -19), (-251, -19), (-372, -19), (238, 131), (307, 131), (365, 131), (140, 301), (296, 301), (416, 301)]
#Creates a coin turtle from the class Coin at each location described in the tuple list
for i in coinLocations:
    coin_x = i[0]
    coin_y = i[1]
    coins.append(Coin(coin_x, coin_y))

# CREATING SCORE TURTLES
scoreturtle = turtle.Turtle() #A turtle for displaying the current score.
scorestamp = turtle.Turtle() #A turtle for stamping over the current score to allow a new one to be written over top of it.
highscoreturtle = turtle.Turtle() #A turtle for displaying the highscore.
highscorestamp = turtle.Turtle() #A turtle for stamping over the highscore to allow a new one to be written over top of it.


# CHANGING BACKGROUND IMAGE
win.bgpic(imageFiles['backdrop'])


# KEYBOARD COMMANDS
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

    #Initialises the score stamp
    scorestamp.shape('square')
    scorestamp.shapesize(1, 2, 1)
    scorestamp.color('#001735')
    scorestamp.penup()
    scorestamp.hideturtle()
    scorestamp.goto(400, 360)
    scorestamp.showturtle()

    #Starts out by writing the score as 0
    scoreturtle.hideturtle()
    scoreturtle.penup()
    scoreturtle.goto(400, 343)
    style = ('Courier', 30, 'bold')
    scoreturtle.color('white')
    scoreturtle.write('0', font=style, align='center')

    #Initialises the high score stamp
    highscorestamp.shape('square')
    highscorestamp.shapesize(1, 10, 1)
    highscorestamp.color('#001735')
    highscorestamp.penup()
    highscorestamp.hideturtle()
    highscorestamp.goto(-335, 360)
    highscorestamp.stamp()

    #Writes the high score from the variable defined above
    highscorestyle = ('Courier', 20, 'bold')
    highscoreturtle.hideturtle()
    highscoreturtle.penup()
    highscoreturtle.goto(-335, 348)
    highscoreturtle.color('white')
    highscoreturtle.write('Highscore: {}'.format(highscore), font=highscorestyle, align='center')

    startTime = time.monotonic() #storing the start time to gain the duration of gameplay later on
    
    #SETTING MAIN CHARACTER COORDINATES
    mainX = -450
    mainY = -200
    jumpCount = 0 #resetting any jumps

    #MOVING THE MAIN CHARACTER TO THE STARTING LOCATION
    mainChar.goto(mainX, mainY)

    #MOVING THE SWORD TO THE STARTING LOCATION
    sword.goto(200, -200)    

    #RESETTING COORDINATES, SHAPES AND ATTRIBUTES FOR FURTHER ATTEMPTS
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
        cardinale1.dying = False
        cardinale1.showturtle()
        cardinale2.dying = False
        cardinale2.showturtle()

         
    #SETTING GAME VARIABLES
    score = 0
    gameOn = True

    #INITIALISING SLASH MECHANICS
    slash = False
    slashCount = 0


    #MAIN LOOP
    while gameOn:
        mainChar.dead(cardinale1, cardinale2) #checks if the main character is dead
        moveChar() #sets the main character's coordinates to move to
        mainChar.goto(mainX,mainY) #moves to those set coordinates
        mainChar.runProgram() #checks if the objective has been reached
        cardinale1.prowl() #sets the first cardinale's coordinates to move to
        cardinale2.prowl() #sets the second cardinale's coordinates to move to
        cardinale1.goto(cardinale1.x, cardinale1.y) #moves the first cardinale
        cardinale2.goto(cardinale2.x, cardinale2.y) #moves the second cardinale
        mainChar.is_on_platform() #sets onPlatform attribute to match the status of the main character's platform stance
        if mainChar.jump != True: #if the character is not jumping, check for gravity to act on it
            mainChar.gravity()
        mainChar.walls() #check for collisions with the walls and act accordingly
        if mainChar.swordEquipped != True: #if the sword has not been collected yet, check for its collection and equip it when it has been collected
            sword.checkCollected()
            mainChar.equipSword(sword)
        else: 
            engageSword() #engage the sword if it is being triggered
            cardinale1.defeat() #check if the cardinales have been slashed and if so trigger their defeats
            cardinale2.defeat()
        if cardinale1.dying == True: #keeps the cardinales on the screen for a certain amount of repetitions after they are slashed
            cardinale1.deathCount = cardinale1.deathCount + 1
        if cardinale2.dying == True:
            cardinale2.deathCount = cardinale2.deathCount + 1
        for coin in coins: #going through each coin
            if coin.collected == False: #if it hasn't been collected yet
                coin.collect() #detect if it's been collected and act on that
                
    
    # For lag testing purposes...
    # print("There are currently {} turtles on the screen.".format(len(win.turtles())))


    if score > highscore: highscore = score #if the score achieved in the game is higher than the highscore, set the highscore to the new highscore!

    #TERMINAL INPUT TO PLAY AGAIN
    gameInput = input("Would you like to play again? y for yes, n for no: ")
    if gameInput == "n": #if the input is 'n', end the loop and close the turtle window
        game = False
        turtle.bye()
    else:
        print("Starting again in 3...") #timer to give player time to return to the turtle window before playing again
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        won.clear()
        for num, i in enumerate(coins): #reset the locations of all the coins
            location = coinLocations[num] #storing the tuple from the list in a variable
            i.x = location[0] #x location from tuple
            i.y = location[1] #y location from tuple
            i.collected = False #resetting the collected attribute so the coins can be re-collected
            i.goto(i.x, i.y) #go to the locations from the tuple
            i.showturtle() #show the coin