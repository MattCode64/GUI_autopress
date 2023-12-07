import os
import string
import time

from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.autoui_utils import *
from utils.config_utils import get_json_file
from utils.manage_file_utils import merge_pdf, merge_pdfs, convert_png_to_pdf


def click(driver):
    """
    Function to click on an element

    :param driver:
    :return:
    """
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
    """
    Function to wait for an element to be present depending on the selector type

    :param args:
    :return element: if element is found
    """
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

        # print("Element found. Waiting...")
        time.sleep(.2)
        return element

    except TimeoutException:
        print("Element not found (TimeoutException)")
        return None

    except Exception as e:
        print("Error while waiting for element: ", e)
        return None


def is_element_present(*args):
    """
    Function to check if an element is present depending on the selector type

    :param args:
    :return bool:
    """
    try:
        if "CSS_SELECTOR" in args:
            CSS_SELECTOR = args[args.index("CSS_SELECTOR") + 1]
            driver = args[0]

            element = wait_for_element(driver, "CSS_SELECTOR", CSS_SELECTOR)
            if element is None:
                print("Element not present")
                return False

            else:
                # print("Element present")
                return True

        elif "XPATH" in args:
            XPATH = args[args.index("XPATH") + 1]
            driver = args[0]
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH)))
            if element is None:
                print("Element not present")
                return False

            else:
                # print("Element present")
                return True

    except Exception as e:
        print("Error while checking if element is present: ", e)
        return False


def click_on_next_page_button(driver, web_name):
    """
    Function to click on the next page button

    :param driver:
    :param web_name:
    :return bool:
    """
    try:
        # CSS_NEXT_PAGE_BUTTON = get_json_file(web_name)["next_page_button"]["CSS_SELECTOR"]
        XPATH_NEXT_PAGE_BUTTON = get_json_file(web_name)["next_page_button"]["full_XPATH"]

        if is_element_present(driver, "XPATH", XPATH_NEXT_PAGE_BUTTON):
            next_page_button = wait_for_element(driver, "XPATH", XPATH_NEXT_PAGE_BUTTON)
            # print("Next page button found")
            if click(next_page_button) is False:
                # print("No more pages")
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
        print("NO more PAGES or Error while clicking on next page button: ", e)
        return False


def click_on_more_options_button(driver, web_name):
    """
    Function to click on the more options button

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_MORE_OPTIONS_BUTTON = get_json_file(web_name)["more_options"]["full_XPATH"]

        more_options_button = wait_for_element(driver, "XPATH", XPATH_MORE_OPTIONS_BUTTON)
        # print("More options button found")

        click(more_options_button)
        # print("Clicked on more options button")
        time.sleep(0.5)

    except TimeoutException:
        print("More options button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on more options button: ", e)
        return


def click_on_print_button(driver, web_name):
    """
    Function to click on the print button

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_PRINT_BUTTON = get_json_file(web_name)["print_button"]["full_XPATH"]

        print_button = wait_for_element(driver, "XPATH", XPATH_PRINT_BUTTON)
        # print("Print button found")

        if print_button:
            click(print_button)
            # print("Clicked on print button")

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
    """
    Function to click on the read newspaper button

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_READ_NEWSPAPER = get_json_file(web_name)["read"]["full_XPATH"]

        read_newspaper = wait_for_element(driver, "XPATH", XPATH_READ_NEWSPAPER)
        # print("Read newspaper found")

        click(read_newspaper)
        # print("Clicked on read newspaper")
        time.sleep(0.5)

    except TimeoutException:
        print("Read newspaper not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on read newspaper: ", e)
        return


def click_on_login_button(driver, web_name):
    """
    Function to click on the login button

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_LOGIN_BUTTON = get_json_file(web_name)["login"]["full_XPATH"]

        login_button = wait_for_element(driver, "XPATH", XPATH_LOGIN_BUTTON)
        # print("Login button found")

        click(login_button)
        # print("Clicked on login button")
        time.sleep(0.5)

    except TimeoutException:
        print("Login button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on login button: ", e)
        return


def click_on_keep_me_logged_in(driver, web_name):
    """
    Function to click on the keep me logged in button

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_KEEP_ME_LOGGED_IN = get_json_file(web_name)["keep_logged_in"]["full_XPATH"]

        keep_me_logged_in = wait_for_element(driver, "XPATH", XPATH_KEEP_ME_LOGGED_IN)
        # print("Keep me logged in found")

        click(keep_me_logged_in)
        # print("Clicked on keep me logged in (Unchecked)")
        time.sleep(.5)

    except TimeoutException:
        print("Keep me logged in not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on keep me logged in: ", e)
        return


def input_email_password(driver, web_name):
    """
    Function to input email and password

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_EMAIL = get_json_file(web_name)["email"]["full_XPATH"]
        XPATH_PASSWORD = get_json_file(web_name)["password"]["full_XPATH"]

        email_field = wait_for_element(driver, "XPATH", XPATH_EMAIL)
        # print("Email field found")
        time.sleep(0.2)

        password_field = wait_for_element(driver, "XPATH", XPATH_PASSWORD)
        # print("Password field found")
        time.sleep(0.2)

        # Wait for email and password field
        # email_field, password_field = wait_email_password(driver)

        # Get email and password
        email, password = get_email_password(web_name)

        # Input email and password
        input_text(email_field, email)
        # print("Email inputted")
        input_text(password_field, password)
        # print("Password inputted")

        # print("~~~ Email and password inputted ~~~")

    except Exception as e:
        print("Error while inputting email and password: ", e)
        return


def input_text(driver, text):
    """
    Function to input text

    :param driver:
    :param text:
    :return:
    """
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
    """
    Function to get email and password from the .env file

    :param web_name:
    :return:
    """
    try:
        web_name = web_name.upper()
        email_env = f"{web_name}_EMAIL"
        password_env = f"{web_name}_PASSWORD"
        load_dotenv()
        email = os.getenv(email_env)
        password = os.getenv(password_env)

        if email and password:
            # print(f"Email and password of {web_name} gotten and are not empty")
            return email, password

        else:
            print("Email and password are empty")
            return

    except Exception as e:
        print("Error while getting email and password: ", e)
        return


def clik_on_se_connecter_button(driver, web_name):
    """
    Function to click on the se connecter button

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_SE_CONNECTER_BUTTON = get_json_file(web_name)["se_connecter_button"]["full_XPATH"]

        se_connecter_button = wait_for_element(driver, "XPATH", XPATH_SE_CONNECTER_BUTTON)
        # print("Se connecter button found")

        click(se_connecter_button)
        # print("Clicked on se connecter button")
        time.sleep(0.5)

    except TimeoutException:
        print("Se connecter button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on se connecter button: ", e)
        return


def click_on_cookies_popup(driver, web_name):
    """
    Function to click on the cookies popup

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_COOKIES_POPUP = get_json_file(web_name)["cookies_button"]["full_XPATH"]

        cookies = wait_for_element(driver, "XPATH", XPATH_COOKIES_POPUP)
        # print("Cookies popup found")
        click(cookies)
        # print("Clicked on cookies popup")
        time.sleep(0.5)

    except TimeoutException:
        print("Cookies popup not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on cookies popup: ", e)
        return


def switch_iframe(driver, web_name, mode):
    """
    Function to switch iframe

    :param driver:
    :param web_name:
    :param mode:
    :return:
    """
    try:
        if mode == 'iframe':
            PATH_IFRAME = get_json_file(web_name)["iframe_cookies"]["full_XPATH"]

            iframe = wait_for_element(driver, "XPATH", PATH_IFRAME)
            # print("Iframe found")
            driver.switch_to.frame(iframe)

        elif mode == 'default':
            driver.switch_to.default_content()
            # print("Switched to default content")

    except TimeoutException:
        print("Iframe not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while switching to iframe: ", e)
        return

    else:
        print("Switched to iframe")


def automatise_print(first_iteration, name, os_system):
    """
    Function to automatise the saving of the pdf file

    :param os_system:
    :param first_iteration:
    :param name:
    :return:
    """
    # Do a switch case for windows mac and linux
    if os_system == 'windows':
        if first_iteration is True:
            time.sleep(2)
            tabulate(5, .5)
            enter(1, .5)
            alt_tab(1, .5)
            save_file(1, name)
            enter(1, .5)
            ctrl_w(1, .5, os_system)

        else:
            time.sleep(2)
            tabulate(5, .5)
            enter(1, .5)
            alt_tab(1, .5)
            save_file(1, name)
            enter(1, .5)
            ctrl_w(1, .5, os_system)
            # time.sleep(2)
            # enter(1, .5)
            # win_tab(2, 1)
            # save_file(1, name)
            # enter(1, .5)
            # ctrl_w(1, .5)

    elif os_system == 'mac':
        return

    elif os_system == 'linux':
        time.sleep(2)
        tabulate(8, .5)
        enter(1, .5)
        save_file(1, name)
        enter(1, .5)
        ctrl_w(1, .5, os_system)


def full_screen_mode(driver, web_name):
    """
    Function to put the browser in full screen mode

    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_FULL_SCREEN_BUTTON = get_json_file(web_name)["full_screen"]["full_XPATH"]

        full_screen_button = wait_for_element(driver, "XPATH", XPATH_FULL_SCREEN_BUTTON)
        # print("Full screen button found")

        click(full_screen_button)
        # print("Clicked on full screen button")
        time.sleep(0.5)

    except TimeoutException:
        print("Full screen button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on full screen button: ", e)
        return


def take_screenshot(driver, web_name, output_file_name):
    """
    Function to take a screenshot

    :param output_file_name:
    :param driver:
    :param web_name:
    :return:
    """
    try:
        XPATH_SCREENSHOT = get_json_file(web_name)["page"]["full_XPATH"]

        screenshot_page = wait_for_element(driver, "XPATH", XPATH_SCREENSHOT)

        # take screenshot with selenium in download folder
        screenshot_page.screenshot(f"../data/imagesLC/{output_file_name}.png")
        print("Screenshot taken")
        time.sleep(0.5)

    except TimeoutException:
        print("Screenshot button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on screenshot button: ", e)
        return


def automatise_print_for_lacroix(driver, web_name):
    full_screen_mode(driver, web_name)
    time.sleep(2)
    condition = True
    # list alphabet
    i_letter = 0
    alphabet = list(string.ascii_lowercase)
    # While it can change page, take screenshot
    while condition:
        time.sleep(3)
        output_file_name = f"{alphabet[i_letter]}_{web_name}"
        # Take screenshot
        take_screenshot(driver, web_name, output_file_name)
        i_letter += 1
        # Click on next page button
        condition = click_on_next_page_button(driver, web_name)
        print("Condition: ", condition)


def automatise(driver, web_name, first_iteration=True, os_system='linux'):
    """
    Function to automatise the navigation on the website

    :param os_system:
    :param driver:
    :param web_name:
    :param first_iteration:
    :return:
    """
    condition = True
    name = 0

    while condition:
        if web_name == 'liberation':
            time.sleep(4.5)
            if first_iteration:
                click_on_print_button(driver, web_name)
                automatise_print(first_iteration, web_name + str(name), os_system)
                name += 1
                condition = click_on_next_page_button(driver, web_name)
                first_iteration = False

            else:
                print("In else because not first iteration")
                # For loop to click two times on the next page button
                for i in range(2):
                    time.sleep(2)
                    print("In for loop ", i)
                    condition = click_on_next_page_button(driver, web_name)

                click_on_print_button(driver, web_name)
                name += 1


def route_lacroix(driver, web_name):
    """
    Function to navigate on the website La Croix

    :param driver:
    :param web_name:
    :return:
    """
    try:
        click_on_cookies_popup(driver, web_name)

        # Click on se connecter button
        clik_on_se_connecter_button(driver, web_name)

        # Email and password
        input_email_password(driver, web_name)

        # Click on keep me logged in
        # print("Click on keep me logged in")
        # click_on_keep_me_logged_in(driver, web_name)

        # Click on login button
        print("Click on login button")
        click_on_login_button(driver, web_name)

        # Click on read newspaper
        print("Click on read newspaper")
        click_on_read_newspaper(driver, web_name)

        # Click on more options button
        # click_on_more_options_button(driver, web_name)

        # While there is a next page button, click on it
        automatise_print_for_lacroix(driver, web_name)

        # Merge pdf
        convert_png_to_pdf()
        merge_pdfs()


    except Exception as e:
        print("Error while navigating on La Croix: ", e)
        return


def route_liberation(driver, web_name):
    """
    Function to navigate on the website Liberation

    :param driver:
    :param web_name:
    :return:
    """
    try:
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

        # Click on login button
        click_on_login_button(driver, web_name)

        # Click on read newspaper
        click_on_read_newspaper(driver, web_name)

        # Click on more options button
        click_on_more_options_button(driver, web_name)

        # While there is a next page button, click on it
        automatise(driver, web_name)

        # Merge pdf
        merge_pdf(web_name)

    except Exception as e:
        print("Error while navigating on Liberation: ", e)
        return


def navigation(driver, web_name):
    print("\033[33m" + f"### Navigation {web_name.upper()} ### " + "\033[0m")

    if web_name == 'lacroix':
        route_lacroix(driver, web_name)

    elif web_name == 'liberation':
        route_liberation(driver, web_name)

    elif web_name == 'figaro':
        time.sleep(10)
        pass

    # End
    time.sleep(10)
