import smtplib
from utils.manage_file_utils import get_download_path_from_system
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import datetime


def send_email_function(website_name):
    """
    TODO
    """
    # # Informations de connexion SMTP
    # smtp_server = 'smtp.gmail.com'
    # smtp_port = 587  # ou 465 pour SSL
    # smtp_user = 'freirematthieu@gmail.com'
    # smtp_password = '()'
    #
    # # Détails du mail
    # destinataire = 'freirematthieu@gmail.com'
    # sujet = 'Sujet du mail'
    # corps_message = 'Bonjour, veuillez trouver ci-joint le document.'
    #
    # # Chemin vers le fichier PDF
    # chemin_dl = get_download_path_from_system()
    # chemin_pdf = chemin_dl + "\JOURNAL" + website_name + str(datetime.date.today()) + ".pdf"
    #
    # # Création du message
    # message = MIMEMultipart()
    # message['From'] = smtp_user
    # message['To'] = destinataire
    # message['Subject'] = sujet
    # message.attach(MIMEText(corps_message, 'plain'))
    #
    # # Attachement du fichier PDF
    # with open(chemin_pdf, "rb") as fichier_pdf:
    #     part = MIMEApplication(fichier_pdf.read(), Name=basename(chemin_pdf))
    # part['Content-Disposition'] = f'attachment; filename="{basename(chemin_pdf)}"'
    # message.attach(part)
    #
    # # Connexion au serveur et envoi du mail
    # try:
    #     with smtplib.SMTP(smtp_server, smtp_port) as server:
    #         server.starttls()  # Activez cette ligne si vous utilisez TLS
    #         server.login(smtp_user, smtp_password)
    #         server.send_message(message)
    #         print("Mail envoyé avec succès.")
    # except Exception as e:
    #     print(f"Erreur lors de l'envoi du mail : {e}")
