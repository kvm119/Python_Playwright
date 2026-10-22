import random
from playwright.sync_api import Page
import json

def generate_random_email():
    return f"user{random.randrange(10000,99999)}@gmail.com"

def get_products_from_local_storage(page:Page) -> list:
    page.wait_for_function(
        "() => localStorage.getItem('products') !== null",
        timeout=30000
    )
    products = page.evaluate("()=>localStorage.getItem('products')")

    return json.loads(products) if products else []