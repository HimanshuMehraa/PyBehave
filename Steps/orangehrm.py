from behave import *
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('Launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Or use Firefox(), etc.
    

@when('Open OrangeURL')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(10)

@when('Enter valid Username Password')
def step_impl(context):
    username = context.driver.find_element(By.XPATH, "//input[@name='username']")
    password = context.driver.find_element(By.XPATH, "//input[@name='password']")
    username.send_keys('admin')
    password.send_keys('admin123')
    time.sleep(5)

@when('Click Login')
def step_impl(context):
    login= context.driver.find_element(By.XPATH, '//button[text()= " Login "]')
    login.click()
    time.sleep(10)

@then('User must login to the Dashboard')
def step_impl(context):
    try:
        text= context.driver.find_element(By.XPATH,'//h6[text()="Dashboard"]').text
    except:
        context.driver.close()
        assert False,"DASHBOARD test failed!!!!"
    if text=='Dashboard':
        context.driver.close()
        assert True, "DASHBOARD test PASSED!!!!"

@when('Navigate to Admin')
def step_impl(context):
    admin_ele = context.driver.find_element(By.XPATH,"//span[text()='Admin']")
    admin_ele.click()


@then('Admin Page Should display')
def step_impl(context):
    time.sleep(10)
    try:
      ele= context.driver.find_element(By.XPATH,"//h6[text()='User Management']").text

    except:
      context.driver.close()
      assert False, "Admin Page Test Case Failed!!!"
    if ele=='Userr Management':
        context.driver.close()
        assert True, "Admin test PASSED!!!!"
    