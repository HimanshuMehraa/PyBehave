Feature: Backgroud tut
 Background: 
   Given Open browser

 Scenario: VERIFYING TITLE
   When provide 'username' and 'password'
   Then verify title

Scenario: Outline
   When provide valid 'username' and 'password'
   Then verify success message
