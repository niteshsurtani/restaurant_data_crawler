from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re
from errorhandler import typec

def crawlLocation(cityName):
	try:
		locationDB = []
		searchUrl = "https://zomato.com/%s" % (cityName)
		response = urlopen(searchUrl)
		html = response.read()
		soup = BeautifulSoup(html)
		for location in soup.find_all("div",{"class":"home-seo-detail"}):
			for item in location.next_element.strip().split('\n'):
				string = ''
				if item != '':
					for i in item:
						if i != '(':
							string += i
						else:
							break#!= div:
				# print re.sub("(?m)^\s+","",string).split('\n')
				if string.rstrip().split('\n') != ['']:
					locationDB.append((typec(string.rstrip().split('\n')[0],'string','string'),searchUrl,))
			# locationDB.append(location.text.split().pop(0))

			 #cityDB.append((typec(city.text.strip(),'string','string'),))
		return locationDB

	except URLError as error:
		print error

f= open('locality.txt','w')
locaDB = crawlLocation("Pune")
loca = []
for i in locaDB:
	loca.append(i[0])
loca = sorted(loca)
for city in loca:
	f.write(city+'\n')
f.close()