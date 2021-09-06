from behave import *
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\Pooja\PycharmProjects\pythonProject\harekrishanabehaveproject\features\driver\chromedriver.exe')

@given('I Launch Chrome browser')
def launch_browser(context):
    context.driver=webdriver.Chrome()

@when('I open Wyscout Homepage')
def whycout_homepage(context):
    driver.get("https://platformrc.wyscout.com/app/")
    driver.implicitly_wait(10)

@when('Enter username and Password')
def user_pass(context):
    context.driver.find_element_by_id("login_username").send_key("poojamulke77@gmail.com")
    context.driver.find_element_by_id("login_password").send_key("pw_IndiaTest!")

@when('Click on Sing In button')
def sing_in(context):
    context.driver.find_element_by_id("login_button").click()

@then('User must successfully login to the Whyscount Homepage')
def succ_login(context):
    text=context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/h1").text
    assert text=="PLATFORM"
    context.driver.close()

