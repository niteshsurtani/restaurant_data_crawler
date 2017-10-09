attribute_mapping = {}
attribute_mapping['CUISINE'] = "cuisine_name"
attribute_mapping['CITY'] = "city.name"
attribute_mapping['LOCALITY'] = "locality.name"

def findRestaurant(dictOfValues):
	cuisine_flag = 0
	if "CUISINE" in dictOfValues.keys():
		cuisine_flag = 1
		sqlQuery = "SELECT restaurants.name FROM city, locality, restaurants, locality_restaurant, cuisine,cuisine_restaurant WHERE " \
			"locality.locality_id = locality_restaurant.locality_id " \
 			"AND locality_restaurant.`restaurant_id` = restaurants.`restaurant_id` " \
			"AND cuisine.`cuisine_id` = cuisine_restaurant.`cuisine_id`" \
			"AND cuisine_restaurant.`restaurant_id` = restaurants.`restaurant_id` AND "
	else:
		sqlQuery = "SELECT restaurants.name FROM city, locality, restaurants, locality_restaurant, dish, menu WHERE " \
			"locality.locality_id = locality_restaurant.locality_id " \
 			"AND locality_restaurant.`restaurant_id` = restaurants.`restaurant_id` " \
 			"AND dish.dish_id = menu.dish_id" \
			"AND menu.`restaurant_id` = restaurants.`restaurant_id` AND "

	length = len(dictOfValues)	
	for key in dictOfValues:
		if key in attribute_mapping.keys():
			attribute_key = attribute_mapping[key]
		else:
			attribute_key = key

		if length>1:
			if type(dictOfValues[key]) == str:
				sqlQuery += "( " + attribute_key + "=" + "'" + str(dictOfValues[key]) + "'" + " )" + " AND "
			elif type(dictOfValues[key]) == dict:
				for key2 in dictOfValues[key]:
					if type(dictOfValues[key][key2]) == dict:
						sqlQuery += "( " + attribute_key + " BETWEEN " + str(dictOfValues[key][key2]["min"]) + " AND " + str(dictOfValues[key][key2]["max"]) + " )"+ " AND "
					elif dictOfValues[key][key2] != None:
						sqlQuery += "( " + attribute_key + "=" + str(dictOfValues[key][key2]) +  " )" + " AND "
			else:
				sqlQuery += "( " + attribute_key + "=" + str(dictOfValues[key]) + " )" + " AND "
			length -= 1
		else:
			if type(dictOfValues[key]) == str:
				sqlQuery += "( " + attribute_key + "=" + "'" + str(dictOfValues[key]) + "'" + " )"
				break
			elif type(dictOfValues[key]) == dict:
				for key2 in dictOfValues[key]:
					if type(dictOfValues[key][key2]) == dict:
						sqlQuery += "( " + attribute_key + " BETWEEN " + str(dictOfValues[key][key2]["min"]) + " AND " + str(dictOfValues[key][key2]["max"]) + " )"
					elif dictOfValues[key][key2] != None:
						sqlQuery += "( " + attribute_key + "=" + str(dictOfValues[key][key2]) +  " )"
				break
			else:
				sqlQuery += "( " + attribute_key + "=" + str(dictOfValues[key]) + " )"
				break
	print sqlQuery

dictOfParams = {"prize":{"exact": None,"range":{"min":45,"max":567}},"name":"Papu Pizza","url":"PPizza.com","address":"Govind Nagar","locality_id":345,"latitude":1.73,"longitude":79.412,"rating":.0002,"country_id":42,"phone":9090909090,"timings":"0400am",}
			# "average_cost_for_two":None,"is_pure_veg":None,"sports_bar_flag":None,"has_bar":None,"has_ac":None,"has_dine_in":None,"has_delivery":None,"takeaway_flag":None,"accepts_credit_cards":None,\
			# "accepts_debit_cards":None,"sheesha_flag":None,"halal_flag":None,"has_wifi":None,"has_live_music":None,"nightlife_flag":None,"stag_entry_flag":None,"entry_fee":None,\
			# "has_online_delivery":None,"min_order":None,"average_delivery_time":None,"delivery_charge":None,"accepts_online_payment":None}
findRestaurant(dictOfParams)