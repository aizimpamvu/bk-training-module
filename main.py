from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

#
EMAIL = "admind@tamanta.net"
PASS = "Dd@1234567890"

# Training list
trainings = ["Amahugurwa y\'abahinzi ba Kawa",
             "Amahugurwa y\' abatubuzi b\'imbuto",
             "Amahugurwa agamije kongera umusaruro w \'imboga"]

trainings_description = ["Ubusobanuro 1 ",
                         "Ubusobanuro 2",
                         "Ubusobanuro 3"]
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://staging.smartkungahara.rw/#/login")


# Get and set email

email = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[2]/div/div/form/div[1]/input')

email.send_keys(EMAIL)
time.sleep(3)
# Enter password
password = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[2]/div/div/form/div[2]/input')
password.send_keys(PASS)
time.sleep(3)
password.send_keys(Keys.ENTER)
time.sleep(5)
# Training module menu
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/app-asidenavbar/aside/section/ul/li[7]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,
                    '/html/body/app-root/app-admin/div/app-asidenavbar/aside/section/ul/li[7]/ul/li/a').click()
time.sleep(2)
# Create training button
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/section/app-training-list/h3/div/div[2]/a').click()
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/section/app-training-create/form/div['
                              '1]/div/div/div/div[1]/div[1]/div/input').send_keys(random.choice(trainings))
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/section/app-training-create/form/div['
                              '1]/div/div/div/div[1]/div[2]/div/input').send_keys(random.choice(trainings_description))
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/section/app-training-create/form/div['
                              '1]/div/div/div/div[2]/div[1]/div/ng-multiselect-dropdown/div/div[1]/span').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/section/app-training-create/form/div['
                              '1]/div/div/div/div[2]/div[1]/div/ng-multiselect-dropdown/div/div[2]/ul[1]/li/input').send_keys(
    "Not Applied")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/section/app-training-create/form/div['
                              '1]/div/div/div/div[2]/div[1]/div/ng-multiselect-dropdown/div/div[2]/ul[2]/li['
                              '1]/div').click()

time.sleep(3)
driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/div/section/app-training-create/form/div[2]/button[2]').click()
time.sleep(3)
driver.maximize_window()

driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/div[3]/div/div[3]/button/span').click()
print(driver.current_url)
time.sleep(2)
