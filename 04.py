'''
La página de The Python Challenge, nos dice que podemos usar urlib,
sin embargo, se puede resolver el reto a solo requests,
por lo que vamos a intentar esta manera.

La página es sus recursos nos dice lo siguiente:
<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->

Por lo que vamos a ir al primer nothing en el siguiente url:
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=

En el href de la imagen nos dan la siguiente pista, de ir a nothing=12345 dentro del url.
<a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"/></a>

En ambas páginas nos dan los siguientes numeros:
55274, 44827

Y seguramente si seguimos así vamos a tener números practicamente infinitos,
a menos de que diseñemos un código para ir buscando todos los 'nothing',
por así decirlo.
'''


import re
import requests

def follow_linkedlist(start='12345', max_steps=10000, verbose=True):
    base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    sess = requests.Session()
    sess.headers.update({"User-Agent": "Mozilla/5.0 (compatible; Python script)"})

    # Patrones
    pat_next = re.compile(r'next nothing is (\d+)', re.I)          # "and the next nothing is 12345"
    pat_any_number = re.compile(r'(\d+)')                         # cualquier número
    # Acepta "divide by two" o "divide by 2" (más tolerante con espacios/puntuación)
    pat_divide = re.compile(r'divide\s*(?:by|\/)\s*(?:2|two)\b', re.I)

    current = str(start)
    visited = set()
    history = []

    for step in range(max_steps):
        url = base + current
        resp = sess.get(url)
        text = resp.text.strip()
        history.append((current, text))

        if verbose:
            # muestro repr para ver si hay tags o saltos de línea que interfieran
            print(f"[{step}] {url} -> {repr(text)}")

        # 1) Intento patrón estándar "next nothing is N"
        m = pat_next.search(text)
        if m:
            new = m.group(1)
            if new in visited:
                if verbose:
                    print("Detectado ciclo en 'next'. Parando.")
                break
            visited.add(new)
            current = new
            continue

        # 2) Si hay instrucción para dividir por 2 -> aplicarla
        if pat_divide.search(text):
            # Primero intentamos extraer el último número visible en la página
            nums = pat_any_number.findall(text)
            if nums:
                last_num = int(nums[-1])
            else:
                # Si no hay número en la página, tomar el número que usamos en la URL actual
                try:
                    last_num = int(current)
                except ValueError:
                    if verbose:
                        print("No se encontró número en la página ni en la URL actual. Parando.")
                    break

            new = str(last_num // 2)  # división entera
            if verbose:
                print(f"Regla especial: dividir {last_num} entre 2 -> {new}")

            if new in visited:
                if verbose:
                    print("Detectado ciclo tras dividir. Parando.")
                break
            visited.add(new)
            current = new
            continue

        # 3) si no hay el patrón ni instrucción especial, intentar cualquier número de la página
        anynum = pat_any_number.search(text)
        if anynum:
            new = anynum.group(1)
            if new in visited:
                if verbose:
                    print("Detectado ciclo con número cualquiera. Parando.")
                break
            visited.add(new)
            current = new
            continue

        # 4) si no hay números ni instrucciones, asumimos que llegamos a la página final
        if verbose:
            print("\nPágina final (sin número ni instrucción detectable):")
            print(text)
        break
    else:
        if verbose:
            print("Se alcanzó el límite máximo de pasos.")

    return history  # devuelve historial [(nothing, page_text), ...]

if __name__ == "__main__":
    hist = follow_linkedlist(start='12345', verbose=True)
    print("\nÚltima página encontrada:")
    if hist:
        print(hist[-1][1])
        print('http://www.pythonchallenge.com/pc/def/' + str(hist[-1][1]))
    else:
        print("Historial vacío.")


