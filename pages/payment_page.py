from playwright.sync_api import Page,expect,Locator

class PaymentPage:

    def __init__(self,page:Page):
        self.page = page

        #Static locators
        self.payment_header = page.get_by_role("heading",name="Select a payment method")
        self.cash_on_delivery_radio_button = page.get_by_text("Cash On Delivery (COD)")
        self.proceed_button = page.get_by_role("button",name="Proceed")

    #Dynamic Locators

    
    #Actions
    def select_cash_on_delivery_and_proceed(self):
        from .order_confirmation_page import OrderConfirmationPage

        expect(self.payment_header).to_be_visible()

        self.cash_on_delivery_radio_button.click()
        self.proceed_button.click()

        return OrderConfirmationPage(self.page)