from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/eshiavsmth/python-selenium-automation/chromedriver')

# Connect to the browser - opens the chrome webbrowser
service = Service('/Users/eshiavsmith/Desktop/Automation/python-selenium-automation/chromedriver')

# This opens the browser
driver = webdriver.Chrome(service=service)


# this Selenium commmand that opens the url
driver.get('https://www.amazon.com/')

sleep(5)
# explain what element you would like to use
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID, 'nav-search-submit-button').click()

# Verfication that the steps were completed with an expected result
expected_result = '"table"'
# This is the text you see on the screen.  Find the element in the path using XPath.
# pull the results in text from the page by adding ".text"
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(actual_result)
# Verify the expected result with the actual
assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')

driver.quit()
