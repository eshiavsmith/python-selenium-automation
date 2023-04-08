# Created by eshiavsmith at 4/6/23
Feature: Amazon Sign-in Search
  # Enter feature description here

  Scenario: User can see Sign-in on the page
   Given Open Amazon page
    When Click on Orders button
    When Email input field is empty
    Then verify that text "Sign in" is shown

