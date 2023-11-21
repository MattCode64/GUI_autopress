import os
import json
import datetime
import img2pdf


def Conversion(config_file):
    """
    Function to convert images to pdf and delete images

    :param config_file:
    :return:
    """
    try:
        # Convert images to pdf
        ConvertImagesToPdf(config_file)

        # Delete images
        # DeleteImages(config_file)

    except Exception as e:
        print("Error while converting images to pdf: ", e)
        return


def DeleteImages(config_file):
    """
    Delete all the images in the folder

    :param config_file:
    :return:
    """
    try:
        # Open JSON file for "image_dirOPI"
        with open(config_file, "r", encoding='utf-8') as f:
            configJson = json.load(f)

        # Get the path of the folder
        path = configJson["directories"]["image_dirOPI"]

        # Get every path of the images in the folder
        images = [os.path.join(path, fn) for fn in os.listdir(path)]

        # Delete all the images
        for image in images:
            os.remove(image)

        print("Images deleted")

    except Exception as e:
        print("Error while deleting images: ", e)
        return


def ConvertImagesToPdf(config_file):
    """
    Convert images to pdf

    :param config_file:
    :return:
    """
    try:
        # GET DD/MM/YYYY of today
        today = datetime.date.today()
        today = today.strftime("%d%m%Y")  # Format changed for file naming

        # Open JSON file for "image_dirOPI"
        with open(config_file, "r", encoding='utf-8') as f:
            configJson = json.load(f)

        # Get the path of the folder
        path = configJson["directories"]["image_dirOPI"]

        # Get the path of the output file will be saved
        output_path = configJson["directories"]["pdf_dir"]
        output_file = os.path.join(output_path, f"JournalOPINION{today}.pdf")  # Nom de fichier PDF basé sur la date

        # Get every path of the images in the folder
        images = [os.path.join(path, fn) for fn in os.listdir(path) if fn.endswith('.png')]  # Filtrer pour les images

        if images:
            print(images)

            # Convert images to pdf
            with open(output_file, "wb") as f:
                f.write(img2pdf.convert(images))

            print("PDF created at", output_file)

    except Exception as e:
        print("An error occurred:", e)
