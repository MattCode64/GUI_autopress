from opinion import *


def ReadMode(driver):
    """
    Function to activate read mode

    CSS Selector: #read-mode > button > span

    :param driver:
    :return:
    """
    try:
        read_mode_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#read-mode > button > span"))
        )
        print("Read mode button gotten")
        read_mode_button.click()
        print("Read mode activated")

    except Exception as e:
        print("Error while activating read mode: ", e)
        return

    # read_mode_button = driver.find_element(By.CSS_SELECTOR, "#read-mode > button > span")
    # print("Read mode button gotten")
    # time.sleep(5)
    # read_mode_button.click()
    # print("Read mode activated")
    # time.sleep(5)


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
            time.sleep(0.5)
            driver = driver.find_element(By.CSS_SELECTOR, sequence).shadow_root
            print("Shadow root number " + str(i + 1) + " gotten")

        print("Final shadow root gotten")
        # time.sleep(5)
        return driver

    except Exception as e:
        print("Error while getting shadow root: ", e)
        return

    # shadow_root = driver.find_element(By.CSS_SELECTOR, "body > epaper-application > div >
    # view-publication").shadow_root print("First shadow root gotten") inner_shadow = shadow_root.find_element(
    # By.CSS_SELECTOR, "div > book-cover > book-navigation").shadow_root print("Second shadow root gotten")
    # inner_inner_shadow = inner_shadow.find_element(By.CSS_SELECTOR, "nav > read-mode").shadow_root print("Third
    # shadow root gotten")
    #


if __name__ == '__main__':
    print("Start of program")
    shadow_sequences = [
        "body > epaper-application > div > view-publication",
        "div > book-cover > book-navigation",
        "nav > read-mode"
    ]

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

    # Getting in shadow root
    edge_driver = GetShadowRoot(edge_driver, shadow_sequences)

    # Read Mode
    ReadMode(edge_driver)

    # Quit Driver
    QuitDriver(edge_driver)
    print("End of program")
