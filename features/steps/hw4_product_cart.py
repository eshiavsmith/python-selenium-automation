from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ITEMS = (By.ID, 'nav-active-cart li')
ADD_PRODUCT_CART = (By.ID, 'add-to-cart-button')

@when('Click on Add to cart button')
def add_to_cart(content):
    content.driver.find_element(*ADD_PRODUCT_CART).click()
    sleep(1)

@then('Verify cart has {expected_number} item(s)')
def verify_cart_items(content, expected_number):
    cart_item = content.driver.find_element(*CART_ITEMS).test
    assert expected_number == cart_item, f'Expected (expected_number), but got (cart_item)'