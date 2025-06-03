import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QApplication
from ui.caesar import Ui_MainWindow
import requests

class VigenereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.encrypt_btn.clicked.connect(self.call_api_encrypt)
        self.ui.decrypt_btn.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": self.ui.plaintext_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.ciphertext_txt.setText(data["encrypted_text"])
                QMessageBox.information(self, "Success", "Encrypted successfully")
            else:
                QMessageBox.critical(self, "Error", "Failed to encrypt")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": self.ui.ciphertext_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plaintext_txt.setText(data["decrypt_text"])
                QMessageBox.information(self, "Success", "Decrypted successfully")
            else:
                QMessageBox.critical(self, "Error", "Failed to decrypt")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereApp()
    window.show()
    sys.exit(app.exec_())
    