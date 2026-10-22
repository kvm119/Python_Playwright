import os

BASE_URL = "https://www.shoppersstack.com"
DEFAULT_BROWSER = "chrome"
HEADLESS = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Screenshot Settings
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

#report settings
REPORT_DIR = os.path.join(BASE_DIR, "reports")
REPORT_FILE = os.path.join(REPORT_DIR, f"report.html")