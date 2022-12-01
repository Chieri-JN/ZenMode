#################################################
# ZenModemain.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################
 
from cmu_112_graphics import *
import math
import os
import random
import copy
import decimal
import string
import classes as cl



###################################################
# Helper functions
###################################################
import dictionaries as dict

##################################################
# Screens
##################################################
import screens as scr


##################################################
# Main App
##################################################

def appStarted(app):
    app.mode == 'startScreen'
    # app.timerDelay = 100
    app.dictionary = dict.dictonaryMood  
    # keys will be words that lead to set of synonymes
    app.selectedWord = None
    app.treebranches = []
    app.buttons = []

 # NOTE FOR LATER
 # just use hard check of if word is positve or neg in meaning(i.e. word in neg/pos)
 # 

# runApp(width=1200, height=900)
