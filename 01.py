string= "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def funcion(string):

    new_string= ''

    for char in string:

        if char == 'y':

            new_string += 'a'

        elif char == 'z':

            new_string += 'b'

        elif ord(char) >= 97 and ord(char) <= 120:

            new_string += chr(ord(char)+2)

        else:

            new_string += char

    return new_string

print(funcion(string), "\n") # Nos dice la instrucción de utilizar el código en la URL.

# Segunda opcion que funcionaria igualmente

def funcion2(string):

    tabla = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

    '''
    Acá el problema se puede ver de manera más sencilla, 
    simplemente tenemos que utilizar un alfabeto dos letras hacia la derecha,
    hacemos una traducción de la tabla, con la palabra map,
    esto, porqué es el nombre de la url de la página.
    '''

    return(string.translate(tabla))

print('http://www.pythonchallenge.com/pc/def/' + str(funcion('map')) + '.html')

'Copiamos la url anterior y la pegamos en la url del buscador'