import unittest
import os
import tkinter as tk
import sys
import re
import pyshorteners
import pyzbar.pyzbar
import PIL.Image
import webbrowser

from tkinter import messagebox
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Qr_Code import QRCodeGeneratorApp

#vérification que l'application peut bien créer des Qr Code sans erreur
class TestURL(unittest.TestCase):
    def valid_url(self, url):
        if url :
            url_regex = re.compile(r'https?://(?:www\.)?[a-zA-Z0-9./]+')
            return bool(url_regex.match(url))
        else:
            return False
    def test_valid_url(self):
        test_url = "https://stackoverflow.com/"
        result = self.valid_url(test_url)

        if result is True :
            print(f"'{test_url}' est une URL valide")
        else :
            root = tk.Tk()
            app = QRCodeGeneratorApp(master=root)

            print(app.generate_qr_code())
            print(f"'{test_url}' n est pas une URL valide")

    def test_invalid_url(self):
        test_url2 = "file:///C:/Users/lefebvre/Desktop/VICTOR%20LEFEBVRE-CORMAO-10.pdf"
        result2 = self.valid_url(test_url2)
        if result2 is True:
            print(f"'{test_url2}' est une URL valide")
        else:
            messagebox.showwarning("Avertissement","Veuillez entrer une adresse URL Valide pour générer un QR Code.")
            print(f"'{test_url2}' n est pas une URL valide")
class UrlRework (unittest.TestCase):
    def lienURL(self):
        lien = input("Entre votre lien :")
        return lien

    @patch('builtins.input', side_effect=['https://www.google.com/search?q=faire+une+entr%C3%A9e+automatique+dans+une+fonction+python*&client=firefox-b-d&sca_esv=7746fac465ae621b&sca_upv=1&sxsrf=ADLYWIKCJaUBJD0k6CxR_UdFTFk2Ag8Aqw%3A1727359489355&ei=AWr1Zp-2FZ2RkdUP4cOVmQo&ved=0ahUKEwjfuozG4-CIAxWdSKQEHeFhJaMQ4dUDCBA&uact=5&oq=faire+une+entr%C3%A9e+automatique+dans+une+fonction+python*&gs_lp=Egxnd3Mtd2l6LXNlcnAiN2ZhaXJlIHVuZSBlbnRyw6llIGF1dG9tYXRpcXVlIGRhbnMgdW5lIGZvbmN0aW9uIHB5dGhvbioyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESLUUUABYjBJwAHgBkAEAmAFWoAGSAaoBATK4AQPIAQD4AQGYAgKgApgBmAMAkgcBMqAH7Ac&sclient=gws-wiz-serp'])
    def test_fonction_a_tester(self, mock_input):
        resultat = self.lienURL()
        type_lien = pyshorteners.Shortener()
        short_lien = type_lien.tinyurl.short(resultat)
        print(f"Le nouveau lien est : "+short_lien)

class TraductionQRCode (unittest.TestCase):

    @patch('builtins.input', side_effect=['qr_code.png'])
    def test_read_qr_code(self, mock_input):
        images = PIL.Image.open(r'qr_code.png')
        codes = pyzbar.pyzbar.decode(images)
        return codes[0].data.decode() if codes else None
    
    url = test_read_qr_code("qr_code.png")
    webbrowser.open(url) 
    

if __name__=='__main__':
    unittest.main()



