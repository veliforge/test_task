from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto('https://highlifeshop.com/cafe')
        page.get_by_role("button", name="DECLINE ALL NON-ESSENTIAL").click()


        self.dropdown_sorter = self.page.locator("ul").filter(has_text="Default New Arrivals Product A-Z").get_by_role("listitem")
        self.sort_by_product_name_asc_btn = (self.page.locator("li.product_asc"))
        self.sort_by_product_name_desc_btn = (self.page.locator("li.product_desc"))
        self.sort_by_product_name_price_asc_btn = (self.page.locator("li.price_asc"))
        self.sort_by_product_name_price_desc_btn = (self.page.locator("li.price_desc"))

        self.loading_mask = page.locator("div.loading-mask")


    def get_list_of_product_by_text(self):
        self.list_of_product = self.page.locator("strong.product-item-name").all_inner_texts()

    def get_list_of_product_by_price(self):
        self.list_of_product_price = self.page.locator("span.price").filter(has_text="AVIOS").all_inner_texts()


