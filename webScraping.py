import MySQLdb
import requests
from bs4 import BeautifulSoup

page = requests.get("http://allrecipes.com")
soup = BeautifulSoup(page.content, 'html.parser')
recipeNames = soup.find_all('span', class_='fixed-recipe-card__title-link')

for i in recipeNames:
  print(i.get_text())

recipeLinks = soup.find_all('a', class_='fixed-recipe-card__title-link', href=True)
for i in recipeLinks:
    recipePage = requests.get(i['href'])
    nextSoup = BeautifulSoup(recipePage.content, 'html.parser')
    ingredients = nextSoup.find_all('span', class_='recipe-ingred_txt')
    for j in ingredients:
        print(j.get_text())
