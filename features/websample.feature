Feature: Test Out the web library

  Scenario Outline: Test Out Some Google Searches

    Given I am on the page with url "http://www.google.com"
    When I put "<search>" in the field with name "q"
    When I click the button with name "btnG"
    Then I should see the text "<result_text>"

    Examples: Searches
      | search        |  result_text  |
      | google        |  google       |
      | test          |  test         |

  Scenario: Test the this repos page

    Given I am on the page with url "http://github.com/mc706/behave-web-seed"
    When I wait 3 seconds
    Then I should see the following text
      """
      A Seed project for starting a behave testing suite for the web
      """