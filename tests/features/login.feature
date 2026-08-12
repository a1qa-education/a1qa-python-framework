Feature: Form Authentication
  As a user, I want to log in and out of the secure area

  @demo
  Scenario: Successful login and logout
    Given the main page is open
    When I navigate to the "Form Authentication" page
      And I log in with valid credentials
    Then the success message is displayed
    When I log out
    Then the 'Form Authentication' page is open
