from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config

def getCityMappingByName(db_name,city):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT word FROM city_mapping where mapping = '"+city+"'")

		row = cursor.fetchall()
		# print row
		return row

	except Error as error:
		print "Error: getCityMappingByName"
		print error

	finally:
		cursor.close()
		conn.close()

def existLocality(city_id,locality_name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT locality_id FROM locality where city_id = '"+str(city_id)+"' and name ='"+locality_name+"'")

		row = cursor.fetchone()
		if(row == None):
			return 0
		else:
			return 1
		# print row

	except Error as error:
		print "Error: existLocality"
		print error

	finally:
		cursor.close()
		conn.close()

def getMappingCityLocalities(db_name,city_id,localities):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT locality_id, name FROM locality where city_id = '"+ str(city_id) +"'")

		rows = cursor.fetchall()
		for row in rows:
			localities[row[0]] = str(row[1])
		# print row
		return rows

	except Error as error:
		print "Error: getMappingCityLocalities"
		print error

	finally:
		cursor.close()
		conn.close()
# getAllCities("zomato")

def getLocalityId(name,city_id):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT locality_id FROM locality where name = '" + name + "' and city_id = '" + str(city_id) + "'")

		row = cursor.fetchone()
		return row[0]

	except Error as error:
		print "Error: getLocalityId"
		print error

	finally:
		cursor.close()
		conn.close()

def getLocalityById(db_name,locality_id):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM locality where locality_id = '" + str(locality_id) + "'")

		row = cursor.fetchone()
		if(row == None):
			return None
		return row

	except Error as error:
		print "Error: getLocalityById"
		print error

	finally:
		cursor.close()
		conn.close()
# getAllCities("zomato")

def insertLocality(name,city_id,lat,lon):
	query = "INSERT INTO locality (name, city_id, latitude, longitude) " \
			"VALUES (%s,%s,%s,%s)"

	args = (name, city_id, lat, lon)

	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)
		conn.commit()

	except Error as error:
		print "Error: insertLocality"
		print error

	finally:
		cursor.close()
		conn.close()

#insertLocality("a",1,3.3,43.2)

def findLastInsertedLocalityId():
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT locality_id FROM locality ORDER BY locality_id desc LIMIT 1")

		row = cursor.fetchone()
		return row[0]
		# for row in rows:
		# 	print row

	except Error as error:
		print "Error: findLastInsertedLocalityId"
		print error

	finally:
		cursor.close()
		conn.close()

def getLocalityFromRestaurantId(db_name,rest_id,restaurant_locality):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT name FROM locality, locality_restaurant WHERE restaurant_id = '" + str(rest_id) + "' and locality.locality_id = locality_restaurant.locality_id")

		rows = cursor.fetchall()
		for row in rows:
			restaurant_locality.append(row[0])

	except Error as error:
		print "Error: getLocalityFromRestaurantId"
		print error

	finally:
		cursor.close()
		conn.close()

def existRestaurantLocality(restaurant_id,locality_id):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT locality_id from locality_restaurant WHERE locality_id = " + str(locality_id) + " and restaurant_id = " + str(restaurant_id)

		cursor.execute(query)
		row = cursor.fetchone()
		if row != None:
			return 1
		return 0

	except Error as error:
		print "Error: existRestaurantLocality"
		print error

	finally:
		cursor.close()
		conn.close()


def getLocalityIdFromName(name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT locality_id FROM locality where name = '" + name + "'")

		row = cursor.fetchone()
		if row == None:
			return -1
		return row[0]

	except Error as error:
		print "Error: getLocalityById"
		print error

	finally:
		cursor.close()
		conn.close()

def insertRestaurantLocality(restaurant_id,locality_id):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if not existRestaurantLocality(restaurant_id,locality_id):
			query = "INSERT INTO locality_restaurant (restaurant_id,locality_id) " \
				"VALUES (%s,%s)"

			args = [str(restaurant_id),str(locality_id)]

			cursor.execute(query, args)
			conn.commit()

	except Error as error:
		print "Error: insertRestaurantLocalities"
		print error

	finally:
		cursor.close()
		conn.close()

# def insertRestaurantLocalities(restaurant_id,localities):
# 	try:
# 		db_config = read_db_config()
# 		db_config['database'] = "warehouse"
# 		conn = MySQLConnection(**db_config)

# 		cursor = conn.cursor()
# 		for locality in localities:
# 			# print "here"
# 			# print locality
# 			locality_id = getLocalityIdFromName(locality)
# 			# print "here"
# 			# print locality_id
# 			if not existRestaurantLocality(restaurant_id,locality_id):
# 				query = "INSERT INTO locality_restaurant (restaurant_id,locality_id) " \
# 					"VALUES (%s,%s)"

# 				args = [str(restaurant_id),str(locality_id)]

# 				cursor.execute(query, args)
# 				conn.commit()

# 	except Error as error:
# 		print "Error: insertRestaurantLocalities"
# 		print error

# 	finally:
# 		cursor.close()
# 		conn.close()
