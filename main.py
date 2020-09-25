# Chrome Bot with Selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

WDPATH = os.environ.get("WDPATH")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


class LikerBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(WDPATH)

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com")
        time.sleep(5)
        emailfield = bot.find_element(By.NAME, "session[username_or_email]")
        time.sleep(3)
        passwordfield = bot.find_element(By.NAME, "session[password]")
        time.sleep(3)
        emailfield.send_keys(self.username)
        passwordfield.send_keys(self.password)
        passwordfield.send_keys(Keys.RETURN)
        time.sleep(5)
        hashtag = "%23webdevelopment"
        bot.get(f"https://twitter.com/search?q={hashtag}")

ars = LikerBot(USERNAME, PASSWORD)
ars.login()
