from mysql.connector import MySQLConnection, Error
from zomato_dbconfig import read_db_config

def insertOneRestaurant(restaurant_id,name,url,address,latitude,longitude,rating,country_id,phone,timings,average_cost_for_two,is_pure_veg,\
			sports_bar_flag,has_bar,has_ac,has_dine_in,has_delivery,takeaway_flag,accepts_credit_cards,accepts_debit_cards,\
			sheesha_flag,halal_flag,has_wifi,has_live_music,nightlife_flag,stag_entry_flag,entry_fee,has_online_delivery,\
			min_order,average_delivery_time,delivery_charge,accepts_online_payment,):
	query = "INSERT INTO restaurants(restaurant_id,name,url,address,latitude,longitude,rating,country_id,phone,timings,average_cost_for_two,is_pure_veg,\
			sports_bar_flag,has_bar,has_ac,has_dine_in,has_delivery,takeaway_flag,accepts_credit_cards,accepts_debit_cards,\
			sheesha_flag,halal_flag,has_wifi,has_live_music,nightlife_flag,stag_entry_flag,entry_fee,has_online_delivery,\
			min_order,average_delivery_time,delivery_charge,accepts_online_payment,) "\
			"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"

	args = (restaurant_id,name,url,address,locality_id,latitude,longitude,rating,country_id,phone,timings,average_cost_for_two,is_pure_veg,\
			sports_bar_flag,has_bar,has_ac,has_dine_in,has_delivery,takeaway_flag,accepts_credit_cards,accepts_debit_cards,\
			sheesha_flag,halal_flag,has_wifi,has_live_music,nightlife_flag,stag_entry_flag,entry_fee,has_online_delivery,\
			min_order,average_delivery_time,delivery_charge,accepts_online_payment,)

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		# print "RESTAURANT DATA INSERTED!!!"

def insertManyRestaurants(restaurants_info):
	query = "INSERT INTO restaurants(restaurant_id,name,url,address,latitude,longitude,rating,country_id,phone,timings,average_cost_for_two,is_pure_veg,\
			sports_bar_flag,has_bar,has_ac,has_dine_in,has_delivery,takeaway_flag,accepts_credit_cards,accepts_debit_cards,\
			sheesha_flag,halal_flag,has_wifi,has_live_music,nightlife_flag,stag_entry_flag,entry_fee,has_online_delivery,\
			min_order,average_delivery_time,delivery_charge,accepts_online_payment)" \
			"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, restaurants_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		# print "RESTAURANT DATA INSERTED!!!"

def findRestaurantById(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM restaurants where restaurant_id = " + id)

		row = cursor.fetchone()
		print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findRestaurantByName(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if query: 
			query = "%" + query + "%"
		cursor.execute("SELECT * FROM restaurants WHERE name LIKE '%s'" % query)

		rows = cursor.fetchall()
		for row in rows:
			print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def getAllRestaurantsIdAndUrl():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT restaurant_id,url FROM restaurants")

		row = cursor.fetchall()
		return row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def getAllRestaurantsLocalityId():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT DISTINCT locality_id FROM restaurants")

		row = cursor.fetchall()
		return row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def findRestaurantIds():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT DISTINCT restaurant_id FROM restaurants")

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def existRestaurant(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM restaurants WHERE restaurant_id = '" + str(query) + "'")

		rows = cursor.fetchone()
		if rows != None:
			return 1
		return 0

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
