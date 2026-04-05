from selenium.webdriver.common.by import By

class NavPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cameras(self):
        self.driver.find_element(By.XPATH, "//button[text()='Cameras']").click()

    def go_to_lenses(self):
        self.driver.find_element(By.XPATH, "//button[text()='Lenses']").click()

    def go_to_contact(self):
        self.driver.find_element(By.XPATH, "//button[text()='Contact']").click()
