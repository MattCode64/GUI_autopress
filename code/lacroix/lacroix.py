from utils.browser_utils import setup_driver, quit_driver, open_website
from utils.navigation_utils import navigation
import time


def lacroix():
    print("Hello from lacroix.py")
    print("Starting lacroix.py")

    # Setup Driver
    web_driver = setup_driver('chrome')

    # Open website with wait
    website_name = "lacroix"
    open_website(web_driver, website_name)

    # Navigation
    navigation(web_driver, website_name)

    # Quit Driver
    quit_driver(web_driver)

    print("Ending lacroix.py")
