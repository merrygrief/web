from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://blog.csdn.net/jdjrdata/article/details/73614607')
bs_obj = BeautifulSoup(html.read(), 'html.parser')
test_list = bs_obj.find_all("a", "title text-truncate")
for text in test_list:
    print(text.get_text())
html.close()