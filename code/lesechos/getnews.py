# Importation for Selenium with Edge
import datetime
import mmap
import os
import shutil
import time
import urllib.request

import img2pdf  # python3-img2pdf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC  # noqa: F401
from selenium.webdriver.support.ui import WebDriverWait


def multi_click(driver, page, urls_traitees):
    click_count = 0
    while True:
        if click_count % 3 == 0:  # Exécute milibris tous les 3 clics
            milibris(driver, page, urls_traitees)

        if not NextPages(edge_driver):
            milibris(driver, page, urls_traitees)  # Exécute milibris une dernière fois après le dernier clic
            break

        click_count += 1


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def getpager(url, subdir, page, urls_traitees):
    if url in urls_traitees:
        print("URL déjà traitée, pas besoin de télécharger à nouveau")
        return

    print(url)
    print(page)
    file_name = os.path.join(subdir, f"page-{page:03}.jpeg")
    try:
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        urls_traitees.add(url)  # Ajouter l'URL traitée au set
    except Exception as e:
        print(f"Erreur lors de l'ouverture de l'URL {url}: {e}")


def extract_image_urls(html_file_path):
    image_urls = []
    with open(html_file_path, 'r') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        pattern_start = b'background-image: url(&quot;'
        pattern_start_sz = len(pattern_start)
        pattern_end = b'&quot;'

        start = mm.find(pattern_start, 0)
        while start != -1:
            start = start + pattern_start_sz
            end = mm.find(pattern_end, start)
            bytes_array = mm[start:end]
            url = 'https://' + str(bytes_array, 'utf-8')
            image_urls.append(url)
            start = mm.find(pattern_start, end)
        mm.close()
    return image_urls


def download_images(image_urls, image_dir, page, urls_traitees):
    for url in image_urls:
        getpager(url, image_dir, page, urls_traitees)
        page += 1


def read_html_and_download_images(html_file_path, image_dir, page, urls_traitees):
    image_urls = extract_image_urls(html_file_path)
    download_images(image_urls, image_dir, page, urls_traitees)


def convert_images_to_pdf(image_dir, pdf_dir, pdf_file_name):
    image_files = [os.path.join(image_dir, i) for i in sorted(os.listdir(image_dir)) if i.endswith('.jpeg')]
    if image_files:
        with open(os.path.join(pdf_dir, pdf_file_name), "wb") as f:
            f.write(img2pdf.convert(image_files))
    else:
        print("Aucune image au format JPEG à convertir en PDF.")


def milibris(driver, page, urls_traitees):
    html_content = driver.page_source
    html_file_path = r'C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\html\page.html'
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    image_dir = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\images"
    pdf_dir = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\pdf"
    create_directory(image_dir)
    create_directory(pdf_dir)

    read_html_and_download_images(html_file_path, image_dir, page, urls_traitees)

    pdf_file_name = "pdfjournaltest.pdf"
    convert_images_to_pdf(image_dir, pdf_dir, pdf_file_name)


def NextPages(driver):
    """
    This function click on the next page button until the last page

    next page HTML (where to click):
    //*[@id="app"]/main/div


    :param driver:
    :return:
    """
    try:
        next_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/main/div/div[2]/div[2]/div[3]"))
        )
        next_page.click()
        print("Next page clicked")
        time.sleep(4)
        return True  # Continue à cliquer

    except Exception as e:
        print("Error clicking next page or end of pages: ", e)
        return False  # Fin des pages ou erreur


def GetCredentials(file_path, site_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if site_name in line and 'email' in line:
                email = line.split(': ')[1].strip()
                password = lines[i + 1].split(': ')[1].strip()
                return email, password
    return None, None


def GetHtml(driver):
    """
    This function saves the html of the current page to a file
    """
    try:
        html = driver.page_source
        print("HTML gotten")

        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(html)
        print("File written")

    except Exception as e:
        print("Error getting HTML: ", e)


def Sign_In(driver):
    """
    This function click on the sign-in button

    sign in HTML:

    <button type="submit" class="sc-14kwckt-16 sc-16o6ckw-0 WiTvs fIpTkV sc-phxcqa-2 gGcvmy">Se connecter</button>
    """
    try:
        sign_in = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".sc-14kwckt-16.sc-16o6ckw-0.WiTvs.fIpTkV.sc-phxcqa-2.gGcvmy"))
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
        time.sleep(0.5)

    except Exception as e:
        print("Error unchecking remember me: ", e)
        return


def Login(driver, email, password):
    # Enter email
    Enter_Email(driver, email)

    # Enter password
    Enter_Password(driver, password)


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
        time.sleep(0.5)

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
        time.sleep(0.5)

    except Exception as e:
        print("Error entering email: ", e)
        return


def AcceptCookies(driver):
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
        time.sleep(0.5)

    except Exception as e:
        print("Error accepting cookies: ", e)
        return


def open_website(driver, url):
    try:
        driver.get(url)
        print("Website Opened")
        time.sleep(2)

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
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
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

    URL = "https://www.lesechos.fr/liseuse/LEC"
    login_file = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\login.txt"
    page = 0
    urls_done = set()

    # Open website
    open_website(edge_driver, URL)

    # Accept cookies
    AcceptCookies(edge_driver)

    # Get login
    email, password = GetCredentials(login_file, 'lesechos')

    # Login
    Login(edge_driver, email, password)

    # Uncheck remember me
    Uncheck_Remember_Me(edge_driver)

    # Sign in
    Sign_In(edge_driver)

    # Click
    multi_click(edge_driver, page, urls_done)

    # Close driver
    edge_driver.close()

    print("End of the program")
