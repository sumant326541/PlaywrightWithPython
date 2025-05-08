from pages.home_page import HomePage
def test_search_product(page):
    home = HomePage(page)
    page.goto("https://www.flipkart.com")
    home.searchProduct("iphone")