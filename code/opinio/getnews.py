# Importation for Selenium with Edge
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa: F401
from selenium.webdriver.edge.options import Options
import datetime
import time


def


def Sign_In(driver):
    """
    This function click on the sign in button

    sign in HTML:

    <button type="submit" class="sc-14kwckt-16 sc-16o6ckw-0 WiTvs fIpTkV sc-phxcqa-2 gGcvmy">Se connecter</button>
    """
    try:
        sign_in = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-14kwckt-16.sc-16o6ckw-0.WiTvs.fIpTkV.sc-phxcqa-2.gGcvmy"))
        )
        sign_in.click()
        print("Sign in clicked")
        time.sleep(5)

    except Exception as e:
        print("Error clicking sign in: ", e)
        return


def Uncheck_Remember_Me(driver):
    """
    This function uncheck the remember me checkbox

    remember me HTML:

    <input name="rememberMe" type="checkbox" class="sc-14kwckt-28 sc-1386amj-3 wwuyu bUPIKX" checked="" value="">
    """
    try:
        remember_me = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "rememberMe"))
        )
        remember_me.click()
        print("Remember me unchecked")
        time.sleep(5)

    except Exception as e:
        print("Error unchecking remember me: ", e)
        return


def Enter_Password(driver, password):
    """
    This function enter password in the input field

    password HTML:

    <p data-is-floating="false" class="sc-14kwckt-6 sc-166k8it-0 gNQWaV kRIHaI">Mot de passe *</p>


    <input autocomplete="current-password" name="password" required="" type="password" class="sc-14kwckt-28 sc-ywv8p0-0 sc-166k8it-1 wwuyu jCZKki FyFvw" value="">
    """
    try:
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)
        print("Password entered")
        time.sleep(5)

    except Exception as e:
        print("Error entering password: ", e)
        return


def Enter_Email(driver, email):
    """
    This function enter email address in the input field

    email HTML:

    <p data-is-floating="false" class="sc-14kwckt-6 sc-166k8it-0 gNQWaV kRIHaI">Email *</p>

    <input autocomplete="email" autofocus="" name="email" required="" type="email" class="sc-14kwckt-28 sc-ywv8p0-0 sc-166k8it-1 wwuyu jCZKki cQRcWN" value="">
    """
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys(email)
        print("Email entered")
        time.sleep(5)

    except Exception as e:
        print("Error entering email: ", e)
        return


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

    url = "https://www.lesechos.fr/liseuse/LEC?date=20231110"

    # Open website
    open_website(edge_driver, url)

    # Accept cookies
    accept_cookies(edge_driver)

    # Enter email
    email = "370ffbe9f3974bc59b2bc7cf5fece6dd5dcd84d8"
    Enter_Email(edge_driver, email)

    # Enter password
    password = "9bab54324b7897fb040d472c363a42af018e9ccd"
    Enter_Password(edge_driver, password)

    # Uncheck remember me
    Uncheck_Remember_Me(edge_driver)

    # Sign in
    Sign_In(edge_driver)

    # Close driver
    edge_driver.close()




