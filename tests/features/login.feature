Feature: Form Authentication
  As a user, I want to log in and out of the secure area

  @demo
  Scenario: Successful login and logout
    Given I open the "Form Authentication" page
    When I log in with valid credentials
    Then the success message is displayed
    When I log out
    Then the 'Form Authentication' page is open
