from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    CALL_TAXI_BUTTON = (By.CLASS_NAME, "Call Taxi Button")
    SUPPORTIVE_PLAN = (By.XPATH, "//div[text()='Supportive']")
    PHONE_NUMBER = (By.XPATH, "//div[text()='Phone number']")
    CREDIT_CARD = (By.XPATH, "//div[text()='Credit Card']")
    SWITCH_INPUT = (By.XPATH, "//input[@type='checkbox' and contains(@class, 'switch-input')]")

    def get_blanket_checkbox_state(self):
        return self.driver.find_element(
            *self.SWITCH_INPUT
        ).get_property("checked")

    def add_ice_cream(self):
        for _ in range(2):
            self.driver.find_element(
                *self.ICE_CREAM_BUTTON
            ).click()

    def is_modal_displayed(self):
        return self.driver.find_element(
            *self.SOME_LOCATOR
        ).is_displayed()
