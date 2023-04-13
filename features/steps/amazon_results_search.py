from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


# Verfication that the steps were completed with an expected result
# expected_result = '"coffee"'
# This is the text you see on the screen.  Find the element in the path using XPath.
# pull the results in text from the page by adding ".text"
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # Verify the expected result with the actual
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

