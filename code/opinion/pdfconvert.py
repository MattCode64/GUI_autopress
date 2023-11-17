from navigation import *
from opinion import *
# Import libraries to convert png to pdf
from PIL import Image
import os
import glob

if __name__ == '__main__':
    path = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\images\1.png"

    # Convert png to pdf
    image1 = Image.open(path)
    im1 = image1.convert('RGB')
    im1.save(r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\data\images\1.pdf")

    # Delete png
    os.remove(path)