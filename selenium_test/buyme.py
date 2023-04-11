import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains


# from selenium.webdriver.support.relative_locator import locate_with
#
# # test for finding and printing attributes
# def print_input_elements(_driver):
#     elements = _driver.find_elements(locate_with(By.TAG_NAME, "input"))
#     for e in elements:
#         att = e.get_attribute("placeholder")
#         print(f"attribute: {att} , prop: {prop}")


driver = webdriver.Chrome(service=Service("C:\\tools\\chromedriver_win32\\112.0.5615.49\\chromedriver.exe"))
wait = WebDriverWait(driver, 3)
# action = ActionChains(driver)

driver.get("https://buyme.co.il")
print(driver.current_url)
print(driver.title)

# click on button
driver.find_element(By.LINK_TEXT, value="כניסה / הרשמה").click()

# wait for the click to take effect and open a new element
# the new element is the registration form
try:
    # using the 'CSS_SELECTOR' we can wait for a html element of
    # type 'form' that has an attribute 'entry'
    search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form.entry")))

    # # a different option to wait for the 'input' element for the email
    # search = wait.until(EC.text_to_be_present_in_element((By.XPATH, '//input[@type="email"]')))
    # action.move_to_element(search).send_keys("")
    print('entry form found')

    # once we managed to find the new 'form'
    # find the email element
    # the search is done using XPATH that looks for:
    #   any element of type 'input'
    #   that has the attribute 'type' and it's value is equal to 'email'
    el_email = driver.find_element(By.XPATH, value='//input[@type="email"]')
    # add text inside the input element
    el_email.send_keys("test@test.co.il")
except:
    print("entry form found")


time.sleep(5)

driver.quit()
