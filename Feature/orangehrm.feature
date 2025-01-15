Feature: OrangeHRM Login
  Background: 
    Given Launch browser
    When Open OrangeURL
    And Enter valid Username Password
    And Click Login
    
  Scenario:
    Then User must login to the Dashboard

  Scenario:
    When Navigate to Admin
    Then Admin Page Should display

  