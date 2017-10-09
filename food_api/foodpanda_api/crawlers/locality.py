from bs4 import BeautifulSoup
import socket
import requests
from re import sub,search
from ErrorHandler import typec
from time import time



def find_foodpanda_valid_locality(cityId):
	# try:
	foodpanda_locality = []
	locality_id = []
	#To temporarily store  Area_idies 
	tempraroy_list1 = [] 
	#To temporarily store  Name of the localities
	tempraroy_list2 = []
	
	flag = 0
	localities = []	
	# for i in "abcdefghijklmnopqrstuvwxyz":
	# 	for j in "abcdefghijklmnopqrstuvwxyz":
	# 		localities.append(i+j)
	f= open("comparison","r")
	combinations = []
	temp = f.read().strip().split('\n')
	temp.pop(0)
	for item in temp:
		item = item.split(" ")
		if int(item[1]) >= 10:
			combinations.append(item[0])
	f.close()
	print len(combinations)
	for loca in combinations:
		try:
			# print count
			# print len(foodpanda_locality)
			# print len(locality_id)
			# print locality_id
			# print loca
			# print cityId
			count = 0
			
			#getting html from the Search Url
			a = time()
			searchurl = "https://www.foodpanda.in/location-suggestions?cityId=%s&area=%s" % (cityId,loca)
			f = requests.get(searchurl)
			html = f.text
			soup = BeautifulSoup(html)
			b = time() - a
			print b
			c = time()
			#checking if the the page of Suggestions of localities is opened or 
			#the request has been redirected to the page of specific locality
			if(soup.find('h1',{'class':'h2'})):
				heading = sub(":","",soup.find('h1',{'class':'h2'}).text)
				heading = heading.strip()
				if heading=="Suggestions":		

					#Extracting Area_idies of the localities
					tempraroy_list1[:] = []
					for data in soup.find_all('a',{'class':'list-group-item'}):
						tempraroy_list1.append(search('area_id=(.+?)">', typec(data,'string','string')).group(1))
					
					#Appendng unique area_id in locality_id list 
					
					#Extracting Name of the Localities
					tempraroy_list2[:] = []
					for data in soup.find_all('div',{'class':'content-block location-suggestions'}):
						tempraroy_list2= sub("(?m)^\s+","",data.text).split('\n')
					tempraroy_list2.pop(0) 												# poping "Suggestion" string
					tempraroy_list2.pop(len(tempraroy_list2)-1)				 			# poping whitespace
					
					if tempraroy_list1 == [] and tempraroy_list2 == []:
						print loca, ":" + "0"

					#Appending Uniquely Localities Full Data in the foodpanda_locality
					for locality,area_id in zip(tempraroy_list2,tempraroy_list1):
						
						if (locality[0:2].lower() == loca):
							
							searchurl= 'http://www.foodpanda.in/restaurants?area_id=%s' % (area_id) 
							Dummytuple =  (area_id,typec((locality).replace(unichr(8226),''),'string','string'),typec(cityId,'string','string'),searchurl,)
							for item in foodpanda_locality:
		 						if Dummytuple[0] == item[0]:						
									flag = 1 
							if flag != 1 :
								foodpanda_locality.append(Dummytuple)
							if area_id not in locality_id:
								locality_id.append(area_id)
							flag = 0
							count += 1

						else:
							try:
								if (locality.split('(')[1][0:2].lower() == loca):
									
									searchurl= 'http://www.foodpanda.in/restaurants?area_id=%s' % (area_id) 
									Dummytuple =  (area_id,typec((locality).replace(unichr(8226),''),'string','string'),typec(cityId,'string','string'),searchurl,)
									for item in foodpanda_locality:
				 						if Dummytuple[0] == item[0]:						
											flag = 1
									if flag != 1 :
										foodpanda_locality.append(Dummytuple)
									if area_id not in locality_id:
										locality_id.append(area_id)
									flag = 0
									count += 1

							except:
								flag = 0
					print loca , ' : ' , count
			print (time() - c)
		except requests.exceptions.ConnectionError as e:
			print e
			f = open("locationConnectionError","a")
			f.write("cityId: %s, " % (cityId))
			f.write("combination: %s\n" % (loca))
			f.close()
			
	if None in locality_id:	
		locality_id.pop(locality_id.index(None))
	return (foodpanda_locality,locality_id)
	# except:
	# 	print "Error in locality"
	# 	print "city Id"
	# 	print cityId
	# 	print "localities"
	# 	print localities

# for num in range(1,169):
# for num in range(11,12):
# 	find_foodpanda_valid_locality(num)
