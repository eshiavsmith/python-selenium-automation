# Created by eshiavsmith at 4/1/23
Feature: Amazon Search test
  # Enter feature description here

  Scenario: User can search for a product on Amazon
   Given Open Amazon page
    When Input text coffee
    When Click on search button
    Then verify that text "coffee" is shown

  Scenario: User can search for a product on Amazon
   Given Open Amazon page
    When Input text table
    When Click on search button
    Then verify that text "table" is shown

    Scenario: User can add a product to the cart