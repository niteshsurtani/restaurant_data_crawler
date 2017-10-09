from api.city import *
from api.locality import *
from api.restaurant import *
from api.dishes import *
from api.cuisine import *
from re import sub

DB_ZOMATO = "zomato"
DB_FOODPANDA = "foodpanda"
DB_WAREHOUSE = "warehouse"

restaurant_params = ['restaurant_id','name','url','address','latitude','longitude','rating','country_id','phone','timings','average_cost_for_two','is_pure_veg', \
            'sports_bar_flag','has_bar','has_ac','has_dine_in','has_delivery','takeaway_flag','accepts_credit_cards','accepts_debit_cards', \
            'sheesha_flag','halal_flag','has_wifi','has_live_music','nightlife_flag','stag_entry_flag','entry_fee','has_online_delivery', \
            'min_order','average_delivery_time','delivery_charge','accepts_online_payment']


def initializeRestaurant(): 
	restaurant_details = {}
	for param in restaurant_params:
		restaurant_details[param] = ""
	return restaurant_details

def normalize_key(key):
	key_db_name = ""
	key_id = ""
	if(key[0:2] == 'Z_'):
		key_id = key[2:]
		key_db_name = "zomato"
	elif(key[0:2] == 'F_'):
		key_id = key[2:]
		key_db_name = "foodpanda"
	return key_id, key_db_name

def mergeRestaurantDetails(db_name,details,restaurant_details):
	for param in restaurant_params:
		if restaurant_details[param] == "":
			restaurant_details[param] = details[param]
		else:
			# Overwrite the details if zomato db
			if db_name == "zomato":
				restaurant_details[param] = details[param]

def restaurantDetails(restaurant):
	restaurant_details = initializeRestaurant()
	for key, name in restaurant.iteritems():
		normalized_key, db_name = normalize_key(key)
		details = getRestaurantDetails(db_name,normalized_key)
		mergeRestaurantDetails(db_name,details,restaurant_details)

	return restaurant_details

def existRestaurantInMappingList(restaurant,restaurant_id_mapping):
	for key, name in restaurant.iteritems():
		normalized_key, db_name = normalize_key(key)
		if normalized_key in restaurant_id_mapping:
			return 1
	return 0

def normalizeRestaurantName(restaurant_name):
	name = sub(r"\(.*?\)","",restaurant_name)
	tokens = name.split(",")
	name = tokens [0]
	strip_string = ''.join(e for e in name if e.isalnum() or e.isspace())
	strip_string = strip_string.strip()
	strip_string = strip_string.lower()
	return strip_string

def preprocessRestaurants(restaurant_list):
	for key, restaurant_name in restaurant_list.iteritems():
		name = sub(r"\(.*?\)","",restaurant_name)
		tokens = name.split(",")
		name = tokens [0]
		strip_string = ''.join(e for e in name if e.isalnum())
		strip_string = strip_string.lower()
		restaurant_list[key] = strip_string
			
def getMappingRestaurant(restaurant):
	restaurant_list = restaurant.copy()
	restaurant_mapping = {}

	for key, restaurant_name in restaurant_list.iteritems():
		if restaurant_name != "0":
			restaurant_list[key] = "0"
			for k,v in restaurant_list.iteritems():
				restaurant_mapping[restaurant_name] = {}
				restaurant_mapping[restaurant_name][key] = restaurant_name

				if v != "0":
					if restaurant_name.find(v) > -1 or v.find(restaurant_name) > -1:
						restaurant_mapping[restaurant_name][k] = v
						restaurant_list[k] = "0"

	return restaurant_mapping

# zomato_dish = getAllDish(DB_ZOMATO)
# fp_dish = getAllDish(DB_FOODPANDA)
# warehouse_dish = list(set(zomato_dish + fp_dish))
# insertDish(warehouse_dish)

# zomato_cuisine = getAllCuisine(DB_ZOMATO)
# fp_cuisine = getAllCuisine(DB_FOODPANDA)
# warehouse_cuisine = list(set(zomato_cuisine + fp_cuisine))
# insertCuisine(warehouse_cuisine)

city_list = getAllCities(DB_WAREHOUSE)
warehouse_city ={}
for city in city_list:
	warehouse_city[city[0]] = str(city[1])

count = 0 

# Overwriting the warehouse for testing the merge for Bangalore
# warehouse_city ={}
# warehouse_city[17] = "Bangalore"

for city_id, city in warehouse_city.iteritems():
	# Each city
	if(city_id>88):
		print "City Name = ",
		print city_id,city
		zomato_localities = {}
		fp_localities = {}

		restaurant_id_mapping = {}

		mapping_cities = getCityMappingByName(DB_WAREHOUSE,city)

		for map_city_tp in mapping_cities:
			map_city = map_city_tp[0]
			zomato_city_id = getCityByName(DB_ZOMATO,map_city)
			foodpanda_city_id = getCityByName(DB_FOODPANDA,map_city)
			if(zomato_city_id != None):
				getMappingCityLocalities(DB_ZOMATO,zomato_city_id,zomato_localities)
			if(foodpanda_city_id != None):
				getMappingCityLocalities(DB_FOODPANDA,foodpanda_city_id,fp_localities)

		# Change zomato key by appending "z" and foodpanda key by appending "f"
		zomato_localities_new = {}
		fp_localities_new = {}

		for key in zomato_localities:
			new_key = "Z_"+str(key)
			zomato_localities_new[new_key] = zomato_localities[key].lower()
		for key in fp_localities:
			new_key = "F_"+str(key)
			fp_localities_new[new_key] = fp_localities[key].lower()

		all_localities = {}
		all_localities = zomato_localities_new.copy()
		all_localities.update(fp_localities_new)

		# print "All localities = ",
		# print all_localities

		for locality_id, locality in all_localities.iteritems():
			# Each locality
			print "Locality = ",
			print locality

		# IF LOCALITY doesn't already exist in the locality table
			inserted_locality_id = 0
			if not existLocality(city_id,locality):
				# STEP: Update locality in the warehouse
				# 		and retrieve its new inserted id
				# Inserting localities and restaurants in Warehouse
				######################################################
				key_id,	key_db_name = normalize_key(locality_id)
				lat = 0.0
				lon = 0.0

				key_row = getLocalityById(key_db_name,key_id)
				name = key_row[1]
				if key_db_name == "zomato":
					lat = key_row[3]
					lon = key_row[4]
				insertLocality(name,city_id,lat,lon)
				inserted_locality_id = findLastInsertedLocalityId()
				# print "Inserted Locality = ",
				# print inserted_locality_id
				# ######################################################

			else:
				inserted_locality_id = getLocalityId(locality,city_id)
				# print "Present Locality = ",
				# print inserted_locality_id
			
				# Each locality from zomato and foodpanda
			locality_mapping = {}
			
			locality = locality.lower()
			
			for k,v in all_localities.iteritems():
				v = v.lower()
				if v.find(locality) > -1:
					locality_mapping[k] = v
			
			# print "Locality Mapping = ",
			# print locality_mapping

			all_restaurant = {}
			for localities_key in locality_mapping.keys():
				# Get all restaurants
				key_id,	key_db_name = normalize_key(localities_key)
				restaurant_list = getAllRestaurantsByLocalityId(key_db_name,key_id)
				all_restaurant.update(restaurant_list)
			# ALL RESTAURANT is the updated list of all restaurants in a given locality

			# Find the restaurants in Zomato and Foodpanda that map to each other
			restaurant_list = all_restaurant.copy()

			# Ex 1 - Mast Kalandar (Whitefield, Adj Forum Mall) 
			# Ex 2 - Refresh, Whitefield
			# 1. Remove text in (*)
			# 2. Remove text after ','
			# 3. Remove special characters, spaces and convert to lowercase
			preprocessRestaurants(restaurant_list)
			restaurant_mapping = getMappingRestaurant(restaurant_list)
			# print "Restaurant Mapping = ",
			# print restaurant_mapping

			# Each restaurant in the restaurant mapping dictionary is a new restaurant in the warehouse
			# Get all data from zomato and foodpanda
			for rest_name, rest_dict in restaurant_mapping.iteritems():
				# Check if any restaurant in the restaurant_dict exist in the restaurant_mapping table.

				new_restaurant_flag = 0
				if not existRestaurantInMappingList(rest_dict,restaurant_id_mapping):

					# Get all the details
					rest_details = restaurantDetails(rest_dict)
					
					# Normalize restaurant name
					rest_details['name'] = normalizeRestaurantName(rest_details['name'])

					restaurant_inserted_id = 0
					# Check whether rest_name exists in "warehouse"
					if existRestaurantInWarehouse(locality_id,rest_details['name']):
						# Update details
						restaurant_inserted_id = getRestaurant(locality_id,rest_details['name'])
						updateExistingRestaurant(restaurant_inserted_id,rest_details)
					else:
						# This new restaurant is to be inserted
						insertNewRestaurant(rest_details)
						restaurant_inserted_id = findLastInsertedRestaurantId()
						new_restaurant_flag = 1

					# print restaurant_inserted_id
					restaurant_cuisine = []
					restaurant_locality = []

					fp_flag = 0
					for key in rest_dict:
						normalized_key, db_name = normalize_key(key)
						restaurant_id_mapping[normalized_key] = restaurant_inserted_id

						# For this restaurant, get all dishes from Foodpanda
						# Get the new id inserted and add the details in the restaurant_menu table
						if new_restaurant_flag == 1:
							if(fp_flag == 0 and db_name == "foodpanda"):
								fp_flag = 1
								dishes = getDishesFromRestaurantId(db_name,normalized_key)
								# print "Dishes ",
								# print dishes
								# insert dishes in warehouse with new restaurant id
								insertDishes(restaurant_inserted_id,dishes)

						# For this restaurant, get all cuisines from Foodpanda and Zomato and create a set
						# Get the new id inserted and add the details of cuisines in cuisine_restaurant table
						getCuisineFromRestaurantId(db_name,normalized_key,restaurant_cuisine)
						getLocalityFromRestaurantId(db_name,normalized_key,restaurant_locality)
					
					restaurant_cuisine_unique = list(set(restaurant_cuisine))
					# print "Cuisines ",
					# print restaurant_cuisine_unique
					insertRestaurantCuisines(restaurant_inserted_id,restaurant_cuisine_unique)

					# restaurant_locality_unique = list(set(restaurant_locality))
					# print "restaurant_locality ",
					# print restaurant_locality_unique
					insertRestaurantLocality(restaurant_inserted_id,inserted_locality_id)

				else:
					insertRestaurantLocality(restaurant_inserted_id,inserted_locality_id)

