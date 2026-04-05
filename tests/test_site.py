import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.nav_page import NavPage
from pages.contact_page import ContactPage
from tests.test_data import *

def test_valid_login(driver):
    page = LoginPage(driver)
    page.login(VALID_USERNAME, VALID_PASSWORD)
    
    app = driver.find_element(By.ID, "app")
    assert "hidden" not in app.get_attribute("class")

#    assert driver.find_element(By.ID, "app").is_displayed()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.login(INVALID_USERNAME, INVALID_PASSWORD)

    assert "Invalid credentials" in page.get_error()

def test_navigate_to_cameras(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    nav = NavPage(driver)
    nav.go_to_cameras()

    assert driver.find_element(By.ID, "cameras").is_displayed()

def test_navigate_to_lenses(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    nav = NavPage(driver)
    nav.go_to_lenses()

    assert driver.find_element(By.ID, "lenses").is_displayed()

def test_navigate_to_contact(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    nav = NavPage(driver)
    nav.go_to_contact()

    assert driver.find_element(By.ID, "contact").is_displayed()

def test_contact_form(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    nav = NavPage(driver)
    nav.go_to_contact()

    contact = ContactPage(driver)
    contact.fill_form(VALID_NAME, VALID_EMAIL, VALID_PHONE, VALID_MESSAGE)
    contact.submit()

    assert "Message sent successfully!" in contact.get_success()

def test_logout(driver):
    page = LoginPage(driver)
    page.login(VALID_USERNAME, VALID_PASSWORD)
    page.driver.find_element(By.XPATH, "//button[text()='Logout']").click()

    assert driver.find_element(By.ID, "loginPage").is_displayed()
