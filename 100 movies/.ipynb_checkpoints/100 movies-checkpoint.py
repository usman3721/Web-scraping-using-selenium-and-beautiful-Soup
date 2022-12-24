from turtle import title
from bs4 import BeautifulSoup
import requests
response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_html=response.text
soup=BeautifulSoup(web_html,"html.parser")
print(soup.find('title').text)
spant = (soup.find('div', class_="jsx-3523802742 listicle-item"))
# print(spant.find_next_element('h3'))
print(spant.find('h3').text)
