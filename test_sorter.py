from models.product_page import ProductPage
from playwright.sync_api import expect, Page


def test_sorting_by_name(page: Page):
    product_page = ProductPage(page)
    product_page.dropdown_sorter.click()
    expect(product_page.sort_by_product_name_asc_btn).to_be_visible()

    product_page.sort_by_product_name_asc_btn.click()
    expect(product_page.dropdown_sorter).to_be_editable()
    expect(product_page.loading_mask).not_to_be_visible()

    product_page.get_list_of_product_by_text()
    assert product_page.list_of_product == sorted(product_page.list_of_product)


def test_sorting_by_price(page: Page):
    product_page = ProductPage(page)
    product_page.dropdown_sorter.click()
    expect(product_page.sort_by_product_name_price_desc_btn).to_be_visible()

    product_page.sort_by_product_name_price_desc_btn.click()
    expect(product_page.dropdown_sorter).to_be_editable()
    expect(product_page.loading_mask).not_to_be_visible()

    product_page.get_list_of_product_by_price()
    assert product_page.list_of_product_price == sorted(product_page.list_of_product_price, reverse=True)

