"""
1. Để chạy được code, cần cài đặt thư viện pycryptodome bằng câu lệnh sau: pip install pycryptodome
2. Sử dụng câu lệnh sau để chạy code: python 52200205_52200051_52200033_9.py
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Tạo cặp khoá RSA
key = RSA.generate(1024)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Mã hóa thông điệp
message = b'This is a secret message'
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
ciphertext = cipher.encrypt(message)

# Giải mã thông điệp
decipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted_message = decipher.decrypt(ciphertext)

print(f'Thông điệp gốc (Original message): {message}')
print(f'\nThông điệp đã được mã hóa (Encrypted message): {ciphertext}')
print(f'\nThông điệp đã được giải mã (Decrypted message): {decrypted_message}')

# Xác minh
if message == decrypted_message:
    print("\nMã hóa thành công: Thông điệp được giải mã khớp với thông điệp gốc.")
else:
    print("\Mã hóa thất bại: Thông điệp được giải mã không khớp với thông điệp gốc.")
