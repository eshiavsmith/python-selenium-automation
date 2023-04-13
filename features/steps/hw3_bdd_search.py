from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')


@when('Click on Orders button')
def click_word(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
    sleep(1)


@when('Verify Email input field is present')
def email_search(context):
    context.driver.find_element(By.ID, "ap_email")


@then('Verify that text {expected_search} is shown')
def verify_search_result(context, expected_search):
    search_results = context.driver.find_element(By.XPATH, "//h1[text()='Sign in']")
    assert expected_search == search_results, f'Expected {expected_search} but got actual {search_results}'



@when('Click on Cart button')
def cart_search(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()
    sleep(1)


# @then('Verify that text {expected_search} is shown')
def verify_cart_search(context, expected_search):
    cart_result = context.driver.find_element(By.XPATH, "//h2[text()='Your Amazon Cart is empty']")
    assert expected_search == cart_result, f'Expected {expected_search} but got actual {cart_result}'