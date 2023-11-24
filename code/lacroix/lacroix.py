from utils.browser_utils import setup_driver, quit_driver, open_website
import time


def lacroix():
    print("Hello from lacroix.py")
    print("Starting lacroix.py")

    # Setup Driver
    web_driver = setup_driver('chrome')

    # Open website with wait
    open_website(web_driver, "lacroix")
    time.sleep(50000)

    # Quit Driver
    quit_driver(web_driver)

    print("Ending figaro.py")
