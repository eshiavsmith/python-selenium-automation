from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# connect to the Browser
service = Service('/Users/eshiavsmith/Desktop/Automation/python-selenium-automation/chromedriver')

# init (opens) driver
driver = webdriver.Chrome(service=service)

# Maximizes the window when open
driver.maximize_window()

# Selenium command to open the url
driver.get('https://www.amazon.com/')

# Find amazon logo (tag.class)
driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')

# Find Create account name (tag.class)
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Find You name (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

# Find Email (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

# Find Password field (tag[attribute=value])
driver.find_element(By.CSS_SELECTOR, "input[class*='auth-require-password-validation']")

# Find Password text (tag[attribute=value])
driver.find_element(By.CSS_SELECTOR, "div[class*='a-box a-alert-inline a-alert-inline-inf']")

# Find Re-enter Password (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

# Finds continue button (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#continue')

# Finds contiue of use (tag[attribute=value])
driver.find_element, (By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# Finds Privacy Notice (tag[attribute=value])
driver.find_element, (By.CSS_SELECTOR, "a[href*='ap_desktop_footer_privacy_notice']")

# Finds Privacy Notice (tag.class)
driver.find_element, (By.CSS_SELECTOR, 'a.a-link-emphasis')
