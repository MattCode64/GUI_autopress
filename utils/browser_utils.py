import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
from utils.config_utils import get_json_file


def open_website(driver, web_name):
    """
    Open the website

    :param driver:
    :param web_name:
    :return:
    """
    try:
        url = get_url(web_name)
        driver.get(url)
        print("Website opened")
        time.sleep(1)

    except Exception as e:
        print("Error while opening website: ", e)
        return


def get_url(web_name):
    """
    Get the url from the config file

    :param web_name:
    :return url:
    """
    try:
        url = get_json_file("url")[web_name]
        return url

    except Exception as e:
        print("Error while getting url: ", e)
        return


def setup_driver(browser_name):
    """
    Function to initialize the browser driver depending on the browser name

    :param browser_name:
    :return:
    """
    try:
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            # Add option to start the browser in format 1280 x 720.
            options.add_argument("--window-size=720,1280")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            # Add option to not ask for where to save the file.
            options.add_experimental_option("prefs", {
                "download.prompt_for_download": False,  # Désactive la demande de confirmation avant le téléchargement
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True  # Active la protection de navigation
            })
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
