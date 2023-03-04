#programa para generar una password de longitud 12 con numeros, letras y caracteres especiales.

import random
import string

def generar_contraseña():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    longitud = 12
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

print(generar_contraseña())


