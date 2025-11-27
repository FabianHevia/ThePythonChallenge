'''
Pues pick hell suena similar a pickle... supuestamente.

Descargamos el banner.p, 
lo deserializamos y mostramos el banner; 
al final imprimimos la palabra encontrada 
y lo adjuntamos dando la URL siguiente.
'''

import pickle
import requests
import io

resp = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")

# Convertimos resp.content (bytes) en un buffer para pickle.load
buffer = io.BytesIO(resp.content)

data = pickle.load(buffer)

for i in data:
    print(''.join([key * val for key, val in i]))

'''
http://www.pythonchallenge.com/pc/def/channel.html

Copiar y pegar la anterior url para ir al nivel 6
'''