from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class PlayersPage(BasePage):
    filter_table_button_xpath = "//*[@aria-label = 'Filter Table']"
    name_input_field_xpath = "//div[1]/div/div/div/input"
    close_button_xpath = "//*[@aria-label = 'Close']"

    def click_on_the_filter_table_button(self):
        self.click_on_the_element(self.filter_table_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.name_input_field_xpath, name)


    def click_on_the_close_button(self):
        self.click_on_the_element(self.close_button_xpath)


    pass