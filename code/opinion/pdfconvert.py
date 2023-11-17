from navigation import *
from opinion import *
# Import libraries to convert png to pdf
from PIL import Image
import os
import glob

# Create a function that converts png to pdf and add it to the pdf
def ConvertPngToPdf(path, pdf):
    """
    Function to convert png to pdf and add it to the pdf

    :param path:
    :param pdf:
    :return:
    """
    try:
        # Create a list of png files
        png_files = glob.glob(path + "/*.png")

        # Sort the list
        png_files.sort()

        # Loop through the list
        for png_file in png_files:
            # Open the png file
            png = Image.open(png_file)

            # Convert png to pdf
            pdf.append(png)

            # Close the png file
            png.close()

        # Return the pdf
        return pdf

    except Exception as e:
        print("Error while converting png to pdf: ", e)
        return