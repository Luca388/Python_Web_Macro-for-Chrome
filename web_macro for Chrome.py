from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('/Users/yu/Desktop/Coding/Python_Web_Macro for Chrome')

url ='https://www.google.com/'

driver.get(url)


element = driver.find_element(By.CLASS_NAME, 'gLFyf')
time.sleep(10)
driver.quit()


#