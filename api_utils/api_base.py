from playwright.sync_api import Page,APIRequestContext
from settings import BASE_URL

class ApiBase:

    def __init__(self,api_request_context):
        self.request_context:APIRequestContext= api_request_context

    def login_as_shopper(self,email:str,password:str)->dict:

        payload = {
            "email": email,
            "password": password,
            "role": "SHOPPER"
            }
        
        url = BASE_URL + "/shopping/users/login"
        response = self.request_context.post(url=url,data=payload)

        assert response.ok , "Login Failed!!!"

        return response.json()['data']
    
    def get_all_addresses(self,user_id:str,jwt_token:str):
        url = BASE_URL + f"/shopping/shoppers/{user_id}/address"
        headers = {
            "Authorization":f"Bearer {jwt_token}"
        }
        response = self.request_context.get(url=url,headers=headers)

        assert response.ok,"Failed to Fetch All Addresses!!!"
        addresses = response.json()['data']

        return addresses if addresses else []
    
    def delete_address(self,user_id:str,address_id:str,jwt_token:str):
        url = BASE_URL + f"/shopping/shoppers/{user_id}/address/{address_id}"
        headers = {
            "Authorization":f"Bearer {jwt_token}"
        }
        response = self.request_context.delete(url=url,headers=headers)
        assert response.ok,f"failed to delete address!!! addressid:{address_id}"

    def delete_all_addresses(self,user_id:str,jwt_token:str):
        for address_details in self.get_all_addresses(user_id=user_id,jwt_token=jwt_token):
            self.delete_address(user_id=user_id,address_id=address_details["addressId"],jwt_token=jwt_token)
        
    def get_all_orders(self,user_id:str,jwt_token:str):
        url = BASE_URL + f"/shopping/shoppers/{user_id}/orders"
        headers = {
            "Authorization":f"Bearer {jwt_token}"
        }
        response = self.request_context.get(url=url,headers=headers)

        assert response.ok,"Failed order details!!!"

        return response.json()['data']
    
    def get_all_cart_items(self,user_id:str,jwt_token:str):
        url = BASE_URL+f"/shopping/shoppers/{user_id}/carts"
        headers = {
            "Authorization":f"Bearer {jwt_token}"
        }
        response = self.request_context.get(url=url,headers=headers)

        assert response.ok,"Failed to fetch cart items!!!"

        return response.json()['data']
    
    def delete_cart_item(self,user_id:str,cart_item_id:str,jwt_token:str):
        url = BASE_URL+f"/shopping/shoppers/{user_id}/carts/{cart_item_id}"
        headers = {
            "Authorization":f"Bearer {jwt_token}"
        }
        response = self.request_context.delete(url=url,headers=headers)
        assert response.ok,f"failed to delete cart item!!! cart_item_id:{cart_item_id}"

    def delete_all_cart_items(self,user_id:str,jwt_token:str):
        for cart_details in self.get_all_cart_items(user_id=user_id,jwt_token=jwt_token):
            self.delete_cart_item(user_id=user_id,cart_item_id=cart_details["productId"],jwt_token=jwt_token)





        
    
    