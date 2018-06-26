from bs4 import BeautifulSoup
import requests
import urllib.request as urllib2

url = "http://www.cricketedmonton.com/season-2018/fixtures/"
text = urllib2.urlopen(url).read()
soup = BeautifulSoup(text, "html.parser")


div = soup.find('div', attrs={'class':'entry-content'})
link = div.a.get('href')

print(link)
