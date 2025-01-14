Feature: Login functionality
 
 Scenario: Valid Username and Password
   Given Open browser
   When Providing valid himanu789@gmail.com and Qwerty#123 credentials
   Then Verifying Dashboard

 Scenario Outline:
   Given Open browser
   When Providing valid <username> and <password> credentials
   Then Verifying Dashboard
   Examples:
     | username | password |
    | himanu789@gmail.com | Qwerty#223 |
    | himanu789@gmail.com | Qwerty#113 |
    | himanu789@gmail.com | Qwerty#123 |