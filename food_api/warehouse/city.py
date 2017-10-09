from api.city import *

DB_ZOMATO = "zomato"
DB_FOODPANDA = "foodpanda"

zomato_city = getAllCities(DB_ZOMATO)
foodpanda_city = getAllCities(DB_FOODPANDA)

len_zomato = len(zomato_city)
len_fp = len(foodpanda_city)

city_groups = []
city_intersection = []


for city in zomato_city:
	print city

print "\n\n\n"

for city in foodpanda_city:
	print city



'''
	tokens = city.split(' ')
	for token in tokens:
		if not checkCityGroups(zomato_city[index],city_intersection):



for zcity in zomato_city:
	
		for city in zomato_city:
			if(city.find(token)):
'''