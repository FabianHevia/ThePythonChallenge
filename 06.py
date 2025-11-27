"""

Tenemos que descargar channel.zip y extraer el enlace que se tiene.
Luego de esto vamos a revisar el texto que descargamos.
Tenemos que decodificar lo que dice, y revisar la palabra que dicen las letras como dice hockey.html

"""

import requests
import io
import zipfile
import re
from urllib.parse import urljoin
from collections import Counter

BASE = "http://www.pythonchallenge.com/pc/def/"

def solve_channel_to_oxygen(base=BASE, start='90052.txt', verbose=True):
 
    zip_url = urljoin(base, "channel.zip")
    if verbose:
        print("Descargando:", zip_url)
    r = requests.get(zip_url)
    r.raise_for_status()

    z = zipfile.ZipFile(io.BytesIO(r.content))

    if verbose:
        print("Archivos en zip:", len(z.namelist()))
        # opcional: ver algunos nombres
        print("Primeros 10 nombres:", z.namelist()[:10])

    comment_bytes = []
    current = start
    seen = set()
    patt_next = re.compile(r'next nothing is (\d+)', re.I)

    while True:
        if current in seen:
            if verbose:
                print("Detectado ciclo en", current)
            break
        seen.add(current)

        try:
            data = z.read(current).decode('utf-8')
        except KeyError:
            if current.endswith('.txt'):
                alt = current[:-4]
                try:
                    data = z.read(alt).decode('utf-8')
                    current = alt
                except KeyError:
                    raise RuntimeError(f"No existe {current} ni {alt} en el ZIP.")
            else:
                raise RuntimeError(f"No existe {current} en el ZIP.")

        zi = z.getinfo(current)

        if zi.comment:

            comment_bytes.append(zi.comment)

            if verbose:

                print(f"[{current}] comentario (len={len(zi.comment)}): {zi.comment!r}")

        m = patt_next.search(data)

        if m:

            nxt = m.group(1) + '.txt'

            if verbose:

                print(f"[{current}] -> siguiente: {nxt}")

            current = nxt
            continue

        else:

            if verbose:

                print("Final (archivo sin 'next'):", current)
                print("Contenido final del archivo:")
                print(data)

            break

    combined = b''.join(comment_bytes)

    try:

        word = combined.decode('utf-8')

    except UnicodeDecodeError:

        word = combined.decode('latin-1')

    if verbose:

        print("\nComentarios concatenados (raw bytes):", combined)
        print("Decodificado:", word)

    return word.strip()

solve_channel_to_oxygen()
