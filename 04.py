from webbot import Browser
import re

web = Browser()
num = '12345'
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

web.go_to(link + num)
patente = re.compile('El siguiente nothing es (\d+)')

while True:
    tmp = web.get_page_source()
    match = patente.search(tmp)
    if match is None:
        break
    new = match.group(1)
    web.go_to(link + new)
