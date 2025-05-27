from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)
@app.route("/")
def home () :
    return render_template('index.html')
#router routes for caesar cypher
@app.route("/caesar")
def caesar () :
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt ():
    text = request.form['inputPlainText']
    key = int (request.form['inputKeyPlain'])
    Caesar = CaesarCipher ()
    encrypted_text = Caesar.encrypt_text (text, key)
    return f"text: {text} <br/>key: {key}<br/>encrypted text:{encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt () :
    text = request.form['inputCipherText']
    key = int (request.form ['inputKeyCipher'])
    Caesar = CaesarCipher ()
    decrypted_text = Caesar.decrypt_text (text, key)
    return f"text: {text}<br/>key: {key} <br/>decrypted text: {decrypted_text}"

#router routes for vigenere cypher
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"Encrypted text: {encrypted_text}"

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"Decrypted text: {decrypted_text}"

# Router routes for Rail Fence cipher
@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)  # Corrected method name
    return f"Encrypted text: {encrypted_text}"

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)  # Method name is already correct
    return f"Decrypted text: {decrypted_text}"

# Router routes for Playfair cipher
@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    encrypted_text = playfair.playfair_encrypt(text, key)
    return f"Encrypted text: {encrypted_text}"

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    decrypted_text = playfair.playfair_decrypt(text, key)
    return f"Decrypted text: {decrypted_text}"

# Main function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)