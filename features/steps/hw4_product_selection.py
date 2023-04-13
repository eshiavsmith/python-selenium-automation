from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_SELECTION = (By.XPATH, "//div[@data-component-type='s-search-result']//a[//span[@class='a-price']]")


@when('Click on the first product under Results')
def product_selections(context):
    context.driver.find_element(*PRODUCT_SELECTION).click()
    sleep(1)


@then('Verify cart has {expected_item} items')
def verify_product_cart(context, expected_item):
    actual_item = context.driver.find_elements(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_item == actual_item, f'Expected {expected_item} but got {actual_item}'
