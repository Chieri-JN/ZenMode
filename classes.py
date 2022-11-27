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

#################################################
# Helper functions
#################################################


#################################################
# Word Class
#################################################

class Word(object):
    def __init__(self, word):#,wordDict
        self.word = word # this is the dict key 
        self.wordDict = dict.dictonaryMood[self.word] # this is the tuple
    
    def __str__(self):
        return f'{self.word}'
        
    def __repr__(self):
        return f'{self.word}'

    def getWord(self):
        return self.word

    def getWordDict(self):
        return dict.dictonaryMood[self.word]

    def getSynonymes(self):
        return self.getWordDict()[0]

    def getAntonymes(self):
        return self.getWordDict()[1]
    
    def drawWord(self, canvas, x, y, font, colour):
        canvas.create_text(x,y, text=f'{self.word}', font=font, fill=colour)

class Synonyme(Word): 
    def __init__(self,type):
        super.__init__(self.word)
    # will have the list here either index into tuple or something else.
    pass

class Antonyme(Word):
    pass

#################################################
# Button Class
#################################################

class Button: 
    def __init__(self, x, y, h, w, colour):
        self.x0 = x
        self.y0 = y
        self.width = h
        self.height = w
        self.x1 = self.x0 + self.width
        self.y1 = self.y0  + self.height
        self.colour = colour

    # takes in function 
    def mousePressed(self, function):
        return function

    def draw(self, canvas):
        canvas.create_rectagle(self.x0,self.y0, self.x1, self.y1, fill=self.colour)
    
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


"""THE FOLLOWING CODE IS TEST CODE AND WILL BE REMOVED IN FINAL PRODUCT"""

def appStarted(app):   
    app.buttons = []
    app.words = []
    for key in dict.dictonaryMood:
        testword = Word(key)#,dict.dictonaryMood[key]
        app.words.append(testword)
    
for key in dict.dictonaryMood:
    testword = Word(key)#,dict.dictonaryMood[key]
    print(testword)
    print(testword.getWord())
    # print(testword.getWordDict())
    print(testword.getAntonymes())
    print('')


def redrawAll(app, canvas):
    # testword.drawWord(canvas,100,50,'Krungthep 26','red')
    for i in range(len(app.words)):
        # note this goes in revers
        app.words[i].drawWord(canvas,100,50 + 30*i,'Krungthep 26','red')


runApp(width=400, height=200)
    