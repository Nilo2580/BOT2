import base64

def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key * (len(data) // len(key) + 1)))

with open(r'E:\telebot\nilesh.py.enc', 'r') as file:
    encrypted_script_base64 = file.read()

key = '@NileshModzOwner' 
encrypted_script = base64.b64decode(encrypted_script_base64).decode()
decrypted_script = xor_encrypt_decrypt(encrypted_script, key)

exec(decrypted_script)