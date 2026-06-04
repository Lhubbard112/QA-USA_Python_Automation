from selenium.webdriver.common.by import By
import helpers



class UrbanRoutesPage:

    # Locators
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_TAXI_BUTTON = (By.CLASS_NAME, "call-taxi-button")
    SUPPORTIVE_PLAN = (By.XPATH, "//div[text()='Supportive']")
    PHONE_NUMBER_BUTTON = (By.XPATH, "//div[text()='Phone number']")
    CREDIT_CARD_BUTTON = (By.XPATH, "//div[text()='Credit Card']")
    PHONE_INPUT = (By.XPATH, "//input[@type='tel']")
    CARD_INPUT = (By.XPATH, "//input[@name='number']")
    COMMENT_FIELD = (By.ID, "comment")
    SWITCH_INPUT = (
        By.XPATH,
        "//input[@type='checkbox' and contains(@class, 'switch-input')]"
    )
    ICE_CREAM_BUTTON = (By.CLASS_NAME, "ice-cream-button")
    ICE_CREAM_COUNTER = (By.CLASS_NAME, "ice-cream-counter")
    ORDER_MODAL = (By.CLASS_NAME, "order-modal")

    def __init__(self, driver):
        self.SEND_CODE_AGAIN_BUTTON = None
        self.PHONE_CODE_INPUT = None
        self.NEXT_BUTTON = None
        self.CONFIRM_BUTTON = None
        self.driver = driver

    def set_from(self, value):
        self.driver.find_element(*self.FROM_FIELD).send_keys(value)

    def set_to(self, value):
        self.driver.find_element(*self.TO_FIELD).send_keys(value)

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def click_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN).click()

    def set_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

        self.driver.find_element(*self.NEXT_BUTTON).click()

        code = helpers.retrieve_phone_code(driver=self.driver)

        self.driver.find_element(*self.PHONE_CODE_INPUT).send_keys(code)

        self.driver.find_element(*self.SEND_CODE_AGAIN_BUTTON).click()

        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def set_credit_card(self, card):
        self.driver.find_element(*self.CREDIT_CARD_BUTTON).click()

        self.driver.find_element(*self.CARD_INPUT).send_keys(card)

    def set_comment_for_driver(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD).click()

        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.SWITCH_INPUT).click()

    def add_ice_cream(self):
        for _ in range(2):
            self.driver.find_element(*self.ICE_CREAM_BUTTON).click()

    def get_from_field_value(self):
         self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def get_to_field_value(self):
         self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def get_comment_for_driver(self):
         self.driver.find_element(*self.COMMENT_FIELD).get_attribute("value")

    def get_ice_cream_count(self):
         self.driver.find_element(*self.ICE_CREAM_COUNTER).get_attribute("value")

    def is_call_taxi_selected(self):
         self.driver.find_element(*self.CALL_TAXI_BUTTON).is_displayed()

    def is_supportive_plan_selected(self):
         self.driver.find_element(*self.SUPPORTIVE_PLAN).is_displayed()

    def is_phone_number_selected(self):
         self.driver.find_element(*self.PHONE_INPUT).is_displayed()

    def is_credit_card_selected(self):
         self.driver.find_element(*self.CARD_INPUT).is_displayed()

    def is_blanket_and_handkerchiefs_selected(self):
         self.driver.find_element(*self.SWITCH_INPUT).get_property("checked")

    def is_modal_displayed(self):
         self.driver.find_element(*self.ORDER_MODAL).is_displayed()