from PIL import Image
from PyPDF2 import PdfMerger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa: F401
from selenium.webdriver.chrome.options import Options
import time


def get_number_of_pages(driver):
    time.sleep(5)
    pages = driver.find_element(By.CLASS_NAME, 'pages')
    return int(pages.text)


def setup(driver):
    # Mettre en plein écran
    driver.maximize_window()
    # time.sleep(2)

    # Aller sur le site
    driver.get("https://www.lopinion.fr/")

    # Si un popup des cookies apparaît, le fermer
    try:
        # Accepter les cookies
        cookies_button = driver.find_element(By.ID, 'didomi-notice-agree-button')
        cookies_button.click()
        time.sleep(1)
    except Exception as e:
        pass

    # Aller sur le journal
    try:
        journal_button = driver.find_element(By.XPATH, '//a[@href="https://www.lopinion.fr/lejournal"]')
        journal_button.click()
        print("Appui sur le bouton Journal")
        time.sleep(3)
    except Exception as e:
        print(f"Erreur lors de l'appui sur le bouton Journal: {e}")
        return

    # try:
    #     # Exécuter un script JavaScript pour cliquer sur la case à cocher
    #     checkbox_script = """
    #     var checkbox = document.querySelector(".checkbox-container checkbox-control[role='checkbox']");
    #     if (checkbox.getAttribute('aria-checked') === 'true') {
    #         checkbox.click();
    #     }
    #     """
    #     driver.execute_script(checkbox_script)
    #     time.sleep(3)
    # except Exception as e:
    #     print(f"Erreur lors de l'interaction avec la case à cocher: {e}")
    #     pass

    # Login et mot de passe
    username = "veille.presse@elysee.fr"
    password = "Presse2019!"

    # Try/except to find div with id "container"
    try:
        container = driver.find_element(By.ID, 'container')
    except Exception as e:
        print(f"Erreur lors de la recherche du conteneur: {e}")
        return

    # Try/except to find in container iframe with ID "myIframe"
    try:
        iframe = container.find_element(By.ID, 'myIframe')
    except Exception as e:
        print(f"Erreur lors de la recherche de l'iframe: {e}")
        return

    # Try/except to switch to iframe
    time.sleep(40)
    try:
        driver.switch_to.frame(iframe)
    except Exception as e:
        print(f"Erreur lors du switch vers l'iframe 1: {e}")
        return

    # Try/except to find div with class "Page-content"
    try:
        page_content = driver.find_element(By.CLASS_NAME, 'Page-content')
    except Exception as e:
        print(f"Erreur lors de la recherche du conteneur Page-content: {e}")
        return

    # Try/except to find div with id "piano-id-container"
    try:
        piano_id_container = page_content.find_element(By.CLASS_NAME, 'piano-id-container')
    except Exception as e:
        print(f"Erreur lors de la recherche du conteneur piano-id-container: {e}")
        return

    # Try/except to find in piano_id_container iframe with ID "piano-id-0pLyc"
    try:
        piano_id_iframe = piano_id_container.find_element(By.NAME, 'piano-id-0pLyc')
    except Exception as e:
        print(f"Erreur lors de la recherche de l'iframe piano-id-0pLyc: {e}")
        return

    # Try/except to switch to iframe
    try:
        driver.switch_to.frame(piano_id_iframe)
    except Exception as e:
        print(f"Erreur lors du switch vers l'iframe 2: {e}")
        return



def convert_to_pdf(image_path, page_number, pdfmerger, split=False):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f'Le fichier {image_path} n\'existe pas')
        return
    except IOError as e:
        print(f"Erreur de l'image: {e}")
        return

    try:
        if split:
            # Diviser l'image en deux si nécessaire
            width, height = image.size
            left_half = image.crop((0, 0, width // 2, height))
            right_half = image.crop((width // 2, 0, width, height))

            # Sauvegarder chaque moitié en tant que PDF
            for i, half in enumerate([left_half, right_half], start=1):
                pdf_path = f'page{page_number}_part{i}.pdf'
                half.convert('RGB').save(pdf_path)
                pdfmerger.append(pdf_path)
        else:
            # Convertir l'image entière en PDF
            pdf_path = f'page{page_number}.pdf'
            image.convert('RGB').save(pdf_path)
            pdfmerger.append(pdf_path)
    except Exception as e:
        print(f"Erreur lors de la conversion de l'image en PDF: {e}")
        return


def navigate_and_capture(driver, total_of_pages, pdf_merger):
    page_number = 1
    save_path = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data"

    while page_number <= total_of_pages:
        # Si page_number == 1
        if page_number == 1:
            time.sleep(5)
            first_page = driver.find_element(By.CSS_SELECTOR, ".page_location")
            # Capture d'écran de first_page
            screenshot_page_path = save_path + f'\Capture d\'écran page {page_number}.png'
            first_page.screenshot(screenshot_page_path)

            # Conversion de la capture d'écran en PDF
            convert_to_pdf(screenshot_page_path, page_number, pdf_merger, split=False)

        elif 1 < page_number < total_of_pages:
            time.sleep(5)
            # Cliquer sur le bouton Page suivante
            next_button = driver.find_element(By.CSS_SELECTOR, '[data-type="next"]')
            next_button.click()

            # Capture et traitement de la page
            screenshot_page_path = save_path + f'\Capture d\'écran page {page_number}.png'
            page = driver.find_element(By.CSS_SELECTOR, ".page_location")
            page.screenshot(screenshot_page_path)

            # Convertir la capture d'écran en PDF
            convert_to_pdf(screenshot_page_path, page_number, pdf_merger, split=True)

        else:
            time.sleep(5)
            # Cliquer sur le bouton Page suivante
            next_button = driver.find_element(By.CSS_SELECTOR, '[data-type="next"]')
            next_button.click()

            # Capture et traitement de la page
            screenshot_page_path = f'Capture d\'écran page {page_number}.png'
            page = driver.find_element(By.CSS_SELECTOR, ".page_location")
            page.screenshot(screenshot_page_path)

            # Convertir la capture d'écran en PDF
            convert_to_pdf(screenshot_page_path, page_number, pdf_merger, split=False)

        page_number += 1

    # Fusion des PDF
    with open("final_document.pdf", "wb") as f_out:
        pdf_merger.write(f_out)


# Function save the final PDF file
def save_pdf(pdf_merger):
    # Sauvegarder le fichier PDF final
    pdf_merger.write('journal.pdf')
    pdf_merger.close()


def close(driver):
    time.sleep(5)
    # Fermer le navigateur
    driver.quit()


if __name__ == '__main__':
    print("Début du script")
    # Initialisation
    pdf_merger = PdfMerger()
    path = r"C:\Data\PC\WebDriver\chromedriver.exe"

    # Ouvrir le navigateur
    print("Ouverture du navigateur")
    chrome_options = Options()
    chrome_options.executable_path = path
    driver = webdriver.Chrome(options=chrome_options)
    setup(driver)

    # Récupérer le nombre de pages
    print("Récupération du nombre de pages")
    total_of_pages = get_number_of_pages(driver)

    # Naviguer et capturer les pages
    print("Navigation et capture des pages")
    navigate_and_capture(driver, total_of_pages, pdf_merger)

    # Sauvegarder le fichier PDF final
    print("Sauvegarde du fichier PDF final")
    save_pdf(pdf_merger)

    # Fermer le navigateur
    print("Fermeture du navigateur")
    close(driver)
