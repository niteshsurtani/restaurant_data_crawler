from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config


restaurant_params = ['restaurant_id','name','url','address','latitude','longitude','rating','country_id','phone','timings','average_cost_for_two','is_pure_veg', \
            'sports_bar_flag','has_bar','has_ac','has_dine_in','has_delivery','takeaway_flag','accepts_credit_cards','accepts_debit_cards', \
            'sheesha_flag','halal_flag','has_wifi','has_live_music','nightlife_flag','stag_entry_flag','entry_fee','has_online_delivery', \
            'min_order','average_delivery_time','delivery_charge','accepts_online_payment']

# Zomato arguments is the list of attributes in Warehouse restaurant table
zomato_arguments = "restaurant_id,name,url,address,latitude,longitude,rating,country_id,phone,timings,average_cost_for_two,is_pure_veg,\
            sports_bar_flag,has_bar,has_ac,has_dine_in,has_delivery,takeaway_flag,accepts_credit_cards,accepts_debit_cards,\
            sheesha_flag,halal_flag,has_wifi,has_live_music,nightlife_flag,stag_entry_flag,entry_fee,has_online_delivery,\
            min_order,average_delivery_time,delivery_charge,accepts_online_payment"

foodpanda_arguments = "restaurant_id,name,address,rating,min_order,delivery_time,delivery_fee"
foodpanda_params = ['restaurant_id','name','address','rating','min_order','delivery_time','delivery_fee']

def initializeRestaurant(): 
	restaurant_details ={}
	for param in restaurant_params:
		restaurant_details[param] = ""
	return restaurant_details

def getRestaurantDetails(db_name,restaurant_id):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if db_name == "foodpanda":
			cursor.execute("SELECT " + foodpanda_arguments + " FROM restaurants WHERE restaurant_id = '"+str(restaurant_id)+"'")
		else:
			cursor.execute("SELECT " + zomato_arguments + " FROM restaurants WHERE restaurant_id = '"+str(restaurant_id)+"'")
		rows = cursor.fetchone()

		restaurant_details = initializeRestaurant()
		count = 0
		if db_name == "foodpanda":
			for param in foodpanda_params:
				restaurant_details[param] = str(rows[count])
				count += 1
		else:
			for param in restaurant_params:
				restaurant_details[param] = str(rows[count])
				count += 1
		return restaurant_details
		
	except Error as error:
		print "Error: getRestaurantDetails"
		print error

	finally:
		cursor.close()
		conn.close()

def existRestaurantInWarehouse(locality_id,name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT restaurants.restaurant_id FROM restaurants, locality_restaurant WHERE locality_id = '"+ str(locality_id) +"' AND name = '" + name + "' AND locality_restaurant.restaurant_id = restaurants.restaurant_id")

		rows = cursor.fetchone()
		if rows != None:
			return 1
		return 0
	except Error as error:
		print "Error: existRestaurantInWarehouse"
		print error

	finally:
		cursor.close()
		conn.close()

def getRestaurant(locality_id,name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT restaurants.restaurant_id FROM restaurants, locality_restaurant WHERE locality_id = '"+ str(locality_id) +"' AND name = '" + name + "' AND locality_restaurant.restaurant_id = restaurants.restaurant_id")

		rows = cursor.fetchone()
		return rows[0]
	except Error as error:
		print "Error: getRestaurant"
		print error

	finally:
		cursor.close()
		conn.close()

def getAllRestaurantsByLocalityId(db_name,locality_id):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT restaurants.restaurant_id, restaurants.name FROM restaurants, locality_restaurant WHERE locality_restaurant.locality_id = '"+ str(locality_id) +"' AND locality_restaurant.restaurant_id = restaurants.restaurant_id")

		restaurants = {}
		rows = cursor.fetchall()
		if rows != None:
			for row in rows:
				rest_id = row[0]

				if(db_name == "zomato"):
					rest_id = "Z_" + str(rest_id)
				else:
					rest_id = "F_" + rest_id
				
				rest_name = row[1]
				restaurants[str(rest_id)] = str(rest_name)
		return restaurants

	except Error as error:
		print "Error: getAllRestaurantsByLocalityId"
		print error

	finally:
		cursor.close()
		conn.close()

warehouse_restaurant_params = ['name','url','address','latitude','longitude','rating','country_id','phone','timings','average_cost_for_two','is_pure_veg', \
            'sports_bar_flag','has_bar','has_ac','has_dine_in','has_delivery','takeaway_flag','accepts_credit_cards','accepts_debit_cards', \
            'sheesha_flag','halal_flag','has_wifi','has_live_music','nightlife_flag','stag_entry_flag','entry_fee','has_online_delivery', \
            'min_order','average_delivery_time','delivery_charge','accepts_online_payment']

# Zomato arguments is the list of attributes in Warehouse restaurant table
warehouse_restaurant_arguments = "name,url,address,latitude,longitude,rating,country_id,phone,timings,average_cost_for_two,is_pure_veg,\
            sports_bar_flag,has_bar,has_ac,has_dine_in,has_delivery,takeaway_flag,accepts_credit_cards,accepts_debit_cards,\
            sheesha_flag,halal_flag,has_wifi,has_live_music,nightlife_flag,stag_entry_flag,entry_fee,has_online_delivery,\
            min_order,average_delivery_time,delivery_charge,accepts_online_payment"


def updateExistingRestaurant(rest_details,rest_id):
	query = "UPDATE restaurants set 'name' = %s and 'url' = %s and 'address' = %s and 'latitude' = %s and 'longitude' = %s and 'rating' = %s and 'country_id' = %s and 'phone' = %s and 'timings' = %s and 'average_cost_for_two' = %s and 'is_pure_veg' = %s and 'sports_bar_flag' = %s and 'has_bar' = %s and 'has_ac' = %s and 'has_dine_in' = %s and 'has_delivery' = %s and 'takeaway_flag' = %s and 'accepts_credit_cards' = %s and 'accepts_debit_cards' = %s and 'sheesha_flag' = %s and 'halal_flag' = %s and 'has_wifi' = %s and 'has_live_music' = %s and 'nightlife_flag' = %s and 'stag_entry_flag' = %s and 'entry_fee' = %s and 'has_online_delivery' = %s and 'min_order' = %s and 'average_delivery_time' = %s and 'delivery_charge' = %s and 'accepts_online_payment' where restaurant_id = '" + str(rest_id) + "'"

	args = []
	for params in warehouse_restaurant_params:
		args.append(rest_details[params])

	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)
		conn.commit()

	except Error as error:
		print "Error: updateExistingRestaurant"
		print error

	finally:
		cursor.close()
		conn.close()

def insertNewRestaurant(rest_details):
	
	query = "INSERT INTO restaurants (" + warehouse_restaurant_arguments + ") " \
			"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

	args = []
	for params in warehouse_restaurant_params:
		args.append(str(rest_details[params]))

	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)
		conn.commit()

	except Error as error:
		print "Error: insertNewRestaurant"
		print error

	finally:
		# print "restaurant inserted"
		cursor.close()
		conn.close()

def findLastInsertedRestaurantId():
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT restaurant_id FROM restaurants ORDER BY restaurant_id desc LIMIT 1")

		row = cursor.fetchone()
		return row[0]
		# for row in rows:
		# 	print row

	except Error as error:
		print "Error: findLastInsertedRestaurantId"
		print error

	finally:
		cursor.close()
		conn.close()
