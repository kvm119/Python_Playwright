from playwright.sync_api import Page,expect,Locator

class CartPage:

    def __init__(self,page:Page):
        self.page = page

        #Static locators
        self.cart_product_container = page.locator("//div[contains(@class,'cart_checkoutProductContainer')]")
        self.buy_now_button = page.get_by_text("Buy Now")
        self.continue_shopping_button = page.get_by_text("Continue Shopping")

    #Dynamic Locators
    def cart_product_name(self,name) -> Locator:
        return self.cart_product_container.get_by_role("heading",name=name)
    def cart_product_price(self,price) -> Locator:
        return self.cart_product_container.get_by_text(price)
    
    #Actions
    def click_on_buy_now(self):
        from .address_page import AddressPage

        self.buy_now_button.click()
        address_page = AddressPage(self.page)
        address_page.validate_select_a_delivery_address_header()

        return address_page
    
    def validate_cart_product(self,name:str,price:str):
        expect(self.cart_product_name(name)).to_be_visible()
        expect(self.cart_product_price(price)).to_be_visible()
