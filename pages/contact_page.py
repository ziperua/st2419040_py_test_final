from selenium.webdriver.common.by import By

class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, name, email, phone, message):
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "phone").send_keys(phone)
        self.driver.find_element(By.ID, "message").send_keys(message)

    def submit(self):
        self.driver.find_element(By.XPATH, "//button[text()='Send Message']").click()

    def get_success(self):
        return self.driver.find_element(By.ID, "formSuccess").text

    def get_name_error(self):
        return self.driver.find_element(By.ID, "nameError").text

    def get_email_error(self):
        return self.driver.find_element(By.ID, "emailError").text

    def get_phone_error(self):
        return self.driver.find_element(By.ID, "phoneError").text
