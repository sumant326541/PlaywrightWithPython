from playwright.sync_api import Page
class HomePage:
    def __init__(self,page:Page):
        self.searchbox_input = page.locator("[placeholder='Search for Products, Brands and More']")
        self.searchbox_Button= page.locator("(//*[@type='submit'])[1]")

    def searchProduct(self,product):
        self.searchbox_input.fill(product)
        self.searchbox_Button.click()
