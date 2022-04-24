from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\My Documents\Rajiv\Python\Selenium Automation\chromedriver.exe")

driver.get("https://anindianbard.blogspot.com/") 

print(driver.title) #Title of the page

#print(driver.current_url) #URL of the page

#print(driver.page_source) #Get page source

driver.get("https://musescore.com/user/1276271/scores/5379706")

time.sleep(5)

print(driver.title) #Title of the page

driver.back()

#print(driver.current_url) #URL of the page

time.sleep(5)

print(driver.title) #Title of the page

driver.forward()

time.sleep(5)

print(driver.title) #Title of the page

driver.close() #Close the browser.
