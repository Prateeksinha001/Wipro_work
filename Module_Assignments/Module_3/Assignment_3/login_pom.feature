Feature: Login using Page Object Model
  As a QA engineer
  I want login scenarios driven by external test data
  So that the same steps validate many credential combinations

  Background:
    Given the user is on the login page

  @datadriven @pom
  Scenario Outline: Login attempt with various credentials
    When the user logs in with username "<username>" and password "<password>"
    Then the login result should be "<expected_result>"

    Examples: Login combinations
      | username | password  | expected_result |
      | testuser | Test@1234 | success          |
      | testuser | WrongPass | failure          |
      |          | Test@1234 | failure          |
