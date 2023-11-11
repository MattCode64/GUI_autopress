# Importation for Selenium with Edge
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa: F401
from selenium.webdriver.edge.options import Options
import datetime
import time


def accept_cookies(driver):
    """
    This function accept cookies

    cookies HTML:

    <button id="didomi-notice-agree-button" class="didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button" aria-label="Accepter &amp; Fermer: Accepter notre traitement des données et fermer" style="color: rgb(255, 255, 255); background-color: rgb(215, 29, 23); border-radius: 20px; border-color: rgba(33, 33, 33, 0.3); border-width: 0px; display: block !important;"><span>Accepter</span></button>
    """
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
        )
        cookies.click()
        print("Cookies accepted")
        time.sleep(5)

    except Exception as e:
        print("Error accepting cookies: ", e)
        return


def open_website(driver, url):
    try:
        driver.get(url)
        print("Website Opened")
        time.sleep(5)

    except Exception as e:
        print("Error opening website: ", e)
        return


# Function to get date of today (format: YYYYMMDD)
def get_date_today():
    date_today = datetime.date.today()
    date_today = date_today.strftime("%Y%m%d")
    return date_today


def InitializedDriver():
    # Try and except to handle error
    try:
        options = Options()
        options.use_chromium = True
        options.add_argument("maximized")
        driver = webdriver.Edge(options=options)
        print("Driver Initialized")
        return driver

    except Exception as e:
        print("Error: ", e)
        return


if __name__ == '__main__':
    print("Start of the program")

    edge_driver = InitializedDriver()


    # Get date of today for URL
    # date_today = get_date_today()
    # url = r"https://www.lesechos.fr/liseuse/LEC?date=" + date_today

    url = r"https://kiosque.lesechos.fr/"


    open_website(edge_driver, url)

    # Accept cookies
    # accept_cookies(edge_driver)




