import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSearchingName(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sign_out_of_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        time.sleep(2)
        user_login.click_on_the_sign_in_button()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_the_players_button()
        time.sleep(2)
        players_page = PlayersPage(self.driver)
        players_page.click_on_the_filter_table_button()
        time.sleep(2)
        players_page.type_in_name('cat')
        time.sleep(2)
        players_page.click_on_the_close_button()
        time.sleep(2)



    @classmethod
    def tearDown(self):
        self.driver.quit()
