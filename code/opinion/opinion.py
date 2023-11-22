import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def KeepMeSignedIn(driver):
    """
    Uncheck the keep me signed in checkbox

    HTML Xpath :
    /html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[5]/span[1]/label/remember-me/checkbox/checkbox-control/input

    :param driver:
    :return:
    """
    try:
        keepMeSignedIn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[5]/span[1]/label/remember-me/checkbox/checkbox-control"))
        )
        keepMeSignedIn.click()
        print("Keep me signed in unchecked")

    except Exception as e:
        print("Error while unchecking keep me signed in: ", e)
        return


def SignIn(driver, configfile, websitename):
    """
    Sign in to the website

    HTML Xpath :
    /html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[6]/button

    :param driver:
    :param configfile:
    :param websitename:
    :return:
    """
    try:
        email, password = GetEmailAndPassword(configfile, websitename)
        InputEmailAndPassword(driver, email, password)
        KeepMeSignedIn(driver)

        signInButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-main/app-widget/screen-layout/main/current"
                                                      "-screen/div/screen-login/p[6]/button"))
        )
        signInButton.click()
        time.sleep(5)
        print("Signed in")

    except Exception as e:
        print("Error while signing in: ", e)
        return


def InputPassword(driver, password):
    """
    Input the password in the website

    HTML Xpath :
    /html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[4]/input

    :param driver:
    :param password:
    :return:
    """
    try:
        passwordInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[4]/input"))
        )
        passwordInput.send_keys(password)
        print("Password inputted")

    except Exception as e:
        print("Error while inputting password: ", e)
        return


def InputEmail(driver, email):
    """
    Input the email in the website

    HTML Xpath :
    /html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[3]/input

    :param driver:
    :param email:
    :return:
    """
    try:
        emailInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[3]/input"))
        )
        emailInput.send_keys(email)
        print("Email inputted")

    except Exception as e:
        print("Error while inputting email: ", e)
        return


def InputEmailAndPassword(driver, email, password):
    """
    Input the email and password in the website

    HTML Xpath :

    Email : /html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[3]/input

    Password : /html/body/app-main/app-widget/screen-layout/main/current-screen/div/screen-login/p[4]/input

    :param driver:
    :param email:
    :param password:
    :return:
    """
    try:
        InputEmail(driver, email)
        InputPassword(driver, password)
        print("Email and password inputted")

    except Exception as e:
        print("Error while inputting email and password: ", e)
        return


def GetEmailAndPassword(configfile, websitename):
    """
    Get the email and password from the config file
    :param websitename:
    :param configfile:
    :return email:
    :return password:
    """
    try:
        with open(configfile, "r") as f:
            configJson = json.load(f)

        email = str(configJson["credentials"][websitename]["email"])
        password = str(configJson["credentials"][websitename]["password"])
        print("Email and password of " + websitename + " gotten")
        return email, password

    except Exception as e:
        print("Error while getting email and password from config file: ", e)
        return


def SwitchIframe(driver):
    """
    Switch to the iframe

    HTML Xpath :
    /html/body/div[3]/div[3]/div/bsp-piano-container/div[1]/div/div/iframe

    :param driver:
    :return:
    """
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div[3]/div/bsp-piano-container/div[1]/div/div/iframe"))
        )
        driver.switch_to.frame(iframe)
        print("Switched to iframe")

    except Exception as e:
        print("Error while switching to iframe: ", e)
        return


def AcceptCookies(driver):
    """
    Accept cookies from the website

    HTML Xpath :
    /html/body/div[1]/div/div/div/div/div/div[3]/button[2]
    :param driver:
    :return:
    """
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[3]/button[2]"))

        )
        cookies.click()
        print("Cookies accepted")
        # Wait for 5 seconds
        driver.implicitly_wait(5)

    except Exception as e:
        print("Error while accepting cookies: ", e)
        return


def GetURL(configfile, websitename):
    """
    Get the URL from the config file
    :param configfile:
    :param websitename:
    """
    try:
        with open(configfile, "r") as f:
            configJson = json.load(f)

        print("URL of " + websitename + " gotten")
        return str(configJson["url"][websitename])

    except Exception as e:
        print("Error while getting URL from config file: ", e)
        return


def OpenWebsite(driver, config_file, website_name):
    """
    Open the website from the config file

    :param driver:
    :param config_file:
    :param website_name:
    :return:
    """
    try:
        URL = GetURL(config_file, website_name)
        driver.get(URL)
        print("Website opened")

    except Exception as e:
        print("Error while opening website: ", e)
        return


def QuitDriver(driver):
    """
    Quit the driver

    :param driver:
    :return:
    """
    try:
        # If driver is driver type, quit
        if isinstance(driver, webdriver.Edge):
            driver.quit()
            print("Driver quit")

        # Else, return
        else:
            print("Driver is not webdriver.Edge type, maybe shadow root.")
            return

    except Exception as e:
        print("Error while quitting driver: ", e)
        return


def SetupDriver(browser_name):
    try:
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument("--window-size=1080,1920")
            driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            options.add_argument("--window-size=1080,1920")
            driver = webdriver.Firefox(options=options)
        elif browser_name.lower() == 'edge':
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("--window-size=1080,1920")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError("Unsupported browser")

        print("Driver Initialized")
        return driver

    except Exception as e:
        print("Error while setup webdriver: ", e)
        return
