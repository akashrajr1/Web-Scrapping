import requests
from bs4 import BeautifulSoup

url='https://in.bookmyshow.com/manipal/movies'
response=requests.get(url)
html=response.content	

soup = BeautifulSoup(html,"lxml")

print "\nCurrent Movies\n"
x= soup.find_all('div',class_="detail")
for row in x:
	if len(row['class'])==1:
		print row.div.a.string