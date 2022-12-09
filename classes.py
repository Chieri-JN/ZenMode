#################################################
# classes.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################
 
from cmu_112_graphics import *
import math
import dictionaries as dict
import texts_colours as col
import drawings as dr

#################################################
# Helper functions
#################################################
def distance(x1, y1, x2, y2): 
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return math.sqrt(x + y) 

def cosineLaw(x1,y1,x2,y2,x3,y3):
    a = distance(x1,y1, x2,y2)
    b = distance(x3,y3, x1,y1)
    c = distance(x2,y2, x3,y3)
    flip = 0
    sign =1
    if y3>y2 and x3 < x1: 
        flip = 360
        sign= -1
    elif y3 > y2 and x1 <= x3 <= x2: 
        flip = 360
        sign = -1
    else:
        flip +=0
    if a != 0 and b != 0: 
        step1 = (a**2 + b**2 - c**2)/ (2*a*b)
        gamma =  math.acos(step1)
        return math.degrees(gamma)*sign + flip
    return 0

# taken from 15-112 homework 
import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
#################################################
# Player Class
#################################################

class Player():
    def __init__(self,app,px, py):
        self.px = px
        self.py = py
        self.pHeight = 186
        self.pWidth = 140
        # change var name
        # player radius dimensions
        self.pHr = self.pHeight/2
        self.pWr = self.pWidth/2
        self.score = 0
        self.idleSprites = dr.PlayerSprites(app)[0]
        self.idleLSprites = dr.PlayerSprites(app)[1]
        self.jumpSprites = dr.PlayerSprites(app)[2]
        self.mRSprites = dr.PlayerSprites(app)[3]
        self.mLSprites = dr.PlayerSprites(app)[4]

    def drawPlayer(self,canvas,spriteState,spriteCount):
        if spriteState == 'idle':
            sprite = self.idleSprites[spriteCount%len(self.idleSprites)]
            canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(sprite))
        elif spriteState == 'idleL':
            sprite = self.idleLSprites[spriteCount%len(self.idleLSprites)]
            canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(sprite))
        elif spriteState == 'jump':
            sprite = self.jumpSprites[spriteCount%len(self.jumpSprites)]
            canvas.create_image(self.px, self.py-125, image=ImageTk.PhotoImage(sprite))

        elif spriteState == 'right':
            sprite = self.mRSprites[spriteCount%len(self.mRSprites)]
            canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(sprite))
        elif spriteState == 'left':
            sprite = self.mLSprites[spriteCount%len(self.mLSprites)]
            canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(sprite))


    def movePlayer(self,dx,dy):
        self.px += dx
        self.py += dy
    
    def inPlayerBounds(self,x,y):
        return ((self.px - self.pWr <= x <= self.px + self.pWr) and
                (self.py - self.pHr == x <= self.py + self.pHr))

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

    def setWord(self,word):
        self.word = word

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

    def checkType(self):
        if self.word in dict.dictionaryType['Negative']:
            return 'Negative'
        elif self.word in dict.dictionaryType['Positive']:
            return 'Positive'
        else:
            return None

class WordBubble(Word):
    def __init__(self,word):
        # cx,cy,r,colour,width,outline
        # super().__init__(cx)
        self.word = word
        self.cx = 0
        self.cy = 0
        self.r = 0
        self.colour = 'white'
        self.width = 0
        self.outline = 'black'
        self.speedx = 0
        self.speedy = 0

    def draw(self,canvas,font,cx,cy,r,colour,width,outline):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.colour = colour
        self.width = width
        self.outline = outline
        canvas.create_oval(self.cx-self.r,self.cy-self.r,
                           self.cx+self.r,self.cy+self.r,
                           fill=self.colour,width=self.width, outline=self.outline,
                          )
        canvas.create_text(self.cx,self.cy,text=f'{self.word}', font=font, fill=self.outline)

    def __eq__(self, other):
        return (isinstance(other, WordBubble) and (self.word == other.word))

    def wordBubblePressed(self):
        return self.word
    
    def getColour(self):
        return self.colour

    def Move(self,dx,dy):
        self.cx += dx 
        self.cy += dy

    def setSpeed(self,vx,vy):
        self.speedx = vx
        self.speedy = vy
    
    def collision(self,other):
        self.speedx,other.speedx = other.speedx, self.speedx
        self.speedy,other.speedy = other.speedy, self.speedy

    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r)

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

    # takes in function and returns function 
    def buttonPressed(self,function):
        print('Button was pressed')
        return function

    # checks that specified object is in bounds
    def inBounds(self, x, y):
        return ((self.x0- self.width <= x <= self.x1) and 
                (self.y0 - self.height <= y <= self.y1))
    
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
# MoodWheel Class
#################################################

class MoodWheel():
    def __init__(self,cx,cy,r):
        self.cx = cx
        self.cy = cy
        self.r = r 
        self.width = 10
        self.test = 0

    def drawColourWheel(self,canvas):
        canvas.create_oval(self.cx-(self.r+10),self.cy-(self.r+10),
                           self.cx+(self.r+10),self.cy+(self.r+10),
                           fill='grey60',width=self.width, outline='grey26')

        for i in range(len(col.coloursList)):
            canvas.create_arc(self.cx-(self.r+self.width/2), self.cy-(self.r+self.width/2), 
                              self.cx+self.r+self.width/2, self.cy+self.r+self.width/2, 
                              fill=col.coloursList[i],outline = '', 
                              style="pieslice",start=i,extent=360-i)

    def getColour(self,x,y):
        x1,y1 = self.cx,self.cy
        x2,y2 = self.cx+self.r,self.cy
        x3,y3 = x, y
        index = roundHalfUp(cosineLaw(x1,y1,x2,y2,x3,y3))
        return col.coloursList[index]

    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r-2*self.width)

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
    def getColour(self):
        return self.colour

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

#################################################
# Tree Class
#################################################

class Tree:
    def __init__(self,colour):
        self.leafColour = colour
 
    def drawBranch(self,canvas,depth,x0,y0,h,angle,step=0):
        if depth == 0:
            x1 = x0+ math.cos(math.radians(angle)) * h
            y1 = y0 -  math.sin(math.radians(angle)) * h
            dr.drawBranch(canvas,x0,y0,x1,y1,h,step,self.leafColour)
        else:
            # center Branch
            self.drawBranch(canvas,depth-1,x0,y0,h,angle,step+0.5)

            newx = x0 + math.cos(math.radians(angle)) * h
            newy = y0 - math.sin(math.radians(angle)) * h
            # right Branch
            self.drawBranch(canvas,depth-1,newx,newy,h*0.7,angle-30,step+1)
            # left Branch
            self.drawBranch(canvas,depth-1,newx,newy,h*0.7,angle+30,step+1)
