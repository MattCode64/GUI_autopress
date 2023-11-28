from utils.browser_utils import setup_driver, quit_driver, open_website
from utils.navigation_utils import navigation
import time


def figaro():
    print("Hello from figaro.py")
    print("Starting figaro.py")

    # Setup Driver
    web_driver = setup_driver('chrome')

    # Open website with wait
    website_name = "lefigaro"
    open_website(web_driver, website_name)
    time.sleep(1000)

    # Navigation
    navigation(web_driver, website_name)

    # Quit Driver
    quit_driver(web_driver)

    print("Ending figaro.py")
