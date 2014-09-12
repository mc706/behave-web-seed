Feature: Test Out the web library

  Scenario Outline: Test Out Some Google Searches

    Given I am on the page with url "http://www.google.com"
    When I put "<search>" in the field with name "q"
    When I click the button with name "btnG"
    Then I should be on the page with url "<result_url>"
    And I should see the text "<result_text>"

    Examples: Amphibians
      | search        | result_url                                 | result_text  |
      | google        | https://www.google.com/#safe=off&q=google  | google       |