# Importation for Selenium with Edge
import datetime
import json
import mmap
import os
import shutil
import time
import urllib.request
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC  # noqa: F401
from selenium.webdriver.support.ui import WebDriverWait


def delete_images(config_file):
    with open(config_file, 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)

    image_dir = config["directories"]["image_dirLE"]

    for filename in os.listdir(image_dir):
        if filename.endswith('.jpeg'):
            os.remove(os.path.join(image_dir, filename))


def convert_images_to_pdf(config, pdf_file_name):
    with open(config, 'r', encoding='utf-8') as config_info:
        print("Getting directories...")
        config = json.load(config_info)

    image_dir = config["directories"]["image_dirLE"]
    pdf_dir = config["directories"]["pdf_dir"]

    delete_unwanted_images(image_dir)
    assembled_images = assemble_images(image_dir)

    if assembled_images:
        pdf_path = os.path.join(pdf_dir, pdf_file_name)
        assembled_images[0].save(pdf_path, "PDF", save_all=True, append_images=assembled_images[1:])
    else:
        print("Aucune image à convertir en PDF.")


def assemble_images(image_dir):
    image_files = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpeg')])
    assembled_images = []

    for i in range(0, len(image_files), 6):
        images_to_assemble = image_files[i:i + 6]
        if len(images_to_assemble) < 6:
            break

        images = [Image.open(img) for img in images_to_assemble]
        widths, heights = zip(*(i.size for i in images))

        new_im = Image.new('RGB', (1372, 2048))

        y_offset = 0
        for j, im in enumerate(images):
            if j == 3:  # Start of the right column
                y_offset = 0
            x_offset = 0 if j < 3 else max(widths)
            new_im.paste(im, (x_offset, y_offset))
            y_offset += im.size[1]

        assembled_images.append(new_im)

    return assembled_images


def delete_unwanted_images(image_dir):
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpeg'):
            page_number = int(filename.split('-')[1].split('.')[0])
            if page_number % 7 == 0:
                os.remove(os.path.join(image_dir, filename))


def multi_click(driver, page, urls_traitees, config, pdf_file_name):
    print("Starting pages processing")
    click_count = 0
    while True:
        if click_count % 3 == 0:  # Exécute milibris tous les 3 clics
            page = MilibrisFunction(driver, page, urls_traitees, config)

        if not NextPages(webDriver):
            page = MilibrisFunction(driver, page, urls_traitees,
                                    config)  # Exécute milibris une dernière fois après le dernier clic
            print("Fin des pages ou erreur")
            print("Nombre de pages: ", click_count * 2)
            print("Nombre de d'imagesLE: ", page)
            break

        click_count += 1

    # Convert imagesLE to PDF
    print("Starting conversion to PDF")
    convert_images_to_pdf(config_file, pdf_file_name)
    print("Conversion to PDF done")
    delete_images(config_file)


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
            url = str(bytes_array, 'utf-8')
            image_urls.append(url)
            start = mm.find(pattern_start, end)
        mm.close()
    return image_urls


def download_images(image_urls, image_dir, page, urls_traitees):
    for url in image_urls:
        getpager(url, image_dir, page, urls_traitees)
        page += 1
    return page


def read_html_and_download_images(html_file_path, image_dir, page, urls_traitees):
    image_urls = extract_image_urls(html_file_path)
    page = download_images(image_urls, image_dir, page, urls_traitees)
    return page


def MilibrisFunction(driver, page, urls_traitees, config):
    with open(config, 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)

    html_file_path = config["directories"]["html_file_path"]
    html_file_path = GetHtml(driver, html_file_path)
    image_dir = config["directories"]["image_dirLE"]
    pdf_dir = config["directories"]["pdf_dir"]

    create_directory(image_dir)
    create_directory(pdf_dir)

    page = read_html_and_download_images(html_file_path, image_dir, page, urls_traitees)
    return page


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
        print("Error clicking next page or end of pages !")
        return False  # Fin des pages ou erreur


def GetCredentials(site_name, login_config):
    try:
        with open(login_config, 'r', encoding='utf-8') as login_file:
            print("Getting credentials...")
            config = json.load(login_file)

        email = str(config["credentials"][site_name]["email"])
        password = str(config["credentials"][site_name]["password"])
        print("Credentials gotten")
        return email, password
    except Exception as e:
        print("Error getting credentials: ", e)
        return None, None


def GetHtml(driver, html_file_path):
    """
    This function saves the html of the current page to the file path specified in config.json
    """
    # Étape 3: Écrire le contenu HTML dans le fichier spécifié
    html_content = driver.page_source
    print("HTML gotten")
    with open(html_file_path, 'w', encoding='utf-8') as file:
        print("File opened and writing in it")
        file.write(html_content)
    print("File written")
    time.sleep(0.5)
    return html_file_path


def SignIn(driver):
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
        print("Opening newspaper...")
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


    <input autocomplete="current-password" name="password" required="" type="password" class="sc-14kwckt-28
    sc-ywv8p0-0 sc-166k8it-1 wwuyu jCZKki FyFvw" value="">
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

    <input autocomplete="email" autofocus="" name="email" required="" type="email" class="sc-14kwckt-28 sc-ywv8p0-0
    sc-166k8it-1 wwuyu jCZKki cQRcWN" value="">
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

    <button id="didomi-notice-agree-button" class="didomi-components-button didomi-button didomi-dismiss-button
    didomi-components-button--color didomi-button-highlight highlight-button" aria-label="Accepter &amp; Fermer:
    Accepter notre traitement des données et fermer" style="color: rgb(255, 255, 255); background_path-color: rgb(215, 29,
    23); border-radius: 20px; border-color: rgba(33, 33, 33, 0.3); border-width: 0px; display: block
    !important;"><span>Accepter</span></button>
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


def InitializedDriver(browser_name):
    # Try and except to handle error
    try:
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        elif browser_name.lower() == 'edge':
            options = EdgeOptions()
            options.use_chromium = True
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError("Unsupported browser")

        driver.maximize_window()
        print("Driver Initialized")
        return driver

    except Exception as e:
        print("Error: ", e)
        return


def GetURL(config_file, site_name):
    """
    This function get the URL from the config file

    "url": {
        "lopinion": "https://www.lopinion.fr/",
        "lesechos": "https://www.lesechos.fr/liseuse/LEC"
    },

    :param config_file:
    :param site_name:
    :return url:
    """
    try:
        with open(config_file, 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)

        url = str(config["url"][site_name])
        print("URL gotten:", url)
        return url
    except Exception as e:
        print("Error getting URL: ", e)
        return None


if __name__ == '__main__':
    print("Start of the program")

    webDriver = InitializedDriver('firefox')

    config_file = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\config\config.json"
    pdf_file_name = "JournalLesEchos" + get_date_today() + ".pdf"
    page = 0
    urls_done = set()

    # Open website
    URL = GetURL(config_file, "lesechos")
    open_website(webDriver, URL)

    # Accept cookies
    AcceptCookies(webDriver)

    # Get login
    email, password = GetCredentials('lesechos', config_file)

    # Login
    Login(webDriver, email, password)

    # Uncheck remember me
    Uncheck_Remember_Me(webDriver)

    # Sign in
    SignIn(webDriver)

    # Processing pages
    multi_click(webDriver, page, urls_done, config_file, pdf_file_name)

    # Close driver
    webDriver.close()

    print("End of the program")
