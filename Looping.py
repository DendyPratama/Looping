from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

x = 0
for x in range(2):
    driver.get("https://www.instagram.com/")
    driver.find_element(by=By.NAME, value="username").send_keys('dendypratama915@gmail.com')
    driver.find_element(by=By.NAME, value="password").send_keys('endy123455#')
    driver.find_element(by=By.XPATH, value="//div[text()='Log in']").click() 

    try:
        driver.find_element(By.XPATH, value="//div[text()='resend it']")
        x = x + 1
        print("\33[92m",x,"PASSED")
        
    except:
        driver.find_element(By.XPATH, value="//p[text()='Sorry, your password was incorrect. Please double-check your password.']")
        x = x + 1
        print("\33[31m",x,"FAILED")
    
driver.refresh()
print("\33[37m","COMPLETED")