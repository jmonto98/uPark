from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash 

texto = "Qwerty24*"

# Genera una clave en formato de secuencia de bytes:
#key = Fernet.generate_key()
key = b'fPIsyTog2w6PALlOWRp5yly58nvlkJZ1qkv_Om7ZCRI='
print(key)
objeto_cifrado = Fernet(key)
texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
print(texto_encriptado)
print(type(texto_encriptado))

texto_desencriptado_bytes = objeto_cifrado.decrypt(texto_encriptado)
print(texto_desencriptado_bytes)
texto_desencriptado = texto_desencriptado_bytes.decode()
print(texto_desencriptado==texto)
print(type(texto_desencriptado))

# clave = 'Qwerty24*'

# pwd = generate_password_hash(clave)
# print (clave)
# print (pwd)
# print (type(pwd))

# print(check_password_hash(pwd, clave))