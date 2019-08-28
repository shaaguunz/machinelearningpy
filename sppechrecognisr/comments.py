# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:01:47 2019

@author: shaag
"""
import pyttsx3
import requests
import os
from bs4 import BeautifulSoup
from get_answers import Fetcher
engine = pyttsx3.init()


class Command:
    def __init__(self):
        self.confirm = ["Yes","affirmative","sure","do it","yeah","confirm"]
        self.cancel = ["No","negaive","negative soldier","nope","cancel"]
    def discover(self, text):
        if"what" in text and "your name" in text:
            if "my" in text:
                self.respond("you haven't told me your name yet")
            else:
                self.respond("My name is python commander.   How are you")
        else:
            f =Fetcher("https://www.google.com/search?q=" +text)
            answer = f.lookup()
            self.respond(answer)
        
            
    def respond(self,response):
        print(response)
        engine.say(response)
        engine.runAndWait()
        