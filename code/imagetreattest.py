from PIL import Image
from io import BytesIO
import cairosvg


def merge_images(background_path, svg_path, output_path):
    # Open the background_path image
    background = Image.open(background_path).convert("RGBA")

    # Convert SVG to PNG
    svg_png_bytes = cairosvg.svg2png(url=svg_path)

    # Convert bytes to PIL Image
    svg_image = Image.open(BytesIO(svg_png_bytes)).convert("RGBA")

    # Ensure the SVG image size matches the background_path
    svg_image = svg_image.resize(background.size, Image.ANTIALIAS)

    # Composite the images
    merged_image = Image.alpha_composite(background, svg_image)

    # Save the result
    merged_image.save(output_path)


if __name__ == '__main__':
    # Paths to files
    background_path = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\code\blob_https___journal.lopinion.fr_3b7b4dd1-692a-4fd1-aba9-54e2cc5abf60.png"
    svg_path = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\code\blob_https___journal.lopinion.fr_1220e907-9b71-419b-b1a1-34cf642d86e7.svg"
    output_path = r"C:\Data\Projet CODE\Code Python\Présidence\Travail\RP AUTO PQN\code\output.png"

    # Usage
    merge_images(background_path, svg_path, output_path)

# from PIL import Image
# import cairosvg

# # Chemins des fichiers
# background_path = (r"C:\Users\freir\Desktop\1\opi\blob_https___journal.lopinion.fr_3b7b4dd1-692a-4fd1-aba9"
#                    r"-54e2cc5abf60.png")
# svg_path = r"C:\Users\freir\Desktop\1\opi\blob_https___journal.lopinion.fr_1220e907-9b71-419b-b1a1-34cf642d86e7.svg"
#
# output_path = r"C:\Users\freir\Desktop\1\opi\output.png"
#
# # Conversion du SVG en PNG
# cairosvg.svg2png(url=svg_path, write_to='temp.png')
#
# # Ouvrir l'image de fond PNG
# background_path = Image.open(background_path)
#
# # Ouvrir l'image SVG convertie en PNG
# overlay = Image.open('temp.png')
#
# # Calculer la position pour centrer l'image SVG sur le PNG
# bg_width, bg_height = background_path.size
# overlay_width, overlay_height = overlay.size
# position = ((bg_width - overlay_width) // 2, (bg_height - overlay_height) // 2)
#
# # Fusionner les images
# background_path.paste(overlay, position, overlay)
# background_path.save(output_path)
