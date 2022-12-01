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
import drawings as dr

#################################################
# Helper functions
#################################################

def branchPoint(startx,starty,h,dir):
    xl = math.cos(math.radians(60)) * h
    yl = math.sin(math.radians(60)) * h
    newy = starty + yl
    if dir == 'right':
        newx = startx + xl
    elif dir == 'left':
        newx = startx - xl
    return (newx,newy)

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
        self.px += dx
        self.py += dy
    
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
    def __init__(self,word,cx,cy,r,colour,width,outline):
        # super().__init__(cx)
        self.word = word
        self.cx = cx
        self.cy = cy
        self.r = r
        self.colour = colour
        self.width = width
        self.outline = outline

    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r-16)

    def draw(self,canvas,font):
        canvas.create_oval(self.cx-self.r,self.cy-self.r,
                           self.cx+self.r,self.cy+self.r,
                           fill=self.colour,width=self.width, outline=self.outline,
                           text=f'{self.word}', font=font)

    def wordBubblePressed(self):
        return self.word

    def Move(self,dx,dy):
        self.cx += dx
        self.cy += dy

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
        canvas.create_text(self.x0, self.y0,
                                text=self.text, font=f'{self.font}',
                                fill=self.outline)

#################################################
# Tree Class
#################################################

class Tree:
    def __init__(self,depth,startx,starty):
        self.branches = []
        self.depth = depth
        self.startx = startx
        self.starty = starty
    
    def drawBranch(self,canvas,depth,x0,y0,x1,y1,step=0):
        if depth == 0:
            dr.drawBranch(canvas,x0,y0,x1,y1)
        else:

            # Main branch
            self.drawBranch(depth+1)

            # left branch
            self.drawBranch(depth+1)

            # Right branch
            self.drawBranch(depth+1)


def drawFreddyFractal(app, canvas, level, x, y, radius, step=0):
    if level == 0:
        # drawFreddyHead(app, canvas, x, y, radius, step)
        drawBranch(app,canvas,x,y,radius)
    else:
        # main head
        drawFreddyFractal(app, canvas, level-1, x, y, radius, step+1)

        # left ear/head
        drawFreddyFractal(app, canvas, level-1, x-(radius*1.1),
                          y-radius, radius/2, step+2)

        # right ear/head
        drawFreddyFractal(app, canvas, level-1, x+(radius*1.1), 
                          y-radius, radius/2, step+3)

#################################################
# Pieslice Class
#################################################

class PieSlice():
    def __init__(self,cx,cy,r,colour,start):
        self.cx = cx
        self.cy = cy
        self.r = r 
        self.colour = colour
        self.start = start # = i

    def draw(self,canvas):
         canvas.create_arc(self.cx-self.r,self.cy-self.r, self.cx+self.r,
                                  self.cy+self.r, fill=self.colour, 
                                  outline = '', style="pieslice",start=self.start,
                                  extent=360-self.start)
    def getColour(self):
        return self.colour
    
    def inBounds(self):
        # figure out
        pass

#################################################
# MoodWheel Class
#################################################

class MoodWheel():
    def __init__(self,cx,cy,r):
        self.cx = cx
        self.cy = cy
        self.r = r 
        self.listOfSlices = []
        self.width = 10

    def drawColourWheel(self,canvas):
        canvas.create_oval(self.cx-(self.r+10),self.cy-(self.r+10),
                           self.cx+(self.r+10),self.cy+(self.r+10),
                           fill='grey60',width=self.width, outline='grey26')

        # Fix LATER
        for i in range(0,len(col.coloursList)):
            degree = PieSlice(self.cx, self.cy, self.r+self.width/2,col.coloursList[i],i)
            # canvas.create_arc(self.cx-self.r,self.cy-self.r, self.cx+self.r,
            #                       self.cy+self.r, fill=col.coloursList[i], 
            #                       outline = '', style="pieslice",start=i,
            #                       extent=360-i)
            degree.draw(canvas)
            self.listOfSlices.append(degree)

            
    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r-16)

#################################################
# Shape Classes
#################################################
class Circle():
    def __init__(self,cx,cy,r, colour,width,outline):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.colour = colour
        self.width = width
        self.outline = outline

    def draw(self,canvas):
        canvas.create_oval(self.cx-self.r,self.cy-self.r,
                           self.cx+self.r,self.cy+self.r,
                           fill=self.colour,width=self.width, outline=self.outline)

    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r)

    def Move(self,dx,dy):
        self.cx += dx
        self.cy += dy

    def Drag(self,x,y):
        self.cx = x
        self.cy = y

class Dot(Circle):
    # use equality and isinstance
    pass

class Box():
    def __init__(self,x, y, h, w, colour, outlinewidth, outline):
        self.width = w/2 # NOTE this /2 esnures that the inputed w/h is the
        self.height = h/2 # NOTE entire button and not the w/h from centerpoint
        self.x0 = x 
        self.y0 = y 
        self.x1 = self.x0 + self.width
        self.y1 = self.y0  + self.height
        self.colour = colour
        self.outlinewidth = outlinewidth
        self.outline = outline
    
    # NOTE remove activefill
    def draw(self, canvas):
        canvas.create_rectangle(self.x0 - self.width,self.y0 - self.height, 
                                self.x1, self.y1, fill=self.colour,  
                                width = self.outlinewidth, outline=self.outline)

    def inBounds(self, x, y):
        return (self.x0 <= x <= self.x1) and (self.y0 <= y <= self.y1)






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
                       "Button",'Krungthep 20')
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
#     mood1 = MoodWheel(app.width/2-300,550,190)
#     mood1.drawColourWheel(canvas)
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


# runApp(width=800, height=800)
    