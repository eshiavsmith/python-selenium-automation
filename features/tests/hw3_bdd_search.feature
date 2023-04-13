# Created by eshiavsmith at 4/6/23
Feature: Amazon Sign-in Search
  # Enter feature description here

  Scenario: User can see Sign-in on the page
   Given Open Amazon page
    When Click on Orders button
    When Verify Email input field is present
    Then Verify that text "Sign in" is shown

 Scenario: Amazon cart is empty
   Given Open Amazon page
    When Click on Cart button
    Then Verify that text "Your Amazon Cart is empty" is shown