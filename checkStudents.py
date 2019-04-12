import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/usr/bin/chromium-browser' 

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",   chrome_options=chrome_options)  
driver.get("https://accounts.thinkful.com/login?_next=https://lark.thinkful.com/available-students/")
username_field = driver.find_element_by_id('LoginInput')
username_field.click()
username_field.send_keys(os.environ["USER"])

password_field = driver.find_element_by_id('LoginPassword')
password_field.click()
password_field.send_keys(os.environ["PASS"])

password_field.submit()

element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "react-app"))
    )
element = driver.find_element_by_id('react-app')

if "There are no students available right now" in element.text:
    print("0")
else:
    print("Students found!")

driver.close() # does literally nothing irl
