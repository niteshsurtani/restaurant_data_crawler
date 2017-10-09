from foodpanda_locality import insertManyLocalities, insertOneLocality, findLocalitiesByCityId
from foodpanda_city import insertManyCities,findAllCities
from foodpanda_restaurants import insertManyRestaurants, insertOneRestaurant
from foodpanda_menu import insertManyDishes
from crawlers.restaurant import find_all_restaurants,restaurant_info
from crawlers.locality import find_foodpanda_valid_locality 
from foodpanda_cuisine_restaurant import insertManyCuisines
from foodpanda_cuisine import findAllCuisines
from foodpanda_locality_restaurant import insertManyLocalityRestaurants
from time import time
from crawlers.city import city_List

def main():
	# cityName = raw_input("Enter city names you want localities for(name should be seprated by comma without any spaces between two cities names)")	
	# cityName = cityName.split(",")
	# lengthOfFoodInfo = 0
	'''It is assumed that we already have cities in our database'''
	#fetching all the cities from database
	cityDB = city_List()
	insertManyCities(cityDB	)
	for cityId in cityDB:
		print cityId
	# 	for locality in find_foodpanda_valid_locality(int(cityId[0]))[0]:
	# 		insertManyLocalities([locality])
		time1 = time()
		# print cityId[0]
		# if((cityId[0] != '1') and (cityId[0] != '11') and (cityId[0] != '10') and (cityId[0]!='17') and (cityId[0]!='12') and (cityId[0]!='27') and (cityId[0]!='3') and (cityId[0]!='185')\
		# 	and (cityId[0] != '126') and (cityId[0] != '127') and  (cityId[0] != '128') and (cityId[0] != '129') and (cityId[0] != '130') and (cityId[0] != '131') and (cityId[0] != '132') and (cityId[0] != '134')\
		# 	and (cityId[0] != '135') and (cityId[0] != '137') and (cityId[0] != '139') and (cityId[0] != '141') and (cityId[0] != '142') and (cityId[0] != '145') and (cityId[0] != '146') and (cityId[0] != '148')\
		# 	and (cityId[0] != '149') and (cityId[0] != '150') and (cityId[0] != '154') and (cityId[0] != '157') and (cityId[0] != '158') and (cityId[0] != '160') and (cityId[0] != '161') and (cityId[0] != '163')\
		# 	and (cityId[0] != '164') ,164,169,174,178,179,18,180,186,19,190,191,193,194,196,2,20,201,21):
		# print cityId[1]
		#crawling common floor website for localities 
		# localities = find_locality(cityId[1])
		#crawling foodpanda for foodpanda valid localities
		foodPandaLoca,locality_id = find_foodpanda_valid_locality(cityId[0])
		if (foodPandaLoca):
			insertManyLocalities(foodPandaLoca)
			# print len(foodPandaLoca)
		for loca in foodPandaLoca:
			#crawling all the restraunts idies in a particular locality
			restaurant_id = find_all_restaurants(loca,cityId[0])
			for oneRestaurantId in restaurant_id:	
				#crawling restaurantInfo,foodInfo and cuisineInfo for a particular restaurant
				restaurantInfo,foodInfo,cuisineInfo = restaurant_info(oneRestaurantId)
				if restaurantInfo:
					insertManyRestaurants([restaurantInfo])
					insertManyLocalityRestaurants([(loca[0],restaurantInfo[0],)])
				if(foodInfo):
					print foodInfo
					insertManyDishes(foodInfo)
					listOfUniqueCuisines = findAllCuisines()
					for restaurantCuisine in cuisineInfo:
						for cuisine in listOfUniqueCuisines:
							if restaurantCuisine[1] == cuisine[1]:
								insertManyCuisines([(restaurantCuisine[0],cuisine[0],)])
				# if(restaurantInfo):
				# 	insertManyRestaurants([restaurantInfo])
				# 	insertManyLocalityRestaurants([tuple((loca[0],oneRestaurantId[0],))])
				# if(foodInfo):
				# 	insertManyDishes(foodInfo)
				# if(cuisineInfo):
				# 	for item in cuisineInfo:
				# 		insertManyCuisines([item])
				# 	print lengthOfFoodInfo
		time2 = time()
		print "Time Taken:",time2-time1
		break

	# else: 
	#  	cityDB = findAllCities()
	#  	for city in cityDB:
	#  		localities = find_locality(city[1])
	#  		foodPandaLoca,locality_id = find_foodpanda_valid_locality(city[0],localities)


if __name__ == '__main__':
	main()