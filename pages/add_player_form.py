from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    submit_button_xpath = "//*[text() = 'Submit']"

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)





    pass