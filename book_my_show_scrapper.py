import requests
from bs4 import BeautifulSoup

url='https://in.bookmyshow.com/manipal/movies'
response=requests.get(url)
html=response.content

soup = BeautifulSoup(html,"lxml")
x= soup.find_all('a',class_="__movie-name")
for row in x:
	print row.string