from playwright.sync_api import Page,expect,Locator
from settings import BASE_URL

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        #Static Locators
        self.shopper_login_button =page.get_by_role("tab",name = "Shopper Login")
        self.email_input = page.locator("//input[@id='Email']")
        self.password_input = page.locator("//input[@id='Password']")
        self.login_button = page.get_by_role("button",name ="Login")
        self.create_account_button = page.get_by_text("Create Account")
    
    #Dynamic Locators
    def gender_radio_button(self,gender:str)-> Locator:
        return self.page.get_by_role("radio",name = gender)
    
    # Actions
    def navigate_to_login_page(self):
        self.page.goto(BASE_URL + "/user-signin")

    def login_as_shopper(self,email:str, password:str):
        from .home_page import HomePage
        self.shopper_login_button.click()

        self.email_input.fill(email)
        self.password_input.fill(password)

        self.login_button.click()

        return HomePage(self.page)

    def navigate_to_shopper_signup_page(self):
        from .signup_page import SignUpPage
        self.shopper_login_button.click()
        self.create_account_button.click()

        return SignUpPage(self.page)