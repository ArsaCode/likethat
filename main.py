# Chrome Bot with Selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LikerBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(os.environ.get("WDPATH"))

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com")
        time.sleep(5)

ars = LikerBot(username=os.environ.get("USERNAME"), password=os.environ.get("PASSWORD"))
ars.login()