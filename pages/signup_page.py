from playwright.sync_api import Page,expect,Locator
from settings import BASE_URL

class SignUpPage:
    def __init__(self, page:Page):
        self.page = page

        #Static Locators
        self.create_your_profile_header = page.get_by_role("heading",name="Create Your Profile")
        self.first_name_input = page.locator("//input[@id='First Name']")
        self.last_name_input = page.locator("//input[@id='Last Name']")
        self.phone_number_input = page.locator("//input[@id='Phone Number']")
        self.email_address_input = page.locator("//input[@id='Email Address']")
        self.password_input = page.locator("//input[@id='Password']")
        self.confirm_password_input = page.locator("//input[@id='Confirm Password']")
        self.terms_and_conditions_checkbox = page.locator("//input[@id='Terms and Conditions']")
        self.register_button = page.get_by_role("button",name ="Register")
        self.successfully_registered_toaster = page.get_by_text("Successfully Registered")
    
    #Dynamic Locators
    def gender_radio_button(self,gender:str)-> Locator:
        return self.page.locator(f"#{gender}")
    
    # Actions
    
    def create_shopper_account(self,first_name:str, last_name:str,phone_number:str,email_address:str,password:str,gender:str="Other"):
        from .home_page import HomePage

        expect(self.create_your_profile_header).to_be_visible()

        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.gender_radio_button(gender=gender).click()
        self.phone_number_input.fill(phone_number)
        self.email_address_input.fill(email_address)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.terms_and_conditions_checkbox.click()

        self.register_button.click()

        expect(self.successfully_registered_toaster).to_be_visible()

        return HomePage(self.page)        



