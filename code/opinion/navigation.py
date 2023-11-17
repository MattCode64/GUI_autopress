from opinion import *


def Processing(driver, config_file):
    """
    Function to take screenshot of all pages

    :param driver:
    :param config_file:
    :return:
    """
    try:
        page = 1
        while True:
            # Take screenshot
            SaveElement(driver, config_file, page)

            # Change page
            ChangePage(driver, config_file)

            # Increment page
            page += 1

    except Exception as e:
        print("Error while processing or no more pages: ", e)
        return


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
        time.sleep(5)

    except Exception as e:
        print("Error while changing page: ", e)
        return


def SaveElement(driver, config_file, page):
    """
    Function to get in shadow root and take screenshot

    Element is in first shadow root

    CSS Selector of element:
    div > book-cover > book-page:nth-child(2) > div.page_location.zoomed > svg


    :param page:
    :param config_file:
    :param driver:
    :return:
    """
    with open(config_file, "r") as f:
        configJson = json.load(f)

    # First value of the dictionary
    shadow_path = list(configJson["shadow_root"].values())[0]

    # Get shadow root
    shadow_root = GetShadowRoot(driver, shadow_path)

    element = WebDriverWait(shadow_root, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div > book-cover > book-page:nth-child(2) > div.page_location > svg"))
    )

    path = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\images\{}.png".format(page)
    element.screenshot(path)
    print("Screenshot of page {} taken".format(page))
    # try:
    #     with open(config_file, "r") as f:
    #         configJson = json.load(f)
    #
    #     # First value of the dictionary
    #     shadow_path = list(configJson["shadow_root"].values())[0]
    #     print(shadow_path)
    #
    #     # Get shadow root
    #     shadow_root = GetShadowRoot(driver, shadow_path)
    #
    #     element = WebDriverWait(shadow_root, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, "div > book-cover > book-page:nth-child(2) > div.page_location > svg"))
    #     )
    #
    #     element.screenshot(r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\images\1.png")
    #
    #     print("Screenshot taken")
    #
    # except Exception as e:
    #     print("Error while taking screenshot: ", e)
    #     return


def ReadMode(driver, config_file, value):
    """
    Function to activate read mode

    CSS Selector: #read-mode > button > span

    :param config_file:
    :param value:
    :param driver:
    :return:
    """
    try:
        with open(config_file, "r") as f:
            configJson = json.load(f)

        shadow_path = configJson[value].values()
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
                time.sleep(2)
                driver = driver.find_element(By.CSS_SELECTOR, sequence).shadow_root
                print("Shadow root number " + str(i + 1) + " gotten")

        else:
            driver = driver.find_element(By.CSS_SELECTOR, shadow_path).shadow_root
            print("Shadow root gotten")

        print("Final shadow root gotten")
        time.sleep(2)
        return driver

    except Exception as e:
        print("Error while getting shadow root: ", e)
        return


if __name__ == '__main__':
    print("Start of program")
    config = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\config\config.json"

    # Setup Driver
    edge_driver = SetupDriver()

    # Open Website
    OpenWebsite(edge_driver, config, "lopinion")

    # Accept Cookies
    AcceptCookies(edge_driver)

    # Switch to iframe
    SwitchIframe(edge_driver)

    # Sign In
    SignIn(edge_driver, config, "lopinion")

    Processing(edge_driver, config)

    QuitDriver(edge_driver)
    print("End of program")
