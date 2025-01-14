from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance that can be used in the steps
@given('Open browsers')
def step_impl_given_open_browser(context):
    # Initialize the WebDriver
    context.driver = webdriver.Chrome()  # Or use Firefox(), etc.
    context.driver.get('https://acme-test.uipath.com/login')  # Replace with actual login URL

@when('Providing {username} and {password} credentials')
def step_impl_when_provide_credentials(context,username,password):
    
    # Locate elements on the page and fill in the credentials
    username_field = context.driver.find_element(By.ID, 'email')  # Replace 'username' with actual ID
    password_field = context.driver.find_element(By.ID, 'password')  # Replace 'password' with actual ID
    submit_button = context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Login']")  # Replace 'loginButton' with actual ID
    
    # Input valid credentials (replace with your actual credentials)
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Submit the form (click the login button)
    submit_button.click()
    time.sleep(3)

@then('Result {result}')
def step_impl_then_see_dashboard(context,result):
    # Wait for the dashboard to load (you can use WebDriverWait for a more robust solution)
    time.sleep(3)  # Not ideal; WebDriverWait is better, but this is just for simplicity.
    if result == "Dashboard":
        # Check that the dashboard is visible
        dashboard_element = context.driver.find_element(By.XPATH, "//h1[@class='page-header']")
        assert dashboard_element.is_displayed() , "Dashboard is not displayed"
    elif result == "error message":
        # Check that the error message is displayed
        error_message = context.driver.find_element(By.XPATH, "//strong[text()='These credentials do not match our records.']")
        assert error_message.is_displayed(), "Error message is not displayed"

    
    # Close the browser
    context.driver.quit()
