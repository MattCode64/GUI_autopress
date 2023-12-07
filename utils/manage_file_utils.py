import datetime
import os
import platform
import re

from PIL import Image
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter

from utils.config_utils import get_json_file, write_json_file


# function that convert png to pdf in the folder
def convert_png_to_pdf():
    directory = "../data/imagesLC/"
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
            pdf_path = image_path.replace(".png", ".pdf")
            image.convert('RGB').save(pdf_path, "PDF")


def merge_pdfs(output_name="JournalLacroix.pdf"):
    input_dir = "../data/imagesLC/"
    output_file = f"../data/imagesLC/{output_name}"

    # Obtenir une liste triée des fichiers PDF dans le dossier par nom
    pdf_files = sorted([item for item in os.listdir(input_dir) if item.endswith('.pdf')])

    pdf_writer = PdfFileWriter()

    for pdf_file in pdf_files:
        file_path = os.path.join(input_dir, pdf_file)
        pdf_reader = PdfFileReader(file_path)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_file, 'wb') as output:
        pdf_writer.write(output)


def delete_png_files():
    directory = "../data/imagesLC/"
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            os.remove(os.path.join(directory, filename))


def delete_pdf_files(path, files_name):
    """
    Delete the pdf files depending on the names in the list files_name

    :param path:
    :param files_name:
    :return:
    """
    try:
        print("Deleting pdf files...")
        for file in files_name:
            os.remove(os.path.join(path, file))

            if os.path.exists(os.path.join(path, file)):
                print(f"The file {file}" + "\033[1m" + "does not exist or has been deleted successfully" + "\033[0m")

    except FileNotFoundError:
        print("FileNotFoundError")
    except OSError:
        print("OSError")
    except Exception as e:
        print(f"Error in delete_pdf_files: {e}")


def change_download_path(default_download_path):
    """
    Change the default download path of the browser

    :param default_download_path:
    :return:
    """
    try:
        # open the config file with get_json_file() function
        config = get_json_file("config")

        # Change the download path in the config file
        if config['directories']['download_dir'] != default_download_path:
            config['directories']['download_dir'] = default_download_path
            write_json_file(config)
            print("Download path changed")

        else:
            print("Download path already changed")

    except Exception as e:
        print(f"Error in change_download_path: {e}")


def get_download_path_from_system():
    """
    Retourne le chemin d'accès par défaut du dossier de téléchargement pour le système d'exploitation de l'utilisateur.
    """
    if platform.system() == 'Windows':
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif platform.system() == 'Darwin':
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif platform.system() == 'Linux':
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        raise ValueError('Système d\'exploitation non pris en charge.')


def get_download_path():
    """
    Function to change the default download path of the browser with get_download_path() function
    :return path:
    """
    # Get the default download path
    default_download_path = get_download_path_from_system()

    # Change the download path
    change_download_path(default_download_path)

    # Get new Json
    config = get_json_file("directories")

    # Return the new download path
    path = config['download_dir']
    return path


def extract_number(filename, pattern):
    match = re.search(pattern, filename)
    if match:
        return int(match.group(1))
    return 0


def merge_pdf(web_name):
    """
    Function to merge the pdf files
    :param web_name:
    :return:
    """
    try:
        output_name = web_name + str(datetime.date.today()) + ".pdf"

        # Get download path
        download_path = get_download_path()

        # Get the pdf files with this name "lacroixX 2023-11-11.pdf"
        # pattern_web_name = fr"{web_name}\d{1, 2} \d{4}-\d{2}-\d{2}\.pdf"
        pattern_web_name = fr"{web_name}(\d{{1,2}}) \d{{4}}-\d{{2}}-\d{{2}}\.pdf"
        pdf_files = [f for f in os.listdir(download_path) if re.match(pattern_web_name, f)]

        # Sort the pdf files by date
        pdf_files.sort(key=lambda filename: extract_number(filename, pattern_web_name))

        # Merge the pdf files
        merger = PdfMerger()

        for pdf in pdf_files:
            merger.append(os.path.join(download_path, pdf))

        merger.write(os.path.join(download_path, f"JOURNAL{output_name}"))
        merger.close()

        # Delete the pdf files
        delete_pdf_files(download_path, files_name=pdf_files)

    except FileNotFoundError:
        print("FileNotFoundError")
    except OSError:
        print("OSError")
    except Exception as e:
        print(f"Error in merge_pdf: {e}")
