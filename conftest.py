from playwright.sync_api import Playwright
import pytest
from pytest import Parser
from settings import DEFAULT_BROWSER,HEADLESS,SCREENSHOT_DIR,REPORT_FILE
from datetime import datetime
import os
import pytest_html

# ==========================================
# Configure HTML Report
# ==========================================

def pytest_configure(config):
    config.option.htmlpath = REPORT_FILE
    config.option.self_contained_html = True


# ==========================================
# Report Metadata
# ==========================================

def pytest_metadata(metadata):
    metadata["Project"] = "Playwright Automation"
    metadata["Execution Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==========================================
# Screenshot on Failure
# ==========================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    extras = getattr(report, "extras", [])

    if report.failed:
        page = item.funcargs.get("open_and_close_browser")

        if page:
            screenshot_name = f"{item.name}_{datetime.now().strftime('%H%M%S')}.png"
            screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)

            page.screenshot(path=screenshot_path)

            extras.append(pytest_html.extras.image(screenshot_path))
            report.extras = extras

def pytest_addoption(parser:Parser):
    parser.addoption("--browser_name",action="store",default = DEFAULT_BROWSER)
    parser.addoption("--headless",action="store",default = HEADLESS)

@pytest.fixture
def playwright_instance(playwright:Playwright):
    return playwright

@pytest.fixture
def open_and_close_browser(playwright_instance: Playwright,request):
    browser = str(request.config.getoption("--browser_name")).lower()
    headless = request.config.getoption("--headless")
    browser_instance = None
    if browser == "chrome":
        browser_instance = playwright_instance.chromium.launch(channel="chrome",headless=headless)
    elif browser in ["edge","msedge"] :
        browser_instance = playwright_instance.chromium.launch(channel="msedge",headless=headless)
    elif browser == "firefox":
        browser_instance = playwright_instance.firefox.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    page = browser_instance.new_page()
    
    yield page
    
    page.close()
    browser_instance.close()

@pytest.fixture
def api_request_context(playwright_instance:Playwright):
    request = playwright_instance.request.new_context(ignore_https_errors=True)
    yield request
    request.dispose()
