from bs4 import BeautifulSoup
import urllib.request

for i in range(100):
    url = "http://spor.haber7.com/trabzonspor/haber/"+str(2448004-i)+"-yanal-sonrasi-firtinada-ilk-idman"

    url_oku = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(url_oku, 'lxml')
    icerik = soup.find_all('ul', attrs={'class': 'comments-list'})

    for div in icerik:
        comment = div.find_all("div", {"class":"content"})

    for i in comment:
        print(i.text)
