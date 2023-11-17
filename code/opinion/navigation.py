import time

from opinion import *


def SaveElement(driver):
    """
    Function to get in shadow root and take screenshot

    Element is in first shadow root

    CSS Selector of element:
    div > book-cover > book-page:nth-child(2) > div.page_location.zoomed > svg


    :param driver:
    :return:
    """
    try:
        # Get shadow root
        shadow_root = GetShadowRoot(driver, ["body > epaper-application > div > view-publication"])
        # Take
        # time.sleep(533333)
        element = WebDriverWait(shadow_root, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div > book-cover > book-page:nth-child(2) > div.page_location > svg"))
        )

        # Save element entirely without screenshot
        element.screenshot(r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\images\1.png")

        # Print the size of the element
        print("Element size: ", element.size)
        print("Screenshot taken")

    except Exception as e:
        print("Error while taking screenshot: ", e)
        return


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
        for i, sequence in enumerate(shadow_path):
            print("Getting shadow root number " + str(i + 1))
            time.sleep(2)
            driver = driver.find_element(By.CSS_SELECTOR, sequence).shadow_root
            print("Shadow root number " + str(i + 1) + " gotten")

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

    # Read Mode
    # ReadMode(edge_driver, config, "shadow_root")
    time.sleep(20)

    # Screenshot Element
    SaveElement(edge_driver)

    # # Scroll Pixels
    # ScrollPixels(shadow_driver, 500)
    # ScrollPixels(edge_driver, 500)

    # Quit Driver
    QuitDriver(edge_driver)
    print("End of program")
