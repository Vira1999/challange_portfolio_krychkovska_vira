from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    header_section_xpath = "//div[1]/header"
    menu_padding_xpath = "//div[1]/div/div/div/ul[1]"
    main_page_button_xpath = "//*[@class='MuiListItemIcon-root']/parent::div"
    players_button_xpath = "//div[1]/div/div/div/ul[1]/div[2]"
    players_name_button_xpath = "//div[1]/div/div/div/ul[2]//child::div"
    matches_button_xpath = "//div[1]/div/div/div/ul[2]/div[2]"
    reports_button_xpath = "//div[1]/div/div/div/ul[2]/div[3]"
    language_button_xpath = "//div[1]/div/div/div/ul[2]/div[4]"
    sign_out_button_xpath = "//div[1]/div/div/div/ul[2]/div[5]"
    my_team_field_xpath = "//input[contains(@name, 'myTeam')]"
    enemy_team_field_xpath = "//input[contains(@name, 'enemyTeam')]"
    my_team_score_field_xpath = "//input[contains(@name, 'myTeamScore')]"
    enemy_team_score_field_xpath = "//input[contains(@name, 'enemyTeamScore')]"
    date_field_xpath = "//input[contains(@type, 'date')]"
    match_at_home_radiobutton_xpath = "//fieldset/div/label[1]/span[1]"
    match_out_home_radiobutton_xpath = "//fieldset/div/label[2]/span[1]"
    t_shirt_color_field_xpath = "//input[contains(@name, 'tshirt')]"
    league_field_xpath = "//input[contains(@name, 'league')]"
    time_played_field_xpath = "//input[contains(@name, 'timePlayed')]"
    number_field_xpath = "//input[contains(@name, 'number')]"
    web_match_field_xpath = "//input[contains(@name, 'webMatch')]"
    general_field_xpath = "//input[contains(@name, 'general')]"
    rating_field_xpath = "//input[contains(@name, 'rating')]"
    submit_button_xpath = "//button[contains(@type, 'submit')]"
    clear_button_xpath = "//button[2]"

    pass