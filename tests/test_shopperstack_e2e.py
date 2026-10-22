from pages.login_page import LoginPage
from test_data.e2e_testdata import *
from utils.utils import generate_random_email,get_products_from_local_storage
from api_utils.api_base import ApiBase
import time

def test_end_to_end(open_and_close_browser,api_request_context):
    #open browser and navigate to login page
    page = open_and_close_browser
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()

    #Create a shopper account
    random_email = generate_random_email()
    signup_page = login_page.navigate_to_shopper_signup_page()
    home_page = signup_page.create_shopper_account(first_name=first_name,last_name=last_name,phone_number=phone_number,gender=gender,email_address=random_email,password=password)

    #login with new account
    home_page.navigate_to_login_page()
    home_page = login_page.login_as_shopper(email=random_email,password=password)
    home_page.validate_username(username=first_name)

    #login through api
    response = ApiBase(api_request_context).login_as_shopper(email=random_email,password=password)
    api = ApiBase(api_request_context)

    shopper_id = response['userId']
    jwt_token = response['jwtToken']
    zone_id = response['zoneId']

    products_list = get_products_from_local_storage(page=page)

    #Add product to cart
    plp_page = home_page.navigate_to_category_plp_page(category=product_category)
    product_name,product_price = plp_page.add_first_product_to_cart()
    cart_page = home_page.navigate_to_cart_page()
    cart_page.validate_cart_product(name=product_name,price=product_price)

    #Delete all address with Api
    api.delete_all_addresses(user_id=shopper_id,jwt_token=jwt_token)

    #create new Address
    address_page = cart_page.click_on_buy_now()
    address_page.validate_select_a_delivery_address_header()
    payment_page = address_page.add_new_address_and_proceed(name=Address_name,house_info=Address_House_info,street_info=Address_Street_info,landmark=Address_Landmark,country=Address_Country,state=Address_State,city=Address_City,pincode=Address_Pincode,api_request_context=api_request_context,user_id=shopper_id,phone_number=Address_Phone_number,jwt_token=jwt_token)

    #select cash on deleivery and proceed
    order_confirmation_pae = payment_page.select_cash_on_delivery_and_proceed()

    #Validate order confirmation
    order_id = order_confirmation_pae.get_order_id()
    orders = api.get_all_orders(user_id=shopper_id,jwt_token=jwt_token)
    assert int(order_id) in [order["orderId"] for order in orders],"Orderid is not exist"