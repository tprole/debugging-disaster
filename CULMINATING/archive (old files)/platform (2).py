#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import random
import glob
import time


# In[2]:


win = turtle.Screen()
win.setup(1195, 835)
filenames = glob.glob('./graphics/gif images/*.gif')
print(filenames)
keys = ['tara', 'sword', 'coin', 'sword-engaged', 'sword-neutral', 'cardinale-R', 'cardinale-4+', 'cardinale', 'backdrop']
imageFiles = dict(zip(keys, filenames))
for file in imageFiles:
    win.register_shape(imageFiles[file])
win.bgpic(imageFiles['backdrop'])
win.listen()


# In[3]:


platforms = {
    'first_left_x': -400,
    'first_right_x' : 0,
    'first_top_y' : 0,
    'first_bottom_y' : 0,
    'second_left_x': 0,
    'second_right_x': 0,
    'second_top_y': 0,
    'second_bottom_y': 0
}


# In[4]:


# me = turtle.Turtle()
# me.hideturtle()
# me.shape(imageFiles['tara'])
# me.penup()
# me.setposition(-450, -200)
# me.showturtle()


# In[5]:


cardinale1 = turtle.Turtle()
cardinale1.hideturtle()
cardinale1.shape(imageFiles['cardinale-R'])
cardinale1.shapesize(0.1, 0.1, 1)
cardinale1.penup()
cardinale1.setposition(100, 100)
cardinale1.showturtle()


# In[ ]:





# In[6]:


class Me(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.onPlatform = False
        self.shape(imageFiles['tara'])
        self.penup()
        self.swordEquipped = False
        self.setposition(-450, -200)

    def moveRight(self):
        self.goto(self.xcor() + 10, self.ycor())

    def moveLeft(self):
        self.goto(self.xcor() - 10, self.ycor())

    def jump(self):
        for i in range(6):
            self.goto(self.xcor(), self.ycor() + 5)
            win.onkey(self.moveLeft(), "Left")
            win.onkey(self.moveRight(), "Right")
        for i in range(6):
            self.goto(self.xcor(), self.ycor() - 5)
            win.onkey(self.moveLeft(), "Left")
            win.onkey(self.moveRight(), "Right")

    def equipSword(self):
        self.shape(imageFiles['sword-neutral'])
        self.swordEquipped = True
        self.swordEngaged = False

    def engageSword(self):
        self.shape(imageFiles['sword-engaged'])
        self.swordEngaged = True


# # In[ ]:


class Cardinale(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(imageFiles['cardinale-R'])
        self.setposition(-40, -30)

    def moveRight(self):
        self.goto(self.xcor() + 10, self.ycor())

    def moveLeft(self):
        self.goto(self.xcor() - 10, self.ycor())

    def detectSword(self):
        if mainChar.engageSword() ==True: #chagned
            self.shape(imageFiles['cardinale-4+'])
            #time.

#
# # In[7]:
#


mainChar = Me()
win.onkey(mainChar.moveLeft, "Left")
win.onkey(mainChar.moveRight, "Right")
win.onkey(mainChar.jump(), "space")

win.listen()

while True:
    
#     print ("helllo")
#


# In[ ]:





# In[1]:


win.exitonclick()

