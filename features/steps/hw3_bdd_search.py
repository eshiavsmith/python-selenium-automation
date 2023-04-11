from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Orders button')
def click_word(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@when('Email input field is empty')
def email_search(context):
    context.driver.find_element(By.ID, "ap_email")


@then('Verify that text {expected_result} is shown')
def verify_search(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@when('Click on Cart button')
def cart_search(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()


@then('Verify that text is shown')
def empty_search(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text