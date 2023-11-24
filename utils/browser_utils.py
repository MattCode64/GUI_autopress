import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.config_utils import *


def get_json():
    get_json_file("lefigaro")
    print("GOOD in get_json in browser_utils.py")


def setup_driver(browser_name):
    """
    Function to initialize the browser driver depending on the browser name

    :param browser_name:
    :return:
    """
    try:
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
            print("Driver Initialized")

        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Firefox(options=options)
            print("Driver Initialized")

        elif browser_name.lower() == 'edge':
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(options=options)
            print("Driver Initialized")

        else:
            raise ValueError("Unsupported browser")

        return driver

    except WebDriverException as e:
        print("Error while setup webdriver: ", e)
        return

    except Exception as e:
        print("Error while setup webdriver: ", e)
        return


def quit_driver(driver):
    """
    Function to quit the driver

    :return:
    """
    try:
        if isinstance(driver, webdriver.Edge) or isinstance(driver, webdriver.Chrome) or isinstance(driver,
                                                                                                    webdriver.Firefox):
            driver.quit()
            print("Driver quit")

        else:
            print("Driver is not webdriver.Edge, Chrome or Firefox type, maybe shadow root.")
            return

    except Exception as e:
        print("Error while quitting driver: ", e)
        return
