Feature: Reset Test Data on Homepage

  @smoke
  Scenario: User clicks on "Reset Test Data" button and sees a confirmation message
    Given Open browsers himanu789@gmail.com and Qwerty#123
    When  Click "Reset Test Data" button
    Then I should see a confirmation message that the test data has been reset

