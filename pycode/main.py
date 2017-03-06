'''
Created on Mar 4, 2017

@author: hamzawix
'''

import speech_recognition as sr
import re

def match_result(pattern, order):
    """
    this function will check if our pattern is matched or not
    """
    s = re.match(pattern, order)
    if s:
        return 1
    else:
        return 0

def decide(order):
    """
    This is a function that takes the returned text from the recognizer
    as an argument and decides where the robot should go.
    """
    if order == "stop":
        print("stoping")
        
    elif order == "forward":
        print("going forward")
        
    elif order == "backward":
        print("going backward")
        
    elif order == "left":
        print("turning left")
        
    elif order == "right":
        print("turning right")
        
    else:
        print("I did not understand")


if __name__ == '__main__':
    
    orders = ["forward", "backward", "stop", "left", "right"] 
    
    #Getting audio from microphone
    engine = sr.Recognizer()
    with sr.Microphone() as source:
        print("Command me!")
        audio = engine.listen(source)
    
    #Recognising speech and deciding
    t = engine.recognize_sphinx(audio)
    for i in orders:
        if match_result("fo", i):
            decide(i)
            break
    
