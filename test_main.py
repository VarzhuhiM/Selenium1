import pytest
from selenium.webdriver.common.by import By
import time
import allure

# Constants
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
ACCOUNT_URL = "https://magento.softwaretestingboard.com/customer/account/"
EMAIL = "varzhuhi@gmail.com"
PASSWORD = "varzhuhi1!#"
NEW_PASSWORD = "varzhuhi1!#"


@allure.feature('Authentication')
@allure.suite('Login Tests')
@allure.title('Invalid Login Test with Incorrect Credentials')
@allure.description('This test verifies that logging in with an invalid email and password results in an error message.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.smoke
def test_invalid_login(driver):
    with allure.step('Navigate to the login page'):
        driver.get(LOGIN_URL)

    with allure.step('Enter invalid email'):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("invalidemail@gmail.com")

    with allure.step('Enter invalid password'):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys("invalidpassword")

    with allure.step('Click the login button'):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    with allure.step('Verify the error message for invalid login'):
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "Please wait and try again later" in error_message.text


@allure.feature('Authentication')
@allure.suite('Login Tests')
@allure.title('Valid Login Test with Correct Credentials')
@allure.description('This test verifies that a user can log in successfully with valid email and password, and is redirected to the account page.')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.regression
@pytest.mark.smoke
def test_login(driver):
    with allure.step('Navigate to the login page'):
        driver.get(LOGIN_URL)

    with allure.step('Enter valid email'):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(EMAIL)

    with allure.step('Enter valid password'):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys(PASSWORD)

    with allure.step('Click the login button'):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    with allure.step('Verify successful login by checking the account page URL'):
        time.sleep(3)
        assert driver.current_url == ACCOUNT_URL


@allure.feature('Account Management')
@allure.suite('Password Change Tests')
@allure.title('Test Change Password with Incorrect Current Password')
@allure.description('This test verifies that attempting to change the password with an incorrect current password results in an error message.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.smoke
def test_change_password_incorrect_current(driver):

    with allure.step('Navigate to the account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Navigate to the change password page'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter incorrect current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys("incorrectpassword")

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Confirm new password'):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Click Save button to attempt password change'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify error message for incorrect current password'):
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "The password doesn't match this account." in error_message.text


@allure.feature('Account Management')
@allure.suite('Password Change Tests')
@allure.title('Test Change Password with Mismatched Confirmation Password')
@allure.description('This test verifies that when the confirmation password does not match the new password, an appropriate error message is shown.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.smoke
def test_change_password_mismatch(driver):

    with allure.step('Navigate to the account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Navigate to the change password page'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter the correct current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step('Enter the new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Enter a mismatched confirmation password'):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("mismatchedpassword")

    with allure.step('Click the Save button to attempt the password change'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify error message for mismatched password confirmation'):
        error_message = driver.find_element(By.ID, "password-confirmation-error")
        assert "Please enter the same value again." in error_message.text


@allure.feature('Account Management')
@allure.suite('Password Change Tests')
@allure.title('Test Change Password with Valid Inputs')
@allure.description('This test verifies that a user can successfully change their password using valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.smoke
def test_change_password(driver):
    with allure.step('Navigate to the account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Navigate to the change password page'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Confirm new password'):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Click Save button to apply the new password'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify success message after password change'):
        success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-success')]")

        assert "You saved the account information." in success_message.text


