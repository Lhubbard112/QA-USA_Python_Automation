from selenium import webdriver
from pages import UrbanRoutesPage
import data
import helpers
import time


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)

        assert routes_page.get_from_field_value() == data.ADDRESS_FROM
        assert routes_page.get_to_field_value() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_plan()
        assert routes_page.is_supportive_plan_selected()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_plan()
        routes_page.click_phone_number_button()
        routes_page.set_phone_input(data.PHONE_NUMBER)
        routes_page.click_next_button()
        time.sleep(1)
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.set_phone_code_input(code)
        routes_page.click_confirm_button()
        expected_value = data.PHONE_NUMBER
        actual_value = routes_page.get_phone_number_entered()
        assert expected_value == actual_value

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_plan()
        routes_page.click_payment_method()
        routes_page.click_add_card()
        time.sleep(1)
        routes_page.set_card_number(data.CARD_NUMBER)
        routes_page.set_card_code(data.CARD_CODE)
        time.sleep(5)
        routes_page.click_link_button()
        expected_value = data.CARD_NUMBER
        actual_value = routes_page.get_credit_card_entered()
        assert expected_value == actual_value

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_plan()
        routes_page.set_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        routes_page.get_comment_for_driver()
        expected_value = data.MESSAGE_FOR_DRIVER
        actual_comment = routes_page.get_comment_for_driver()
        assert actual_comment == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_plan()
        routes_page.click_order_requirements()
        time.sleep(2)
        routes_page.click_blanket_and_handkerchiefs()
        assert routes_page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_plan()
        time.sleep(2)
        ice_creams=2
        for i in range(ice_creams):
            routes_page.click_add_ice_cream()
        assert routes_page.get_ice_cream_count() == "2"

    def test_car_search_modal_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_call_taxi_button()
        routes_page.click_supportive_plan()
        routes_page.click_phone_number_button()
        routes_page.set_phone_input(data.PHONE_NUMBER)
        routes_page.click_next_button()
        time.sleep(1)
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.set_phone_code_input(code)
        routes_page.click_confirm_button()
        routes_page.click_payment_method()
        routes_page.click_add_card()
        time.sleep(1)
        routes_page.set_card_number(data.CARD_NUMBER)
        routes_page.set_card_code(data.CARD_CODE)
        time.sleep(5)
        routes_page.click_link_button()
        routes_page.click_close_button()
        routes_page.set_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        routes_page.click_blanket_and_handkerchiefs()
        ice_creams = 2
        for i in range(ice_creams):
            routes_page.click_add_ice_cream()
        routes_page.click_smart_button()
        assert routes_page.is_modal_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
