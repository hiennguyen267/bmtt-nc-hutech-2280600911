import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b()
    blake2_hash.update(message)
    return blake2_hash.hexdigest()

def main():
    text = input("Nhập chuỗi văn bản: ")
    text_bytes = text.encode('utf-8')
    hashed_text = blake2(text_bytes)

    print("Chuỗi văn bản: ", text)
    print("Blake2 HASH:", hashed_text)

if __name__ == "__main__":
    main()