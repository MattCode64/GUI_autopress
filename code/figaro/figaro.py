from utils.browser_utils import setup_driver, quit_driver, get_json
import time


def figaro():
    print("Hello from figaro.py")
    print("Starting figaro.py")

    # Setup Driver
    web_driver = setup_driver('chrome')
    time.sleep(5)

    get_json()

    # Quit Driver
    quit_driver(web_driver)

    print("Ending figaro.py")
