import os
import re
import datetime
import platform
from utils.config_utils import get_json_file, write_json_file
from PyPDF2 import PdfMerger


def delete_pdf_files(path, files_name):
    """
    Delete the pdf files depending on the names in the list files_name

    :param path:
    :param files_name:
    :return:
    """
    try:
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
    # open the config file with get_json_file() function
    config = get_json_file("config")

    # Change the download path in the config file
    if config['directories']['download_dir'] != default_download_path:
        config['directories']['download_dir'] = default_download_path
        write_json_file(config)
        print("Download path changed")

    else:
        print("Download path already changed")


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
    :return:
    """
    # Get the default download path
    default_download_path = get_download_path_from_system()
    print(default_download_path)

    # Change the download path
    change_download_path(default_download_path)

    # Get new Json
    config = get_json_file("directories")

    # Return the new download path
    path = config['download_dir']
    print(path)
    print(type(path))
    return path
    # try:
    #
    #
    # except Exception as e:
    #     print(f"Error in change_download_path: {e}")


def extract_number(filename):
    match = re.search(r"lacroix(\d{1,2}) \d{4}-\d{2}-\d{2}\.pdf", filename)
    if match:
        return int(match.group(1))
    return 0  # Retourner 0 si aucun nombre n'est trouvé (ou pour les noms de fichiers ne correspondant pas au modèle)


def merge_pdf(output_name):
    """
    Function to merge the pdf files
    :param output_name:
    :return:
    """
    print("Hello from merge_pdf")

    if output_name == "liberation":
        print("MERGING PDF FOR LIBERATION")
        # output_name = output_name + str(datetime.date.today()) + ".pdf"
        # # Get download path
        # download_path = get_download_path()
        #
        # # Delete the pdf files
        # # delete_pdf_files(download_path, website_name=output_name, mode='before')
        #
        # # Get the pdf files
        # pdf_files = [f for f in os.listdir(download_path) if f.endswith(".pdf")]
        #
        # # Merge the pdf files
        # merger = PdfMerger()
        #
        # for pdf in pdf_files:
        #     merger.append(os.path.join(download_path, pdf))
        #
        # merger.write(os.path.join(download_path, f"JOURNAL{output_name}"))
        # merger.close()
        #
        # # Delete the pdf files
        # # delete_pdf_files(download_path, website_name=output_name, mode='after')

    elif output_name == "lefigaro":
        print("MERGING PDF FOR LEFIGARO")
        # # Get download path
        # download_path = get_download_path()
        #
        # # Delete the pdf files
        # delete_pdf_files(download_path, website_name=output_name, mode='before')
        #
        # # Get the pdf files
        # pdf_files = [f for f in os.listdir(download_path) if f.endswith(".pdf")]
        #
        # # Merge the pdf files
        # merger = PdfMerger()
        #
        # for pdf in pdf_files:
        #     merger.append(os.path.join(download_path, pdf))
        #
        # merger.write(os.path.join(download_path, f"JOURNAL{output_name}" + str(datetime.date.today()) + ".pdf"))
        # merger.close()
        #
        # # Delete the pdf files
        # delete_pdf_files(download_path, website_name=output_name, mode='after')

    elif output_name == "lacroix":
        output_name = output_name + str(datetime.date.today()) + ".pdf"

        # Get download path
        download_path = get_download_path()

        # Get the pdf files with this name "lacroixX 2023-11-11.pdf"
        pdf_files = [f for f in os.listdir(download_path) if re.match(r"lacroix\d{1,2} \d{4}-\d{2}-\d{2}\.pdf", f)]

        # Sort the pdf files by date
        pdf_files.sort(key=extract_number)

        # Merge the pdf files
        merger = PdfMerger()

        for pdf in pdf_files:
            merger.append(os.path.join(download_path, pdf))

        merger.write(os.path.join(download_path, f"JOURNAL{output_name}"))
        merger.close()

        # Delete the pdf files
        delete_pdf_files(download_path, files_name=pdf_files)

    # else:
    #     print(f"MERGING PDF FOR OTHERS MEDIA : {output_name.upper()}")
    #     # Get download path
    #     download_path = get_download_path()
    #
    #     # Get the pdf files
    #     pdf_files = [f for f in os.listdir(download_path) if f.endswith(".pdf")]
    #
    #     # Merge the pdf files
    #     merger = PdfMerger()
    #
    #     for pdf in pdf_files:
    #         merger.append(os.path.join(download_path, pdf))
    #
    #     merger.write(os.path.join(download_path, f"JOURNAL{output_name}" + str(datetime.date.today()) + ".pdf"))
    #     merger.close()
    #
    #     # Delete the pdf files
    #     delete_pdf_files(download_path, files_name=pdf_files)
