Feature: Login functionality
  
  @Regression
  Scenario Outline: User attempts to log in with different credentials
    Given Open browsers
    When Providing <username> and <password> credentials
    Then Result <result>

    Examples:
      | username        | password        | result            |
      | himanu789@gmail.com  | Q123   | Dashboard   |
      | hia789@gmail.com | invalidPassword | error message|



