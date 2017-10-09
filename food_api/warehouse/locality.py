from api.city import *
from api.locality import *
from re import sub

ignore_city_terms = ['0','north','south','cahuraha','near','east','west','colony','bridge','sector','block','bazar','bazaar','bagh','nagar','line','lines','mall','ka','area','avenue','gate','old','main','street','new','navi','market','puram','ganj','ghat','naka','town','road','tower','towers']

DB_ZOMATO = "zomato"
DB_FOODPANDA = "foodpanda"
DB_WAREHOUSE = "warehouse"

# Warehouse cities consists of unique cities of Zomato and Foodpanda tables
# The list of mapping cities is stored in city_mapping table
city_list = getAllCities(DB_WAREHOUSE)

# Convert warehouse to dictionary
warehouse_city ={}
for city in city_list:
	warehouse_city[city[0]] = str(city[1])

count = 0 
for city_id, city in warehouse_city.iteritems():
	print city 
	zomato_localities = {}
	fp_localities = {}

	# Get all mapping cities for a city in warehouse
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
		new_key = "z"+str(key)
		zomato_localities_new[new_key] = zomato_localities[key]
	for key in fp_localities:
		new_key = "f"+str(key)
		fp_localities_new[new_key] = fp_localities[key]

	all_localities = {}
	all_localities = zomato_localities_new.copy()
	all_localities.update(fp_localities_new)

	# print all_localities

	location_values = all_localities.values()
	location_values_set = set(location_values)
	locations = list(location_values_set)
	location_len = len(locations)

	# print locations
	# Finding common localities of zomato and foodpanda cities.
	# Merging restaurants of common localities
	# Adding resturants of distinct localities 
	common_localities = []
	all_common_localities = []
	for index in range(0,location_len):
		val = locations[index]
		val = sub(r"\)|\(","",val)
		tokens = val.split(' ')
		new_localities = []
		for token in tokens:
			token = token.lower()
			if token not in ignore_city_terms:
				
				for i in range(index+1,location_len):
					zval = locations[i]
					zval = sub(r"\)|\(","",zval)
					t1 = zval.split(' ')
					for t in t1:
						t = t.lower()
						if(token == t):
							new_localities.append(zval.lower())
							all_common_localities.append(zval.lower())
							locations[i] = '0'
							break
		if len(new_localities) > 0:
			new_localities.append(val.lower())
			all_common_localities.append(val.lower())
			common_localities.append(new_localities)
			locations[index] = '0'

	# print all_localities
	# print common_localities

	for key, value in all_localities.iteritems():
	# Go through zomato and foodpanda list
	# Case 1: One has locality which other doesn't have.
	# Get all the restaurants with that id, assign locality new id, and change the id of the restaurants
	# In this case, the locality is not present in the common_localities and also not in other db (fp or zomato).
		# Mark the key as already traversed
		all_localities[key] = "0"
		if key[0] == 'z':
			zomato_localities_new[key] = "0"
		elif key[0] == 'f':
			fp_localities_new[key] = "0"

		# # Get next id to insert
		# Inserting localities and restaurants in Warehouse
		key_id = 0
		key_db_name = ""
		lat = 0.0
		lon = 0.0
		if(key[0] == 'z'):
			key_id = key[1:]
			key_db_name = "zomato"
		else:
			key_id = key[1:]
			key_db_name = "foodpanda"

		key_row = getLocalityById(key_db_name,key_id)
		name = key_row[1]
		if key_db_name == "zomato":
			lat = key_row[3]
			lon = key_row[4]
		
		#insertLocality(name,city_id,lat,lon)
		#locality_id = findLastInsertedLocalityId()
		count += 1
		locality_id = count 

		locality_mapping = {}
		locality_mapping[locality_id] = []
		locality_mapping[locality_id].append(key)

		value = value.lower()
		if value != "0":
			if value not in all_common_localities:
				match_flag = 0
				matched_key = 0
				# If match is found, then change the found match to '0'
				# Zomato, then search in foodpanda
				if key[0] == 'z':
					for k,v in fp_localities_new.iteritems():
						v=v.lower()
						if value == v:
							matched_key = k
							match_flag = 1
							
							fp_localities_new[k] = "0"
							all_localities[k] = "0"

				# Search in zomato
				else:
					for k,v in zomato_localities_new.iteritems():
						v=v.lower()
						if value == v:
							matched_key = k
							match_flag = 1
							
							zomato_localities_new[k] = "0"
							all_localities[k] = "0"

				# Case 2: Both have the same locality name
				# Get all restaurants from both locality and assign new ids
				if(match_flag == 1):
					locality_mapping[locality_id].append(matched_key)
					# Case 1. Insert this locality in warehouse
					# Get all data for the key
				# Case 3: Locality belongs in the list of common localities, process the complete list and get all the localities
				# which are more specific that the given locality
			else:
				# Locality in common localities
				# Find the list of common localities

				selected_locality = []
				for listing in common_localities:
					if value in listing:
						selected_locality = listing
				print str(len(selected_locality))
				print selected_locality
				print value
				for k,v in all_localities.iteritems():
					v = v.lower()
					print v
					if v in selected_locality:
						#print v
						locality_mapping[locality_id].append(k)
						# all_localities[k] = "0"
						# if k[0] == 'z':
						# 	zomato_localities_new[k] = "0"
						# elif k[0] == 'f':
						# 	fp_localities_new[k] = "0"
		print locality_mapping
	
'''
	tokens = city.split(' ')
	for token in tokens:
		if not checkCityGroups(zomato_city[index],city_intersection):



for zcity in zomato_city:
	
		for city in zomato_city:
			if(city.find(token)):
'''
