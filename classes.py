#################################################
# classes.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################
 
import cmu_112_graphics 
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
    def __init__(self, word):
        self.word == word # this is the dict key 
        self.wordDict = dict.dicitonaryMood[word] # this is the tuple
    
    def __str__(self):
        return f'A(x={self.word})'
    def __repr__(self):
        return f'A(x={self.word})'
    
    def getWord(self):
        return self.word

    def getWordDict(self):
        return self.wordDicrt

    def getSynonymes(self):
        return self.getWordDict[0]
    
    def getAntonymes(self):
        return self.getWordDict[0]

    def drawWord(self, app, canvas, x, y):
        pass


class Synonyme(Word): 
    def __init__(self,type):
        super.__init__(word)
    # will have the list here either index into tuple or something else.
    pass

class Antonyme(Word):
    pass

#################################################
# Button Class
#################################################

class Button: 
    def __init__(self, x0, y0, x1, y1):
        pass

#################################################
# Tree Class
#################################################


class Tree:
    def __init(self):
        pass



for key in dict.dictonaryMood:
    testword = Word(key)
    print(testword.getWord)