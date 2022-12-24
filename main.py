import requests
from bs4 import BeautifulSoup #import the beautifulsoup



response=requests.get("https://news.ycombinator.com/") #gettng the sites API
web_page=response.text
soup=BeautifulSoup(web_page,"html.parser") # Creating a  soup
table=soup.find("table", class_="itemlist")
titles=[t.text.strip() for t in table.find_all("tr",class_="athing")]
links=[t.find('span',class_="titleline").find('a')['href'].strip() for t in table.find_all("tr",class_="athing")]
upvotes=[t.find('span',class_="score").text() for t in table.find_all("tr",class_="athing")]
# article_upvotes=[int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
# highest_upvotes=max(article_upvotes)
# hihgest_index=article_upvotes.index(highest_upvotes)
# print(titles[hihgest_index])
# print(links[hihgest_index])











# with open("/Users\hp\Desktop/100DaysOfCode by Angela Yu/100intermediatelevel2\web development\HTML personal site/index.html", encoding='utf8') as website: #opening an dcreating a file 
    # file=website.read()
# soup=BeautifulSoup(file,"html.parser") #creating a soup object from beautiful soup
# print(soup.title.name) #name of the tag
# print(soup.title.string) # string in the tag
# print(soup.prettify()) # proper indentation
# for data in soup.find_all("a"):
    # print(data.get_text()) #get the text only
    # print(data.get("href")) #get the link only
# heading=soup.find(name="h3",id="experience").get_text() #finding a specific name and attributes or class
# url=soup.select_one(selector="p a") # to selct a specific tag using the css selectors
# url=soup.select(".heading") # to selct a specific tag 
# print(url)
#newlist = [expression for item in iterable if condition == True]
# print(article_upvotes)
# print(article_links)
# print(article_text)
# article_upvote=
# # print(article_tag)
# print(article_link)
# print(article_upvote)
#score_33232165
# article=soup.find(name="span",class_="titleline")#gwtting the link class amd its text'
# article_text=[text.text for text in article.find_all(name="span",class_="titleline")]
# article_links=[link for link in article.find_all(name="a")]