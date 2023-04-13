Feature: Amazon test Links
  # Verify at least 5 links

  Scenario: User can verify 5 links on the page
   Given Open Amazon page
    When Click on BestSeller button
    Then Verify page has 5 links
