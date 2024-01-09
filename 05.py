import pickle
from urllib.request import urlopen

link = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

data = pickle.load(link)

for i in data:
    print(''.join([key * val for key, val in i]))