import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\tools\\chromedriver_win32\\112.0.5615.49\\chromedriver.exe"))
driver.get("https://www.google.com")
print(driver.current_url)
print(driver.title)
# print(driver.page_source)

driver.find_element(By.CLASS_NAME, value="gLFyf").send_keys('is selenium good for tests')
driver.find_element(By.NAME, value="btnK").submit()
time.sleep(5)

driver.quit()
