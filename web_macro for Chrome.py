from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('/Users/yu/Desktop/Coding/Python_Web_Macro for Chrome')

url ='https://www.google.com/'

driver.get(url)

element = driver.find_element(By.CLASS_NAME, 'gLFyf') # find javascript class

element.send_keys('test') # enter that want to serch
element.send_keys(Keys.ENTER)
#element.click()

# time sleep and quit
time.sleep(10)
driver.quit()
