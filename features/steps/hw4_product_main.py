from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLER_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
BESTSELLER_SEARCH = (By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers')]")


# @given('Open Amazon page')
# def open_amazon(context):
#      context.driver.get('https://www.amazon.com')


@when('Input text {prod_search_field} into search field')
def enter_product_name(context, prod_search_field):
    context.driver.find_element(*BESTSELLER_SEARCH_FIELD).send_keys(prod_search_field)


@when('Click on Search Amazon button')
def click_button(context):
    context.driver.find_element(*BESTSELLER_SEARCH).click()


# @when('Click on the first product under Results')
# def product_selections(context):
#     context.driver.find_element(*PRODUCT_SELECTION).click()
#     sleep(1)


# @then('Verify page has {expected_number} links')
# def verify_bestseller_links(context, expected_number):
#     expected_number = int(expected_number)
#     bestseller_links = context.driver.find_elements(*BESTSELLER_LINKS)
#     assert len(bestseller_links) == expected_number, f'Expected {expected_number} links but got {len(bestseller_links)}'
