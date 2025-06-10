import hashlib

def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()


data_to_hash = input("Nhập dữ liệu để HASH bằng SHA-256: ")
hash_value = calculate_sha256(data_to_hash)
print("Giá trị HASH SHA-256:", hash_value)
