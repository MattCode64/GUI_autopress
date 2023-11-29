import time
import os
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from utils.config_utils import get_json_file
from utils.autoui_utils import *


def click(driver):
    try:
        driver.click()

    except WebDriverException:
        print("WebDriverException while clicking")
        return False

    except Exception as e:
        print("Error while clicking: ", e)
        return False
    else:
        print("\033[31m" + "~~~~ CLICK ~~~~" + "\033[0m")


def wait_for_element(*args):
    try:
        driver = args[0]
        if "CSS_SELECTOR" in args:
            CSS_SELECTOR = args[args.index("CSS_SELECTOR") + 1]
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))

        elif "XPATH" in args:
            XPATH = args[args.index("XPATH") + 1]
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATH)))

        else:
            raise ValueError("Selector type not specified")

        print("Element found. Waiting...")
        time.sleep(.2)
        return element

    except TimeoutException:
        print("Element not found (TimeoutException)")
        return None

    except Exception as e:
        print("Error while waiting for element: ", e)
        return None


def is_element_present(*args):
    try:
        if "CSS_SELECTOR" in args:
            CSS_SELECTOR = args[args.index("CSS_SELECTOR") + 1]
            driver = args[0]

            element = wait_for_element(driver, "CSS_SELECTOR", CSS_SELECTOR)
            if element is None:
                print("Element not present")
                return False

            else:
                print("Element present")
                return True

        elif "XPATH" in args:
            # Search for the XPATH value
            XPATH = args[args.index("XPATH") + 1]
            driver = args[0]
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH)))
            if element is None:
                print("Element not present")
                return False

            else:
                print("Element present")
                return True

    except Exception as e:
        print("Error while checking if element is present: ", e)
        return False


def click_on_next_page_button(driver, web_name):
    try:
        # CSS_NEXT_PAGE_BUTTON = get_json_file(web_name)["next_page_button"]["CSS_SELECTOR"]
        XPATH_NEXT_PAGE_BUTTON = get_json_file(web_name)["next_page_button"]["full_XPATH"]

        if is_element_present(driver, "XPATH", XPATH_NEXT_PAGE_BUTTON):
            next_page_button = wait_for_element(driver, "XPATH", XPATH_NEXT_PAGE_BUTTON)
            print("Next page button found")
            if click(next_page_button) is False:
                print("No more pages")
                return False

            else:
                print("Clicked on next page button")
                return True

        else:
            print("Next page button not found")
            return False

    except TimeoutException:
        print("Next page button not found (TimeoutException)")
        return False

    except Exception as e:
        print("Error while clicking on next page button: ", e)
        return False


def click_on_more_options_button(driver, web_name):
    try:
        XPATH_MORE_OPTIONS_BUTTON = get_json_file(web_name)["more_options"]["full_XPATH"]

        more_options_button = wait_for_element(driver, "XPATH", XPATH_MORE_OPTIONS_BUTTON)
        print("More options button found")

        click(more_options_button)
        print("Clicked on more options button")
        time.sleep(0.5)

    except TimeoutException:
        print("More options button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on more options button: ", e)
        return


def click_on_print_button(driver, web_name):
    try:
        XPATH_PRINT_BUTTON = get_json_file(web_name)["print_button"]["full_XPATH"]

        print_button = wait_for_element(driver, "XPATH", XPATH_PRINT_BUTTON)
        print("Print button found")

        if print_button:
            click(print_button)
            print("Clicked on print button")

        else:
            print("Print button is None")
            # End
            quit()

        time.sleep(0.5)

    except TimeoutException:
        print("More options button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on more options button: ", e)
        return


def click_on_read_newspaper(driver, web_name):
    try:
        XPATH_READ_NEWSPAPER = get_json_file(web_name)["read"]["full_XPATH"]

        read_newspaper = wait_for_element(driver, "XPATH", XPATH_READ_NEWSPAPER)
        print("Read newspaper found")

        click(read_newspaper)
        print("Clicked on read newspaper")
        time.sleep(0.5)

    except TimeoutException:
        print("Read newspaper not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on read newspaper: ", e)
        return


def click_on_login_button(driver, web_name):
    try:
        XPATH_LOGIN_BUTTON = get_json_file(web_name)["login"]["full_XPATH"]

        login_button = wait_for_element(driver, "XPATH", XPATH_LOGIN_BUTTON)
        print("Login button found")

        click(login_button)
        print("Clicked on login button")
        time.sleep(0.5)

    except TimeoutException:
        print("Login button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on login button: ", e)
        return


def click_on_keep_me_logged_in(driver, web_name):
    try:
        XPATH_KEEP_ME_LOGGED_IN = get_json_file(web_name)["keep_logged_in"]["full_XPATH"]

        keep_me_logged_in = wait_for_element(driver, "XPATH", XPATH_KEEP_ME_LOGGED_IN)
        print("Keep me logged in found")

        click(keep_me_logged_in)
        print("Clicked on keep me logged in (Unchecked)")
        time.sleep(.5)

    except TimeoutException:
        print("Keep me logged in not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on keep me logged in: ", e)
        return


def input_email_password(driver, web_name):
    try:
        XPATH_EMAIL = get_json_file(web_name)["email"]["full_XPATH"]
        XPATH_PASSWORD = get_json_file(web_name)["password"]["full_XPATH"]

        email_field = wait_for_element(driver, "XPATH", XPATH_EMAIL)
        print("Email field found")
        time.sleep(0.2)

        password_field = wait_for_element(driver, "XPATH", XPATH_PASSWORD)
        print("Password field found")
        time.sleep(0.2)

        # Wait for email and password field
        # email_field, password_field = wait_email_password(driver)

        # Get email and password
        email, password = get_email_password(web_name)

        # Input email and password
        input_text(email_field, email)
        print("Email inputted")
        input_text(password_field, password)
        print("Password inputted")

        print("~~~ Email and password inputted ~~~")

    except Exception as e:
        print("Error while inputting email and password: ", e)
        return


def input_text(driver, text):
    try:
        driver.send_keys(text)
        # Add color to the
        print("\033[31m" + "~~~~ INPUT TEXT ~~~~" + "\033[0m")

    except WebDriverException:
        print("Error of WebDriverException while inputting text")
        return

    except Exception as e:
        print("Error while inputting text: ", e)
        return


def get_email_password(web_name):
    try:
        web_name = web_name.upper()
        email_env = f"{web_name}_EMAIL"
        password_env = f"{web_name}_PASSWORD"
        load_dotenv()
        email = os.getenv(email_env)
        password = os.getenv(password_env)

        if email and password:
            print(f"Email and password of {web_name} gotten and are not empty")
            return email, password

        else:
            print("Email and password are empty")
            return

    except Exception as e:
        print("Error while getting email and password: ", e)
        return


def clik_on_se_connecter_button(driver, web_name):
    try:
        XPATH_SE_CONNECTER_BUTTON = get_json_file(web_name)["se_connecter_button"]["full_XPATH"]

        se_connecter_button = wait_for_element(driver, "XPATH", XPATH_SE_CONNECTER_BUTTON)
        print("Se connecter button found")

        click(se_connecter_button)
        print("Clicked on se connecter button")
        time.sleep(0.5)

    except TimeoutException:
        print("Se connecter button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on se connecter button: ", e)
        return


def click_on_cookies_popup(driver, web_name):
    try:
        XPATH_COOKIES_POPUP = get_json_file(web_name)["cookies_button"]["full_XPATH"]

        cookies = wait_for_element(driver, "XPATH", XPATH_COOKIES_POPUP)
        print("Cookies popup found")
        click(cookies)
        print("Clicked on cookies popup")
        time.sleep(0.5)

    except TimeoutException:
        print("Cookies popup not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on cookies popup: ", e)
        return


def switch_iframe(driver, web_name, mode):
    try:
        if mode == 'iframe':
            PATH_IFRAME = get_json_file(web_name)["iframe_cookies"]["full_XPATH"]

            iframe = wait_for_element(driver, "XPATH", PATH_IFRAME)
            print("Iframe found")
            driver.switch_to.frame(iframe)

        elif mode == 'default':
            driver.switch_to.default_content()
            print("Switched to default content")

    except TimeoutException:
        print("Iframe not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while switching to iframe: ", e)
        return

    else:
        print("Switched to iframe")


def automatise_print(first_iteration, name):
    if first_iteration is True:
        time.sleep(2)
        # Tabulate 5 times
        tabulate(5, .5)

        # Enter 1 time
        enter(1, .5)

        # Down arrow 1 time
        down_arrow(1, .5)

        # Enter 1 time
        enter(1, .5)

        # Tabulate 4 times
        tabulate(4, .5)

        # Enter 1 time
        enter(1, .5)

        # Save the file
        save_file(1, name)

        # Enter 1 time
        enter(1, .5)

        # Close window
        ctrl_w(1, .5)

    else:
        time.sleep(2)
        enter(1, .5)
        save_file(1, name)
        enter(1, .5)
        ctrl_w(1, .5)


def automatise(driver, web_name, first_iteration=True):
    condition = True
    name = 0

    while condition:
        if first_iteration:
            click_on_print_button(driver, web_name)
            automatise_print(first_iteration, web_name + str(name))
            name += 1
            condition = click_on_next_page_button(driver, web_name)
            first_iteration = False

        else:
            click_on_print_button(driver, web_name)
            automatise_print(first_iteration, web_name + str(name))
            condition = click_on_next_page_button(driver, web_name)
            name += 1


def navigation(driver, web_name):
    print("\033[33m" + "### Navigation ### " + "\033[0m")

    if web_name == 'lacroix':
        click_on_cookies_popup(driver, web_name)

        # Click on se connecter button
        clik_on_se_connecter_button(driver, web_name)

        # Email and password
        input_email_password(driver, web_name)

        # Click on keep me logged in
        click_on_keep_me_logged_in(driver, web_name)

        # Click on login button
        click_on_login_button(driver, web_name)

        # Click on read newspaper
        click_on_read_newspaper(driver, web_name)

        # Click on more options button
        click_on_more_options_button(driver, web_name)

        # While there is a next page button, click on it
        automatise(driver, web_name)

    elif web_name == 'liberation':
        # Switch iframe
        switch_iframe(driver, web_name, mode='iframe')

        # Click on cookies popup
        click_on_cookies_popup(driver, web_name)

        # Switch iframe
        switch_iframe(driver, web_name, mode='default')

        # Click on se connecter button
        clik_on_se_connecter_button(driver, web_name)

        # Email and password
        input_email_password(driver, web_name)

        # Click on keep me logged in
        click_on_keep_me_logged_in(driver, web_name)

        # Click on login button
        click_on_login_button(driver, web_name)

        # Click on read newspaper
        click_on_read_newspaper(driver, web_name)

        # Click on more options button
        click_on_more_options_button(driver, web_name)

        # While there is a next page button, click on it
        automatise(driver, web_name)

    # End
    time.sleep(10)
