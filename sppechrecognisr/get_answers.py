# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:43:20 2019

@author: shaag
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
    def __init__(self,url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver,5)
        self.url = url
    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME,"gsfi")
    ))
        except:
            print("yeah it failed")
            
        soup = BeautifulSoup(self.driver.page_source,"html.parser")
        answer = soup.find_all(class_ = "_sPg")
        
        if not answer:
            answer = soup.find_all(class_ = "_m3b")
        if not answer:
            answer  ="couldn't find"
        self.driver.quit()
        return answer[0].get_text()
        