# Chrome Bot with Selenium
from selenium import webdriver

PATH = "/opt/WebDriver/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://twitter.com")

driver.find_element(By.LINK_TEXT, "Log in").click()