from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re
from errorhandler import typec
from re import search
from re import sub
import json

def crawlRestaurants(restaurant_url):
	try:
		menu_url = []
		restaurant_menu_url_with_unicode = restaurant_url + "/menu#food"
		restaurant_menu_url_with_unicode = restaurant_menu_url_with_unicode.replace(unichr(233),'e')
		restaurant_menu_url = sub(r"[^\x00-\x7F]+","",restaurant_menu_url_with_unicode)
		try:
			response = urlopen(restaurant_menu_url)
			html = response.read()
			# print html
			rest_soup = BeautifulSoup(html)
			for javascript_code in rest_soup.find_all("script",{"type":"text/javascript"}):
				text = javascript_code.text
				pat = "zomato.menuPages"
				index = text.find(pat)
				if index >= 0:
					menu_items = search("zomato.menuPages = (.+?);",text).group(1)
					menu_dict = json.loads(menu_items)
					
					for urls in menu_dict:
						menu_url.append(str(urls['url']))
			return menu_url
		except URLError as error:
			print restaurant_menu_url
		return restaurantsDB
	except URLError as error:
		print error 
# <<<<<<< HEAD
# def crawlRestaurants(city_name,locality_name):
# 	try:
# 		restaurantsDB = []
# 		searchUrl = "https://www.zomato.com/" + city_name + "/" + locality_name.replace(" ","-").lower() + "-restaurants"
# 		response = urlopen(searchUrl)
# 		html = response.read()
# 		soup = BeautifulSoup(html)

# 		# Extracting no. of pages
# 		for pages in soup.find("div",{"class":"col-l-3 mtop0 alpha tmargin pagination-number"}):
# 			text = pages.text
# 			tokens = text.split(" ")
# 			flag = 0 
# 			page_no = 1
# 			for token in tokens:
# 				if token.isdigit():
# 					if flag == 1:
# 						page_no = int(token) + 1
# 					flag = 1
		
# 		# Crawling on each page of restaurant locality
# 		for page in range(1,page_no):
# 			searchUrl = "https://www.zomato.com/" + city_name + "/" + locality_name.replace(" ","-").lower() + "-restaurants?page="+str(page)
# 			response = urlopen(searchUrl)
# 			html = response.read()
# 			soup = BeautifulSoup(html)

# 			for rest_div in soup.find_all("li",{"class":"resZS mbot0 pbot0 bb even status1"}) + soup.find_all("li",{"class":"resZS mbot0 pbot0 bb even near status1"}):
# 				restDB = {}
# 				restDB['id'] = rest_div['data-res_id']
# 				rest_url_a = rest_div.find("a",{"class":"result-title"})
# 				rest_url = rest_url_a["href"]

# 				rest_url = rest_url.replace(unichr(233),'e')
# 				rest_url = sub(r"[^\x00-\x7F]+","",rest_url)
# 				restDB['url'] = str(rest_url)
				
# 				restaurant_menu_url_with_unicode = restDB['url'] + "/menu#food"
# 				restaurant_menu_url_with_unicode = restaurant_menu_url_with_unicode.replace(unichr(233),'e')
# 				restaurant_menu_url = sub(r"[^\x00-\x7F]+","",restaurant_menu_url_with_unicode)
# 				try:
# 					response = urlopen(restaurant_menu_url)
# 					html = response.read()
# 					# print html
# 					rest_soup = BeautifulSoup(html)
# 					for javascript_code in rest_soup.find_all("script",{"type":"text/javascript"}):
# 						text = javascript_code.text
# 						pat = "zomato.menuPages"
# 						index = text.find(pat)
# 						if index >= 0:
# 							menu_items = search("zomato.menuPages = (.+?);",text).group(1)
# 							menu_dict = json.loads(menu_items)

# 							menu_url = []
# 							for urls in menu_dict:
# 								menu_url.append(str(urls['url']))

# 					restDB['menu'] = menu_url
# 					restaurantsDB.append(restDB)
# 				except URLError as error:
# 					print restaurant_menu_url
# 		return restaurantsDB
# 	except URLError as error:
# 		print error

# print crawlRestaurants(city_name,locality_name)
# =======

