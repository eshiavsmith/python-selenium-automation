from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('http://www.amazon.com/')


#@when('Input text coffee')
@when('Input text {search_word}')
def input_search_word(context, search_word):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
@when('Click on search button')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

#@then('Verify that text "coffee" is shown')
@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
        # Verfication that the steps were completed with an expected result
        #expected_result = '"coffee"'
        # This is the text you see on the screen.  Find the element in the path using XPath.
        # pull the results in text from the page by adding ".text"
        actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

        # Verify the expected result with the actual
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

