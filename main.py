from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
#
EMAIL = "admind@tamanta.net"
PASS = "Dd@1234567890"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://staging.smartkungahara.rw/")

# Get and set email
email = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[2]/div/div/form/div[1]/input')
time.sleep(3)
email.send_keys(EMAIL)

# Enter password
password = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[2]/div/div/form/div[2]/input')
password.send_keys(PASS)

password.send_keys(Keys.ENTER)
time.sleep(3)


driver.quit()
