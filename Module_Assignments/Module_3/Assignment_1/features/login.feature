Feature: User login
  As a registered user
  I want to log into the application
  So that I can access my dashboard

  Background:
    Given the user is on the login page

  @smoke
  Scenario: Successful login with valid credentials
    When the user enters username "testuser" and password "Test@1234"
    And the user clicks the login button
    Then the user should see the dashboard page

  Scenario: Login fails with invalid password
    When the user enters username "testuser" and password "WrongPass"
    And the user clicks the login button
    Then the user should see an error message "Invalid username or password"
