import time

from utils.browser_utils import setup_driver, quit_driver, open_website
from utils.navigation_utils import navigation


def liberation():
    print("Hello from liberation.py")
    print("Starting liberation.py")

    # Setup Driver
    web_driver = setup_driver('chrome')

    # Open website with wait
    website_name = "liberation"
    open_website(web_driver, website_name)
    # time.sleep(100)

    # Navigation
    navigation(web_driver, website_name)

    # Quit Driver
    quit_driver(web_driver)

    print("Ending liberation.py")
