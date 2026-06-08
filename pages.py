from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import helpers


class UrbanRoutesPage:
    # Locators
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_TAXI_BUTTON = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_PLAN = (By.XPATH, "//div[text()='Supportive']")
    PHONE_NUMBER_BUTTON = (By.XPATH, "//div[@class='np-button'] //div[text()='Phone number']")
    CREDIT_CARD_BUTTON = (By.XPATH, "//div[text()='Credit Card']")
    PHONE_INPUT = (By.ID, "phone")
    PHONE_CODE_INPUT = (By.ID, "code")
    CARD_NUMBER = (By.ID, 'number')
    CARD_CODE = (By.ID, 'code')
    COMMENT_FIELD = (By.ID, "comment")
    BLANKET_AND_HANDKERCHIEFS = (By.XPATH,"//div[text()='Blanket and handkerchiefs']")
    ICE_CREAM_BUTTON = (By.CLASS_NAME, "counter-plus")
    ICE_CREAM_COUNTER = (By.CLASS_NAME, "counter-value")
    ORDER_MODAL = (By.CLASS_NAME, "order-body")
    SMART_BUTTON = (By.CLASS_NAME, "smart-button")
    LINK_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Link']")
    ORDER_REQUIREMENTS = (By.XPATH,"//div[contains(@class,'reqs-header')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    SEND_CODE_AGAIN_BUTTON = (By.CLASS_NAME, "send code again")
    PHONE_NUMBER_DISPLAY = (By.XPATH, "//div[text()='Phone number']")
    SUBMIT = (By.XPATH, "//button[@type='submit' and text()='Confirm']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    ADD_CARD = (By.XPATH, "//div[text()='Add card']")
    PAYMENT_METHOD = (By.XPATH, "//div[contains(@class, 'pp-text') and contains(text(), 'Payment method')]")
    BLANKET_CHECKBOX = (By.XPATH,"//input[@type='checkbox' and ancestor::div[contains(., 'Blanket and handkerchiefs')]]")
    CLOSE_BUTTON = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')


    def __init__(self, driver):
        self.driver = driver


    def set_from(self, value):
        return self.driver.find_element(*self.FROM_FIELD).send_keys(value)


    def set_to(self, value):
        return self.driver.find_element(*self.TO_FIELD).send_keys(value)

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()


    def click_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN).click()


    def set_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

        self.driver.find_element(*self.SUBMIT).send_keys()

        code = helpers.retrieve_phone_code(driver=self.driver)

        self.driver.find_element(*self.PHONE_INPUT).send_keys(code)

        self.driver.find_element(*self.SEND_CODE_AGAIN_BUTTON).click()

        self.driver.find_element(*self.SMART_BUTTON).click()

    def set_credit_card(self, card):
        self.driver.find_element(*self.CREDIT_CARD_BUTTON).click()

        self.driver.find_element(*self.CARD_NUMBER).send_keys(card)

    def set_comment_for_driver(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

    def click_add_ice_cream(self):
        element = self.driver.find_element(*self.ICE_CREAM_BUTTON)

        print("Displayed:", element.is_displayed())
        print("Enabled:", element.is_enabled())
        print(element.get_attribute("outerHTML"))

        element.click()


    def get_from_field_value(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")


    def get_to_field_value(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def get_comment_for_driver(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_attribute("value")


    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER).text


    def is_call_taxi_selected(self):
        return self.driver.find_element(*self.CALL_TAXI_BUTTON).is_displayed()


    def is_supportive_plan_selected(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN).is_displayed()


    def get_phone_number_entered(self):
        return self.driver.find_element(*self.PHONE_INPUT).get_attribute("value")


    def is_credit_card_selected(self):
        return self.driver.find_element(*self.CARD_NUMBER).is_displayed()

    def is_blanket_and_handkerchiefs_selected(self):
        checkbox = self.driver.find_element(*self.BLANKET_CHECKBOX)

        print("checked =", checkbox.get_property("checked"))
        print("selected =", checkbox.is_selected())

        return checkbox.get_property("checked")


    def is_modal_displayed(self):
        return self.driver.find_element(*self.ORDER_MODAL).is_displayed()


    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()


    def set_phone_code_input(self, code):
        self.driver.find_element(*self.PHONE_CODE_INPUT).send_keys(code)


    #def get_phone_number(self):
        #return self.driver.find_element(*self.PHONE_NUMBER_DISPLAY).get_attribute('value')

    def set_card_number(self, card_number):
        field = self.driver.find_element(*self.CARD_NUMBER)
        field.click()
        field.clear()
        field.send_keys(card_number)
        field.send_keys(Keys.TAB)


    def click_smart_button(self):
        self.driver.find_element(*self.SMART_BUTTON).click()

    def click_order_requirements(self):
        self.driver.find_element(*self.ORDER_REQUIREMENTS).click()

    def click_credit_card_button(self):
        self.driver.find_element(*self.CREDIT_CARD_BUTTON).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def set_phone_input(self, phone_number):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone_number)

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    def get_credit_card(self):
        self.driver.find_element(*self.CREDIT_CARD_BUTTON).get_attribute("value")

    #def set_card_code(self, card_code):
        self.driver.find_element(*self.CARD_CODE).send_keys()

    def set_card_code(self, card_code):
        fields = self.driver.find_elements(*self.CARD_CODE)

        for field in fields:
            if field.is_displayed():
                field.send_keys(card_code)
                return

        raise Exception("No visible card code field found")

    def get_credit_card_entered(self):
        return self.driver.find_element(*self.CARD_NUMBER).get_attribute("value")

    def get_credit_card_code_entered(self):
        return self.driver.find_element(*self.CARD_CODE).get_attribute("value")

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON).click()

    def click_blanket_and_handkerchiefs(self):
        elements = self.driver.find_elements(*self.BLANKET_AND_HANDKERCHIEFS)

        print("Matches found:", len(elements))

        for i, element in enumerate(elements):
            print(
                f"Element {i}:",
                "text=", repr(element.text),
                "displayed=", element.is_displayed(),
                "location=", element.location,
                "size=", element.size
            )

    def click_ice_cream_counter(self):
        self.driver.find_element(*self.ICE_CREAM_COUNTER).click()

    def click_close_button(self):
        self.driver.find_element(*self.CLOSE_BUTTON).click()