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
import dictionary as dict

#################################################
# Helper functions
#################################################


#################################################
# Word Class
#################################################

class Word:
    # 
    def __init__(self,word):
        self.getWord == word # this is the dict key 
        self.getWordDict = dict.dicitonaryMood[word] # this is the tuple
    pass


class Synonyme(Word):
    pass # will have the list here either index into tuple or something else.

class Antonyme(Word):
    pass


#################################################
# Button Class
#################################################