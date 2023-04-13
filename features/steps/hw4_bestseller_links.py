from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BESTSELLER_SEARCH = (By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers')]")
BESTSELLER_LINKS = (By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li']")


@given('Open Amazon page')
def open_amazon(context):
     context.driver.get('https://www.amazon.com')


@when('Click on BestSeller button')
def click_button(context):
    context.driver.find_element(*BESTSELLER_SEARCH).click()


@then('Verify page has {expected_number} links')
def verify_bestseller_links(context, expected_number):
    expected_number = int(expected_number)
    bestseller_links = context.driver.find_elements(*BESTSELLER_LINKS)
    assert len(bestseller_links) == expected_number, f'Expected {expected_number} links but got {len(bestseller_links)}'
