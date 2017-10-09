from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re
from errorhandler import typec
from zomato_city import findCityByName,updateManyCities

def crawlCity():
	try:
		cityDB = []
		response = urlopen("https://zomato.com/india")
		html = response.read()
		soup = BeautifulSoup(html)
		for city in soup.find_all("a",{"class":"country-links"}):
			cityDB.append((typec(city.text.strip(),'string','string'),re.sub("https://www.zomato.com/","",(city["href"])),))
		return cityDB

	except URLError as error:
		print error
# f= open('city.txt','w')
# cityDB = crawlCity()
# for city in cityDB:
# 	f.write(city[0]+'\n')
# f.close()
cityDB = crawlCity()
cityId = []
for city in cityDB:
	if findCityByName(city[1]) != []:
		city = ((city[1],findCityByName(city[1])[0][1]),)
		updateManyCities(ci)

print cityId
# UPDATE aselectcity set base_city_name = '' WHERE Name = ''