# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 23:57:52 2022

@author: Nick
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='chromedriver.exe')

# username = input("please enter your soundcloud username: ")
# password = input("please enter your soundcloude password: ")

driver.get("https://soundcloud.com/discover")

time.sleep(4)

sign_in_button = driver.find_element(By.XPATH, '//*[@id="app"]/header/div/div[3]/div[1]/button[1]').click()
time.sleep(2)
username_input = driver.find_element(By.class, "sc-input sc-input-large focus-receiver")


# print(username, password)

# driver.quit()

# Todo
# connect to chrome driver 
# find html element pointing to song  url
# copy 
# go to downloader web page
# paste 
# automate