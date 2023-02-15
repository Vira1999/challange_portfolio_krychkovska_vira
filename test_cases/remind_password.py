import os
import time
import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPassword(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remind_password(self):
        user_login = LoginPage(self.driver)
        time.sleep(2)
        user_login.click_on_the_remind_password_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
