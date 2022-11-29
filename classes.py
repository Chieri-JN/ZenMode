#################################################
# classes.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################
 
from cmu_112_graphics import *
import math
import random
import string
import dictionaries as dict
import texts_colours as col

#################################################
# Helper functions
#################################################



#################################################
# Player Class
#################################################
# TODO INCORPERATE BOUNDS
class Player():
    def __init__(self, px, py):
        self.px = px
        self.py = py
        self.score = 0

    def movePlayer(self,dx,dy):
        pass
    
    def getPowerUp(self,ix,iy):
        pass


#################################################
# Word Class
#################################################

class Word(object):
    def __init__(self, word):
        self.word = word # this is the dict key 
        # allows for 
        if self.word in dict.dictonaryMood:
            self.wordDict = dict.dictonaryMood[self.word] # this is the tuple
        else:
             self.wordDict = None
    
    def __str__(self):
        return f'{self.word}'
        
    def __repr__(self):
        return f'{self.word}'

    def getWord(self):
        return self.word

    def getWordDict(self):
        if self.word in dict.dictonaryMood:
            return dict.dictonaryMood[self.word]
        return None

    def getSynonymes(self):
        if self.getWordDict() != None:
            return self.getWordDict()[0]
        return None

    def getAntonymes(self):
        if self.getWordDict() != None:
            return self.getWordDict()[1]
        return None
    
    def drawWord(self, canvas, x, y, font, colour):
        canvas.create_text(x,y, text=f'{self.word}', font=font, fill=colour,
                           justify='center')

class Synonyme(Word): 
    def __init__(self,type):
        super.__init__(self.word)
    # will have the list here either index into tuple or something else.
    pass

class Antonyme(Word):
    pass

class WordBubble(Word):
    pass
# 
#################################################
# Button Class
#################################################

class Button: 
    def __init__(self, x, y, h, w, colour, colour2, outlinewidth, outline, text, font):
        self.width = w/2 # NOTE this /2 esnures that the inputed w/h is the
        self.height = h/2 # NOTE entire button and not the w/h from centerpoint
        self.x0 = x 
        self.y0 = y 
        self.x1 = self.x0 + self.width
        self.y1 = self.y0  + self.height
        self.colour = colour
        self.colour2 = colour2
        self.outlinewidth = outlinewidth
        self.outline = outline
        self.text = text
        self.font = font

    # 
    # def buttonPressed(self):
    #     print('Button was pressed')
    #     return self.function
    # takes in function and returns function 
    def buttonPressed(self,function):
        print('Button was pressed')
        return function

    # checks that specified object is in bounds
    def inBounds(self, x, y):
        return (self.x0 <= x <= self.x1) and (self.y0 <= y <= self.y1)
    
    # NOTE remove activefill
    def draw(self, canvas):
        canvas.create_rectangle(self.x0 - self.width,self.y0 - self.height, 
                                self.x1, self.y1, fill=self.colour, 
                                activefill=self.colour2, 
                                width = self.outlinewidth, outline=self.outline)
        if self.text != '':
            canvas.create_text(self.x0, self.y0,
                                text=self.text, font=f'{self.font}',
                                fill=self.outline)

#################################################
# Tree Class
#################################################

class Tree:
    def __init__(self,depth):
        self.branches = []
        self.depth = depth
    
    def drawBranch(self,depth):
        if depth == 0:
            return 'create draw funciton'
        else:
            self.drawBranch(depth-1)

#################################################
# MoodWheel Class
#################################################

class MoodWheel():
    def __init__(self,cx,cy,r):
        self.cx = cx
        self.cy = cy
        self.r = r 

    def drawColourWheel(self,canvas):
        canvas.create_oval(self.cx-(self.r+10),self.cy-(self.r+10),
                           self.cx+(self.r+10),self.cy+(self.r+10),
                           fill='yellow',width=5, outline='grey46')

        # Fix LATER
        for i in range(360,0):
            if i % 2 == 0:
                canvas.create_arc(self.cx-self.r,self.cy-self.r,self.cx+self.r,
                                  self.cy+self.r, fill=co.coloursList[i], 
                                  outline = '', style="pieslice",start=i,
                                  extent=i)



    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r)

#################################################
# Circle Class
#################################################
class Circle():
    def __init__(self,cx,cy,r):
        self.cx = cx
        self.cy = cy
        self.r = r

    def draw(self,canvas):
        pass

    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r)

    def circleMove(self,dx,dy):
        self.cx += dx
        self.cy += dy

    def circleDrag(self,x,y):
        self.cx += x
        self.cy += y


"""THE FOLLOWING CODE IS TEST CODE AND WILL BE REMOVED IN FINAL PRODUCT"""
def message():
    return 'Something happened!'

def appStarted(app):   
    app.buttons = []
    app.words = []
    for key in dict.dictonaryMood:
        testword = Word(key)
        app.words.append(testword)
    app.check = False

    newButton = Button(100, 200, 70, 120, 'green', 'lightGreen', 3, 'white',
                       "Button",'Krungthep 20',message())
    app.buttons.append(newButton)
    
for key in dict.dictonaryMood:
    testword = Word(key)
    # print(testword)
    # print(testword.getWord())
    # # print(testword.getWordDict())
    # print(testword.getAntonymes())
    # print('')

# testword2 = Word('Send Help')
# print(testword2.getAntonymes())

def mousePressed(app,event):

    for button in app.buttons:
        if button.inBounds(event.x, event.y) or app.check:
            print(button.buttonPressed(message()))
    return 'Not a Button!'
    
# def redrawAll(app, canvas):
#     testword.drawWord(canvas,100,50,'Krungthep 26','red')

#     for i in range(len(app.words)):
#         # note this goes in revers
#         app.words[i].drawWord(canvas,100,50 + 30*i,'Krungthep 26','red')
#     for button in app.buttons:
#         button.draw(canvas)
#     pass

def mouseMoved(app, event):
    for button in app.buttons:
        if button.inBounds(event.x, event.y):
            app.check = True
        else:
            app.check = False
            # button.buttonPressed(event, message())

    # for branch in app.branches:
    #     branch.draw(canvas)


#runApp(width=800, height=800)
    