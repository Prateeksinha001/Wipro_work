Feature: User API data-driven tests
  As a QA engineer
  I want to validate the Users API against multiple data sets
  So that I can confirm it behaves correctly for each input

  @datadriven
  Scenario Outline: Create a user via API with different payloads
    Given the API endpoint "/users"
    When the user sends a POST request with name "<name>" and job "<job>"
    Then the response status code should be <status_code>
    And the response should contain name "<name>"

    Examples: Valid users
      | name    | job          | status_code |
      | Alice   | Engineer     | 201         |
      | Bob     | QA Analyst   | 201         |
      | Charlie | Product Mgr  | 201         |

  @datadriven @externaldata
  Scenario: Create users from external JSON test data file
    Given the API endpoint "/users"
    When the user creates all users defined in "testdata/users.json"
    Then every response status code should match the expected value
