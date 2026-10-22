from playwright.sync_api import Page,expect,Locator,APIRequestContext

class AddressPage:

    def __init__(self,page:Page):
        self.page = page

        #Static locators
        self.select_a_delivery_address_header = page.get_by_role(role="heading",name="Select a delivery address")
        self.add_new_address_button = page.get_by_text("Add New Address")
        self.add_address_header = page.get_by_role("heading",name="Add Address")
        self.name_input = page.locator("#Name")
        self.house_info_input = page.locator("//*[@id='House/Office Info']")
        self.street_info_input = page.locator("//*[@id='Street Info']")
        self.landmark_input = page.locator("#Landmark")
        self.country_dropdown = page.locator("//select[@id='Country']")
        self.state_dropdown = page.locator("//select[@id='State']")
        self.city_dropdown = page.locator("//select[@id='City']")
        self.pincode_input = page.locator("#Pincode")
        self.phone_number_input = page.locator("//*[@id='Phone Number']")
        self.add_address_button = page.get_by_role("button", name="Add Address")
        self.successfully_added_toaster = page.get_by_text("Successfully Added")
        self.proceed_button = page.get_by_role("button",name="Proceed")

    
    #Dynamic Locators
    def address_type(self,name:str) -> Locator:
        return self.page.get_by_text(name)
    
    def select_address_radio_button(self,address_id:str):
        return self.page.locator(f"//input[@id='{address_id}']")

    #Actions
    def validate_select_a_delivery_address_header(self):
        expect(self.select_a_delivery_address_header).to_be_visible()

    def add_new_address_and_proceed(self,name:str,house_info:str,street_info:str,landmark:str,country:str,state:str,city:str,pincode:str,api_request_context:APIRequestContext,user_id:str,phone_number,jwt_token:str,address_type:str="Home"):
        self.add_new_address_button.click()

        expect(self.add_address_header).to_be_visible()
        self.name_input.fill(name)
        self.house_info_input.fill(house_info)
        self.street_info_input.fill(street_info)
        self.landmark_input.fill(landmark)
        self.country_dropdown.select_option(label=country)
        self.state_dropdown.select_option(label=state)
        self.city_dropdown.select_option(label=city)
        self.pincode_input.fill(pincode)
        self.phone_number_input.fill(phone_number)
        self.add_address_button.click()

        expect(self.successfully_added_toaster).to_be_visible()

        from api_utils.api_base import ApiBase
        api = ApiBase(api_request_context)
        addressid = api.get_all_addresses(user_id=user_id,jwt_token=jwt_token)[0]["addressId"]

        self.select_address_radio_button(address_id=addressid).click()
        self.proceed_button.click()

        from .breadcrumbs import BreadCrumbs
        breadcrumb = BreadCrumbs(self.page)
        breadcrumb.validate_breadcrumb_link(link_name="Payment Method")

        from .payment_page import PaymentPage
        payment_page = PaymentPage(self.page)

        return payment_page
