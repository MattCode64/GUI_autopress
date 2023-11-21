import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def Screenshots(driver, config_file, page):
    """
    Function to take screenshot of all pages

    CSS Selector of element:
    div > book-cover > book-page:nth-child([ITERATE UNTIL MAX PAGE]) > div.page_location > svg

    :param page:
    :param driver:
    :param config_file:
    :return:
    """
    try:
        with open(config_file, "r", encoding='utf-8') as f:
            configJson = json.load(f)

        # First value of the dictionary
        shadow_path = list(configJson["shadow_root"].values())[0]

        # Call function to get shadow root
        shadow_root = GetShadowRoot(driver, shadow_path)

        # Take screenshot of the element
        print(page)
        css_selector = "div > book-cover > book-page:nth-child({}) > div.page_location > svg".format(page + 1)
        print("\nCSS Selector: ", css_selector)
        element = WebDriverWait(shadow_root, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

        # Open with config file to get the path of the folder
        with open(config_file, "r", encoding='utf-8') as f:
            configJson = json.load(f)

        # Get the path of the folder
        path = configJson["directories"]["image_dirOPI"]
        print("Path of the folder: ", path)

        # Save the element as a png file
        path = path + "\\{}.png".format(page)
        element.screenshot(path)
        print("~~~ Screenshot of page {} taken ~~~".format(page))
        print("Saved in {}".format(path))

    except Exception as e:
        print("Error while taking screenshot: ", e)
        return


def Processing(driver, config_file):
    """
    Function to take screenshot of all pages

    :param driver:
    :param config_file:
    :return:
    """
    # Get number of pages
    number_of_pages = GetNumberOfPages(driver, config_file)
    print("Number of pages: ", number_of_pages)

    # Convert number_of_pages to int
    number_of_pages = int(number_of_pages)

    # Iterate through all pages
    for page in range(1, number_of_pages + 1):
        print("Page number: ", page)
        Screenshots(driver, config_file, page)
        ChangePage(driver, config_file)
        print("Page changed")

    print("End of processing")


def GetNumberOfPages(driver, config_file):
    """
    Function to get the number of pages

    CSS Selector of element:
    nav > div > span.pages

    :param config_file:
    :param driver:
    :return:
    """
    try:
        with open(config_file, "r") as f:
            configJson = json.load(f)

        shadow_path = configJson["shadow_root"].values()
        shadow_path = list(shadow_path)[:-1]

        # Get shadow root
        shadow_root = GetShadowRoot(driver, shadow_path)

        # Get number of pages
        number_of_pages = WebDriverWait(shadow_root, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "nav > div > span.pages"))
        )
        print("Number of pages gotten")
        print("Number of pages: ", number_of_pages.text)
        # Convert number_of_pages to int
        return number_of_pages.text

    except Exception as e:
        print("Error while getting number of pages: ", e)
        return


def ChangePage(driver, config_file):
    """
    Function to change page

    CSS Selector of element:
    nav > button:nth-child(11) > span

    :param config_file:
    :param driver:
    :return:
    """
    try:
        with open(config_file, "r") as f:
            configJson = json.load(f)

        shadow_path = configJson["shadow_root"].values()
        shadow_path = list(shadow_path)[:-1]

        # Get shadow root
        shadow_root = GetShadowRoot(driver, shadow_path)

        change_page = WebDriverWait(shadow_root, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "nav > button:nth-child(11)"))
        )
        change_page.click()
        time.sleep(2)

    except Exception as e:
        print("Error while changing page or no more pages: ", e)
        return


def ReadMode(driver, config_file):
    """
    Function to activate read mode

    CSS Selector: #read-mode > button > span

    :param config_file:
    :param driver:
    :return:
    """
    try:
        with open(config_file, "r") as f:
            configJson = json.load(f)

        shadow_path = list(configJson["shadow_root"].values())
        print(type(shadow_path))
        print(shadow_path)

        shadow_driver = GetShadowRoot(driver, shadow_path)

        read_mode_button = WebDriverWait(shadow_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#read-mode > button > span"))
        )
        print("Read mode button gotten")
        read_mode_button.click()
        print("Read mode activated")

    except Exception as e:
        print("Error while activating read mode: ", e)
        return


def GetShadowRoot(driver, shadow_path):
    """
    Function to get the shadow root of the website

    :param driver:
    :param shadow_path:
    :return driver:
    """
    try:
        # If shadow path is a list, then code below. Else, it is a string so just get the shadow root
        if type(shadow_path) is list:
            for i, sequence in enumerate(shadow_path):
                print("Getting shadow root number " + str(i + 1))
                time.sleep(0.2)
                driver = driver.find_element(By.CSS_SELECTOR, sequence).shadow_root
                print("Shadow root number " + str(i + 1) + " gotten")

        else:
            driver = driver.find_element(By.CSS_SELECTOR, shadow_path).shadow_root
            print("Shadow root gotten")

        print("Final shadow root gotten")
        time.sleep(0.2)
        return driver

    except Exception as e:
        print("Error while getting shadow root: ", e)
        return
