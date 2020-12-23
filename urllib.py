from urllib.request
import urlopen
from bs4 import BeautifulSoup
a="http://"+input('url ')
f=urllib.request.urlopen(a)
print(f.read())
