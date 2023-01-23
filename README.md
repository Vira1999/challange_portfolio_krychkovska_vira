# framework_test
# Task 1: software configuration
## Subtask 1: Why did I choose to participate in the Dare IT Challenge?
Testing is an fast changing proffesion. You should test different applications using different browsers or devices, utilizing different user roles, and varied paths through the system. So, it's never be boring and I really love it!
Moreover, I want to improve my knowledge, so that is why I want to switch on the QA automatization. *(It's not actually switching because of the same goal, but it is more interesting as for me.)*
Dare IT it is huge opportunity to get some experience in real cases and to know how to mix all this programs to find **THE BUG** :smiley:
To my mind, I can spend enough time to sink my teeth in to this challange.

# TASK 2: Selectors
### login_input_xpath:
//*[@id="login"]  
//input[contains(@id, "login")]  
//input[contains(@name, "login")]  

### login_label_xpath:
//*[@id="login-label"]  
//label[@id = 'login-label' and @for = ‘login’]  
//input[@id='login']

### password_input_xpath:
//*[@id="password"]  
//input[starts-with(@name,'pass')]  
//input[@id='password']

### password_label_xpath:
//*[@id="password-label"]  
//*[@for="password"]  
//label[starts-with(@for,'pass')]

### english_unordered_list_item_xpath:
//*[@id="menu-"]/div[3]/ul/li[2]  
//parent::ul/li[2]    
//div[3]/ul/li[2]

### polish_unordered_list_item_xpath:
//span[@class='MuiTouchRipple-root']/parent::li   
//parent::ul/li    
//*[@id="menu-"]/div[3]/ul/li[1]

### sign_in_button_xpath:
//span[@class='MuiTouchRipple-root']//parent::button  
//span[@class='MuiButton-label']/parent::button  
//*[text()="Sign in"]