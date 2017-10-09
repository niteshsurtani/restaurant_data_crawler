from urllib2 import Request, urlopen, URLError
import re
from bs4 import BeautifulSoup

response = urlopen("https://www.zomato.com/ncr/restaurants")
html = response.read()
soup = BeautifulSoup(html)
data =  soup.find("ul",{"class":"facet-list-dialog livefiltersearch"}).find_next('ul').text
data = re.sub("\("," ",data)
data = re.sub("\)"," ",data)
cuisine = ''
for i in data:
	i = str(i)
	if i.isalpha() or i == ' ':
		cuisine += i
cuisine = cuisine.split("  ")
cuisine.pop(len(cuisine)-1)
for i in 

# 	if not i.isalpha():
# 		print type(i)
# 		data.remove(i)
# print data
# for cuisine in soup.find("ul",{"class":"facet-list-dialog livefiltersearch"}).find_next('ul'):
# 	 # cuisineDB.append((typec(cuisine.text.strip(),'string','string'),))
# 	 print cuisine.text#.strip()
