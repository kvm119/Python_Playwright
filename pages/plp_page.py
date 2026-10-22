from playwright.sync_api import Page,expect
import time

class PLPPage:

    def __init__(self,page:Page):
        self.page = page

        #Static Locators
        self.first_product_card = page.locator("//div[contains(@class,'productCard')]").nth(0)
        self.first_product_name = self.first_product_card.locator("//div[contains(@class,'featuredProducts_footerLeft__PmkNa')]/span").first
        self.first_product_add_to_cart_button = self.first_product_card.get_by_role("button",name= "add to cart")
        self.first_product_added_button = self.first_product_card.get_by_role("button",name= "added")
        self.first_product_price = self.first_product_card.locator("//p[contains(@class,'CalculateOffer_wrapper')]/span").first

    def add_first_product_to_cart(self):
        name = self.first_product_name.text_content()
        price = self.first_product_price.text_content()
        time.sleep(3)
        if self.first_product_add_to_cart_button.is_visible():
            self.first_product_add_to_cart_button.hover()
            self.first_product_add_to_cart_button.click()
        expect(self.first_product_added_button).to_be_visible()

        return (name,price)

