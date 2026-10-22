from playwright.sync_api import Page,expect,Locator

class BreadCrumbs:

    def __init__(self,page:Page):
        self.page = page

        #Static locators
    
    #Dynamic Locators
    def page_link_breadcrumb(self,name:str)-> Locator:
        return self.page.locator(f"//a[text()='{name}']")

    #Actions
    def validate_breadcrumb_link(self,link_name:str):
        expect(self.page_link_breadcrumb(link_name)).to_be_visible()