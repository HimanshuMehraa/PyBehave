from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# Create a WebDriver instance that can be used in the steps
@given('Open browsers {username} and {password}')
def step_impl_given_open_browser(context,username,password):
    # Initialize the WebDriver
    context.driver = webdriver.Chrome()  # Or use Firefox(), etc.
    context.driver.get('https://acme-test.uipath.com/login')  # Replace with actual login URL
    username_field = context.driver.find_element(By.ID, 'email')  # Replace 'username' with actual ID
    password_field = context.driver.find_element(By.ID, 'password')  # Replace 'password' with actual ID
    submit_button = context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Login']")  # Replace 'loginButton' with actual ID
    
    # Input valid credentials (replace with your actual credentials)
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

@when('Click "Reset Test Data" button')
def step_impl_then_see_dashboard(context):
     menu_element = context.driver.find_element(By.XPATH, "//button[text()=' User options']")  # Replace with the actual XPath or selector for the menu

        # Find the element to click after hovering
     submenu_element = context.driver.find_element(By.XPATH, "//a[text()='Reset test data']")  # Replace with the actual XPath or selector for the submenu

     actions = ActionChains(context.driver)
     actions.move_to_element(menu_element).perform()
     actions.click(submenu_element).perform()

     test_element = context.driver.find_element(By.XPATH, "//h3[text()='Are you sure you want to Reset your Test Data?']")
     assert test_element.is_displayed() , "Test confirmation is not displayed"

@then('I should see a confirmation message that the test data has been reset')
def step_impl_then_see_dashboard(context):
     
     reset= context.driver.find_element(By.XPATH,"//button[@id='buttonRTD']")
     reset.click()
     time.sleep(15)
     #context.driver.find_element(By.ID, "trigger_alert_button").click()
     alert = context.driver.switch_to.alert
     alert_text= alert.text
     assert alert_text == "Your Test Data has been successfully reset.", f"Expected alert text 'Your Test Data has been successfully reset.', but got '{alert_text}'"
     print("Alert text:", alert.text)
     alert.accept()

    # Close the browser
     context.driver.quit()
