@scenario2
Feature: Personal World Clock

  Scenario: Add Minsk to the personal world clock
    Given I navigate to the page "https://www.timeanddate.com/worldclock/personal.html"
    Then I press the link with name "Add City"
    And I verify the modal with title "Search for a city" is opened
    When I enter "Minsk" into the input with id "addtxt"
    And I wait 5 seconds until the suggestion list is shown
    But I click suggestion number 1 in dropdown
    Given I press the modal button with text "Save"
    And word "Minsk" is displayed
