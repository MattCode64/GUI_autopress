from opinion import *


def GetShadowRoot(driver, xpathSequence):
    """
    Get the shadow root of the element

    :param driver:
    :param xpathSequence:
    :return:
    """
    try:
        current_element = driver
        for number, xpath in enumerate(xpathSequence):
            print("Getting shadow root number ", number)
            print("Current element: ", current_element)
            print("Xpath: ", xpath)
            shadow_host = WebDriverWait(current_element, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            current_element = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
            print("Shadow root gotten")

        print("Final shadow root gotten")
        return current_element

    except Exception as e:
        print("Error while getting shadow root: ", e)
        return None


def ReadMode(driver):
    """
    Function to activate the read mode on the website

    HTML Xpath:
    /html/body/epaper-application/div/view-publication//div/book-cover/book-navigation//nav/read-mode//div/button/span

    :param driver:
    :return:
    """
    try:
        readModeButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/epaper-application/div/view-publication//div/book-cover/book-navigation//nav/read-mode//div/button"))
        )
        readModeButton.click()
        print("Read mode activated")

    except Exception as e:
        print("Error while activating read mode: ", e)
        return


if __name__ == '__main__':
    print("Start of program")
    xpath_sequence = [
        "/html/body/epaper-application/div/view-publication",
        "/div/book-cover/book-navigation",
        "/nav/read-mode"
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
    shadow_root = GetShadowRoot(edge_driver, xpath_sequence)

    # Read Mode
    # ReadMode(edge_driver)

    # Quit Driver
    QuitDriver(edge_driver)
    print("End of program")
