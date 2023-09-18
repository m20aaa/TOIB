import hashlib

cleartext_password = input('Enter your password: ')
password_hash = hashlib.sha256(cleartext_password.encode()).hexdigest()
print(f'SHA-256 password hash: {password_hash}')
