'''

Acá tenemos que obtener el dato que está escondido en la franja gris del PNG de la página;
Tenemos que tomar la fila media, muestrear cada 7 píxeles y convertir los valores grises da 
una lista de bytes con el mensaje que incluye los códigos ASCII.

Hay que tener algo en consideración, nosotros vamos a convertir los valores grises
a través de .convert('L'), esto debido a que al utilizar getpixel da un error,
que dice que la tupla (r,g,b) no tiene los tres canales iguales.

'''

import requests
import io
from PIL import Image
import ast
import re

def buscando_oxigeno(base="http://www.pythonchallenge.com/pc/def/"):
    url = base + "oxygen.png"
    resp = requests.get(url)
    resp.raise_for_status()

    # Abrir y convertir a escala de grises (modo 'L')
    im = Image.open(io.BytesIO(resp.content)).convert('L')
    w, h = im.size
    mid = h // 2

    # Muestreo cada 7 píxeles a lo largo de la fila media
    vals = []
    for x in range(0, w, 7):
        v = im.getpixel((x, mid))
        vals.append(v)

    data = bytes(vals)
    print("Bytes extraídos:", data)

    # Extraer la lista de números y convertirla a lista de ints
    m = re.search(rb"\[([0-9,\s]+)\]", data)
    if not m:
        raise RuntimeError("No se encontró la lista de números en los bytes")
    nums = ast.literal_eval("[" + m.group(1).decode() + "]")

    word = ''.join(chr(n) for n in nums)
    print("Palabra encontrada:", word)
    print("Siguiente URL:", base + word + ".html")

buscando_oxigeno(base="http://www.pythonchallenge.com/pc/def/")


