# conftest.py
import pytest
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption("--play_browser", action="store", default="chromium", help="Browser type: chromium, firefox, webkit")
    parser.addoption("--headless", action="store", default="true", help="Run browser in headless mode (true/false)")

@pytest.fixture(scope="session")
def browser(playwright: Playwright, pytestconfig):
    # Get the browser type (chromium, firefox, or webkit)
    browser_type = pytestconfig.getoption("--play_browser").lower()
    
    # Get headless mode value (it will be a string "true" or "false")
    headless = pytestconfig.getoption("--headless").lower() == "true"
    
    # Launch the appropriate browser in headless mode or not based on the --headless option
    if browser_type == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_type == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        browser = playwright.chromium.launch(headless=headless)
    
    yield browser
    browser.close()
