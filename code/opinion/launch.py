from opinion import *
from navigation import *
from pdfconvert import *


def main():
    print("Start of program")
    config = "../../data/config/config.json"

    # Setup Driver
    edge_driver = SetupDriver('chrome')

    # Open Website
    OpenWebsite(edge_driver, config, "lopinion")

    # Accept Cookies
    AcceptCookies(edge_driver)

    # Switch to iframe
    SwitchIframe(edge_driver)

    # Sign In
    SignIn(edge_driver, config, "lopinion")

    # Read Mode
    # ReadMode(edge_driver, config)
    # time.sleep(5000)

    # Processing
    Processing(edge_driver, config)

    # Convert PDF
    Conversion(config)

    QuitDriver(edge_driver)
    print("End of program")


if __name__ == '__main__':
    main()
