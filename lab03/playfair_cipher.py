import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from ui.playfair import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.encrypt_btn.clicked.connect(self.call_api_encrypt)
        self.ui.decrypt_btn.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.plaintext_txt.toPlainText(),
            "key": self.ui.key_txt.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.ciphertext_txt.setText(data["encrypted_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "Error", f"Encryption Failed: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.ciphertext_txt.toPlainText(),
            "key": self.ui.key_txt.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plaintext_txt.setText(data["decrypted_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "Error", f"Decryption Failed: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("Playfair Cipher Tool")
    window.show()
    sys.exit(app.exec_())
