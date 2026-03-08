import re
import os
from splinter.browser import Browser

def chrome_browser(headless=True):
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")  # recommended headless mode
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    prefs = {
        "credentials_enable_service": False,  # disable password manager
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    return Browser("chrome", options=chrome_options)

def firefox_browser(headless=True):
    return Browser("firefox", headless=headless)

def before_all(context):
    context.browser = chrome_browser(headless=True)
    # Alternatively, use `firefox_browser` and headless=False to see the browser while testing

def after_all(context):
    context.browser.quit()
    context.browser = None

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text

def after_step(context, step):
    if step.status == "failed":
        feature = slugify(context.feature.name)
        scenario = slugify(context.scenario.name)
        step_name = slugify(step.name)
        os.makedirs("screenshots", exist_ok=True)
        filename = f"screenshots/{feature}__{scenario}__{step_name}.png"
        context.browser.driver.save_screenshot(filename)
