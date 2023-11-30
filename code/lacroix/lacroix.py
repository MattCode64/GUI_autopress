from utils.browser_utils import setup_driver, quit_driver, open_website
from utils.navigation_utils import navigation


def lacroix():
    print("\033[93m" + "LA CROIX" + "\033[0m")

    # Setup Driver
    web_driver = setup_driver('chrome')

    # Open website with wait
    website_name = "lacroix"
    open_website(web_driver, website_name)

    # Navigation and Automation
    navigation(web_driver, website_name)

    # Quit Driver
    quit_driver(web_driver)

    print("\033[93m" + "END LA CROIX" + "\033[0m")
