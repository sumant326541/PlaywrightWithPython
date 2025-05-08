from playwright.sync_api import Playwright
import pytest

def pytest_addoption(parser):
    parser.addoption("--play_browser",action="store",default="chromium",help="eBrowser type: chromium, firefox, webkit" )
    parser.addoption("--headless", action="store", default=False)
    
@pytest.fixture(scope="session")
def browser(playwright: Playwright,pytestconfig):
    browser_type = pytestconfig.getoption("--play_browser").lower()
    headless = pytestconfig.getoption("--headless")
    if browser_type == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_type == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        browser = playwright.chromium.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()