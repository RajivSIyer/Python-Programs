from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome(executable_path="D:\My Documents\Rajiv\Python\Selenium Automation\chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.makemytrip.com/")

driver.find_element(By.ID, "fromCity").send_keys("Mumbai")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']").click()
time.sleep(2)
driver.find_element(By.ID, "toCity").send_keys("Bangalore")
time.sleep(2)
driver.find_element(By.ID, "react-autowhatever-1-section-0-item-0").click()