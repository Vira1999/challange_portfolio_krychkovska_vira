import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    header_section_xpath = "//div[1]/header"
    menu_padding_xpath = "//div[1]/div/div/div/ul[1]"
    main_page_button_xpath = "//*[@class='MuiListItemIcon-root']/parent::div"
    players_button_xpath = "//div[1]/div/div/div/ul[1]/div[2]"
    language_button_xpath = "//div[1]/div/div/div/ul[2]//child::div"
    sign_out_button_xpath = "//div[1]/div/div/div/ul[2]/div[2]"
    players_count_section_xpath = "//div[contains(text(),'Players count')]//ancestor::div[2]"
    matches_count_section_xpath = "//div[contains(text(),'Matches count')]//ancestor::div[2]"
    reports_count_section_xpath = "//div[contains(text(),'Reports count')]//ancestor::div[2]"
    events_count_section_xpath = "//div[contains(text(),'Events count')]//ancestor::div[2]"
    dev_team_contact_hyperlink_xpath = "//a"
    add_player_hyperlink_xpath = "//*[@href='/en/players/add']"
    last_created_player_hyperlink_xpath = "//div[1]/main/div[3]/div[3]/div/div//child::a"
    last_updated_player_hyperlink_xpath = "//div[1]/main/div[3]/div[3]/div/div//child::a[2]"
    last_created_match_hyperlink_xpath = "//div[1]/main/div[3]/div[3]/div/div//child::a[3]"
    last_updated_match_hyperlink_xpath = "//div[1]/main/div[3]/div[3]/div/div//child::a[4]"
    last_updated_report_hyperlink_xpath = "//div[1]/main/div[3]/div[3]/div/div//child::a[5]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add/"
    expected_add_player_title_of_page = "Add player"
    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_hyperlink_xpath)

    def title_of_add_player_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_player_url) == self.expected_add_player_title_of_page

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    pass

