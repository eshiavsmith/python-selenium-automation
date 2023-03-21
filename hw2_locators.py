from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# init driver
service = Service('/Users/eshiavsmith/Desktop/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

# maximize the window size
driver.maximize_window()

# Locate amazon logo By class
driver.find_element(By.XPATH, "//a[contains(@href, '/ref=ap_frn_logo')]")

# Locate email field By ID
driver.find_element(By.ID, "//input[@id='ap_email']")

# Locate continue button field By ID
driver.find_element(By.ID, "//input[@id='continue']")

# Locate "Need help" link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Locate "Forgot your password" link by first clicking on "Need help" link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

# Locate "Other Issues with Sign-In" link by first clicking on "Need help" link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

# Locate "Create your Amazon account" button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

# Locate "Conditions of Use" link By XPath Contains:
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_desktop_footer_cou?ie')]")

# Locate "Privacy Notice" link By XPath Contains:
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_desktop_footer_privacy_notice?ie')]")

