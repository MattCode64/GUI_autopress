CREER AU PREALABLE LES DOSSIERS POUR LES IMAGES ET LES PDF


CREATE CONFIG.JSON FOR USING THIS CODE

EXEMPLE :

{
    "url": {
        "lopinion": "https://journal.lopinion.fr/",
        "lesechos": "https://www.lesechos.fr/liseuse/LEC"
    },

    "credentials": {
        "lopinion": {
            "email": "EMAIL",
            "password": "PASSWORD",
        },
        "lesechos": {
            "email": "EMAIL",
            "password": "PASSWORD"
        }
    },
    "directories": {
        "pdf_dir": "PATH TO PDF DIRECTORY",
        "image_dir": "PATH TO IMAGE DIRECTORY",
        "html_file_path": "PATH TO HTML FILE"
    },
    "shadow_root": {
        "body": "body > epaper-application > div > view-publication",
        "nav": "div > book-cover > book-navigation",
        "read_mode": "nav > read-mode"
    }
}