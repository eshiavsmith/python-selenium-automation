# Created by eshiavsmith at 4/11/23
Feature: Amazon product cart
  # Verify at least 5 links

  Scenario: User can add products to the cart
   Given Open Amazon page
    When Input text Zulu Water Bottles into search field
    When Click on Search Amazon button
    And Click on the first product under Results
    And Click on Add to cart button
    Then Verify cart has 3 item(s)
