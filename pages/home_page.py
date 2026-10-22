
from playwright.sync_api import Page,expect,Locator
from settings import BASE_URL
from .breadcrumbs import BreadCrumbs

class HomePage:

    def __init__(self,page:Page):
        self.page = page
        self.breadcrumb = BreadCrumbs(self.page)

        #Static locators
        self.login_button = self.page.get_by_role("button",name = "Login")
        self.shopper_login_header = self.page.get_by_role("heading").filter(has_text='Shopper Login')
        self.cart_link = page.locator("#cart")

    #Dynamic Locators
    def username_header(self,username) -> Locator:
        return self.page.get_by_role("heading", name=f"Hello, {username}")
    
    def category_link(self,category:str):
        return self.page.get_by_role("link",name = category,exact=True)
    
    #Actions
    def navigate_to_homepage(self):
        self.page.goto(BASE_URL)
    
    def navigate_to_login_page(self):
        from .login_page import LoginPage
        self.login_button.click()
        expect(self.shopper_login_header).to_be_visible()
        login_page = LoginPage(self.page)
        return login_page
    
    def validate_username(self,username:str):
        expect(self.username_header(username)).to_be_visible()
    
    def navigate_to_category_plp_page(self,category:str):
        self.category_link(category=category).click()
        self.cart_link.hover()
        self.breadcrumb.validate_breadcrumb_link(link_name=category.lower())
        from .plp_page import PLPPage
        return PLPPage(self.page)

    def navigate_to_cart_page(self):
        self.cart_link.click()
        from .cart_page import CartPage
        self.breadcrumb.validate_breadcrumb_link(link_name="cart")
        return CartPage(self.page)




