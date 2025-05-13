import pytest
from pages.home_page import HomePage

@pytest.mark.regression
def test_search_product(page):
    home = HomePage(page)
    page.goto("https://www.flipkart.com")
    home.searchProduct("iphone")

@pytest.mark.smoke
#@pytest.mark.skip(reason="This test is being skipped temporarily")
def test_verify_title(page):
    home = HomePage(page)
    url = "https://www.flipkart.com/"
    page.goto(url)
    current_url = page.url
    print(f"Current URL: {current_url}")
    assert current_url == url, f"Unexpected URL: {current_url}"