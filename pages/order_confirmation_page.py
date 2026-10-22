from playwright.sync_api import Page,expect,Locator

class OrderConfirmationPage:

    def __init__(self,page:Page):
        self.page = page

        #Static locators
        self.order_confirmation_header = page.get_by_role("heading",name="Order Confirmed")
        self.orderid_text = page.locator("//b[contains(.,'#')]")

    #Dynamic Locators

    #Actions
    def get_order_id(self):
        return self.orderid_text.text_content().strip().strip("#")