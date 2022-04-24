from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\My Documents\Rajiv\Python\Selenium Automation\chromedriver.exe")

driver.get("https://www.netflix.com/in/login")

usr_ele = driver.find_element_by_name("userLoginId")

print(usr_ele.is_displayed()) #returns true/false based of element status

print(usr_ele.is_enabled()) #return true/false

usr_ele.send_keys("sureshrk@gmail.com")

pwd_ele = driver.find_element_by_id("id_password")

print(pwd_ele.is_displayed()) #returns true/false based of element status

print(pwd_ele.is_enabled()) #return true/false

pwd_ele.send_keys("IQKiller")

driver.find_element_by_tag_name("button").click()