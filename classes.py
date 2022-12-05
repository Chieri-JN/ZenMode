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
    return newx,newy

def distance(x1, y1, x2, y2): 
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return math.sqrt(x + y) 
    
#################################################
# Player Class
#################################################
# TODO INCORPERATE BOUNDS

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
        # self.sprS = spriteState # dictates what the player is doing
        # self.sprC = spriteCount

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
            sprite = self.mRSprites[spriteCount]
            canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(sprite))
        elif spriteState == 'left':
            sprite = self.mLSprites[spriteCount]
            canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(sprite))


    def movePlayer(self,dx,dy):
        self.px += dx
        self.py += dy
    
    # NOTE FIX
    def inPlayerBounds(self,x,y):
        return ((self.px - self.pWr <= x <= self.px + self.pWr) and
                (self.py - self.pHr <= x <= self.py + self.pHr))

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

    def inBounds(self,x,y):
        #NOTE Taken from dot class example
        return (((self.cx - x)**2 + (self.cy - y)**2)**0.5 <= self.r)

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
# Pieslice Class
#################################################

# possibly change to line class and use trig (sin,cos and iterated degrees/radians )
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

#################################################
# Tree Class
#################################################

class Tree:
    def __init__(self,depth,startx,starty):
        self.branches = []
        self.depth = depth
        self.startx = startx
        self.starty = starty
        self.anlgeShift = math.pi/5
    
    def drawBranch(self,canvas,depth,x0,y0,x1,y1,step=0,check=0):
        if depth == step:
            dr.drawBranch(canvas,x0,y0,x1,y1,step,check)
        else:
            #main branch
            self.drawBranch(canvas,depth,x0,y0,x1,y1,step+1,check+1)

            #left branch
            xl,yl = branchPoint(x1,y1,(y1-y0)*0.75,'left')
            self.drawBranch(canvas,depth,x1,y1,xl,yl,step+1,check+2)

            # Right branch
            xr,yr = branchPoint(x1,y1,(y1-y0)*0.75,'right')
            self.drawBranch(canvas,depth,x1,y1,xr,yr,step+1,check+2)

    # def drawBranch(self,canvas,depth,ogX,ogY,):
    #     pass
 


"""THE FOLLOWING CODE IS TEST CODE AND WILL BE REMOVED IN FINAL PRODUCT"""

# for key in dict.dictonaryMood:
#     testword = Word(key)
#     print(testword)
#     print(testword.getWord())
#     print(testword.getWordDict())
#     print(testword.getAntonymes())
#     print('')


def mousePressed(app,event):
    pass

def appStarted(app):
    app.px = app.width/2
    app.py = 790
    app.player = Player(app,app.px,app.py)
    # app.timerDelay = 1000
    app.spriteCounter  = 0
    # app.playerSprites = PlayerSprites(app)[3]
    app.spriteState = 'idle'
    app.timerDelay = 300

    app.jumpState = False
    app.jumpCounter = 0
    
# def redrawAll(app, canvas):
#     drawPlayer(app,canvas)
#     tree = Tree(4,app.width/2,750)
#     tree.drawBranch(canvas,5,app.width/2,790,app.width/2,700)

#     for i in range(len(app.words)):
#         # note this goes in revers
#         app.words[i].drawWord(canvas,100,50 + 30*i,'Krungthep 26','red')

def drawPlayer(app,canvas):
    app.player.drawPlayer(canvas,app.spriteState,app.spriteCounter)
    

def keyPressed(app,event):
    if event.key == 'Right':
        app.spriteState = 'right'
        app.spriteCounter = (1 + app.spriteCounter) % 7 # change later
        app.player.movePlayer(10,0)
        # app.px += 5 
    elif event.key == 'Left':
        app.spriteState = 'left'
        app.spriteCounter = (1 + app.spriteCounter) % 7 # change later
        app.player.movePlayer(-10,0)
        # app.px -= 10
    elif event.key == 'Space':
        app.spriteState == 'jump'
        app.jumpState = True
    elif not event.key:
        timerFired(app)

def keyReleased(app,event):
    if event.key == 'Space':
        app.jumpState = True
        app.spriteState == 'jump'
    elif event.key == 'Right':
        # create r idle
        app.spriteState = 'idle'
    elif event.key == 'Left':
        app.spriteState = 'idleL'

def timerFired(app):
            if not app.jumpState:
                if app.spriteState == 'idle':
                    app.spriteCounter = (1 + app.spriteCounter) % 2
                elif app.spriteState == 'idleL':
                     app.spriteCounter = (1 + app.spriteCounter) % 2
            elif app.jumpState:
                app.spriteCounter = (1 + app.spriteCounter) % 11
                app.jumpCounter += 1
                if app.jumpCounter == 10:
                    app.jumpState = False
                    app.jumpCounter = 0
                    app.spriteState == 'idle'

            # if app.spriteState == 'jump':
            #     app.timerDelay = 1000
            #     app.spriteCounter = 0
            #     while app.spriteCounter < 12:
            #         app.spriteCounter +=1
            #     app.spriteState = 'idle'
            #     app.timerDelay = 200

# runApp(width=800, height=800)
    