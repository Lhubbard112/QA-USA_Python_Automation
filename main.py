from selenium import webdriver
from pages import UrbanRoutesPage
import data
import helpers


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

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)

        assert self.routes_page.get_from_field_value() == data.ADDRESS_FROM
        assert self.routes_page.get_to_field_value() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.click_call_taxi_button()

        assert self.routes_page.is_call_taxi_selected()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.set_phone_number(data.PHONE_NUMBER)

        assert self.routes_page.is_phone_number_selected()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.set_credit_card(data.CARD_NUMBER)

        assert self.routes_page.is_credit_card_selected()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.set_comment_for_driver(data.MESSAGE_FOR_DRIVER)

        actual_comment = self.routes_page.get_comment_for_driver()

        assert actual_comment == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.click_blanket_and_handkerchiefs()

        assert self.routes_page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.add_ice_cream()

        assert self.routes_page.get_ice_cream_count() == "2"

    def test_car_search_modal_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        self.routes_page = UrbanRoutesPage(self.driver)

        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)

        self.routes_page.click_call_taxi_button()

        self.routes_page.set_phone_number(data.PHONE_NUMBER)
        self.routes_page.set_credit_card(data.CARD_NUMBER)

        self.routes_page.set_comment_for_driver(data.MESSAGE_FOR_DRIVER)

        self.routes_page.click_blanket_and_handkerchiefs()

        self.routes_page.add_ice_cream()

        assert self.routes_page.is_modal_displayed()
        assert self.routes_page.get_from_field_value() == data.ADDRESS_FROM
        assert self.routes_page.get_to_field_value() == data.ADDRESS_TO
        assert self.routes_page.is_supportive_plan_selected() is True
        assert self.routes_page.is_call_taxi_selected() is True
        assert self.routes_page.is_credit_card_selected() is True
        assert self.routes_page.is_phone_number_selected() is True
        assert self.routes_page.is_blanket_and_handkerchiefs_selected() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()