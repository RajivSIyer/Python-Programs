from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\My Documents\Rajiv\Python\Selenium Automation\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/index.php") 

#The below commands won't be executed until the page is loaded completely in the span of time mentioned below.
driver.implicitly_wait(10) #seconds

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")

driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()
