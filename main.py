from bs4 import BeautifulSoup
import requests
import lxml

result = requests.get('https://news.ycombinator.com/').text

soup = BeautifulSoup(result, 'lxml')

tags = soup.select(selector='.title .titleline')

articles_titles = [title.find('a') for title in tags]


with open('articles.txt', 'w') as file:
  for i in range(len(articles_titles)):
    file.write(f"Title: {articles_titles[i].text}\nLink: {articles_titles[i].get('href')}\n\n")