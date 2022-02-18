import time
import xlrd

from locators.patient_creation_page_locators import PatientCreationPageLocators
from config.set_up import Setup
from behave import given, when, then
from selenium.webdriver.common.by import By


# getting test data from the excel file "testdata.xls"
workbook = xlrd.open_workbook('testdata.xls')
sheet = workbook.sheet_by_name('patientinfo')


rowCount = sheet.nrows
colCount = sheet.ncols

for current_row in range(1, rowCount):
    first_name = sheet.cell_value(current_row, 0)
    middle_name = sheet.cell_value(current_row, 1)
    last_name = sheet.cell_value(current_row, 2)
    phone_number = sheet.cell_value(current_row, 3)
    date_of_birth = sheet.cell_value(current_row, 4)
    address = sheet.cell_value(current_row, 5)
    full_name = first_name + " " + middle_name + " " + last_name


@given('I open the a browser and navigate to the URL')
def navigate_to_url(context):
    context.driver = Setup.get_driver()
    context.driver.get("http://localhost:3000/")
    context.driver.maximize_window()
    time.sleep(5)


@when("I type the patient's first name")
def type_patient_first_name(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.first_name_xpath).send_keys(first_name)
    time.sleep(5)


@then("I type the patient's middle name")
def type_patient_middle_name(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.middle_name_xpath).send_keys(middle_name)
    time.sleep(5)


@then("I type the patient's last name")
def type_patient_last_name(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.last_name_xpath).send_keys(last_name)
    time.sleep(5)


@then("I type the patient's phone number")
def type_patient_phone_number(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.phone_number_xpath).send_keys(phone_number)
    time.sleep(5)


@then("I type the patient's date of birth")
def type_patient_date_of_birth(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.date_of_birth_xpath).send_keys(date_of_birth)
    time.sleep(5)


@then("I type the patient's address")
def type_patient_address(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.address_xpath).send_keys(address)
    time.sleep(5)


@when("I click on the add new user button")
def click_add_new_user_button(context):
    context.driver.find_element(By.XPATH, PatientCreationPageLocators.add_new_user_button_xpath).click()
    time.sleep(5)


@then("I should see the added patient's full name")
def check_patient_full_name(context):
    text_to_check = context.driver.find_element(By.XPATH, PatientCreationPageLocators.created_user_full_name_xpath).text
    assert full_name == text_to_check


@then("I should see the added patient's address")
def check_patient_address(context):
    text_to_check = context.driver.find_element(By.XPATH, PatientCreationPageLocators.created_user_address).text
    assert address in text_to_check


