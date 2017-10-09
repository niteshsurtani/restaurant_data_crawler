from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config
from re import sub

def getCuisineFromRestaurantId(db_name,rest_id,restaurant_cuisine):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT cuisine_name FROM cuisine_restaurant WHERE restaurant_id = '" + str(rest_id) + "'")

		rows = cursor.fetchall()
		for row in rows:
			restaurant_cuisine.append(row[0])

	except Error as error:
		print "Error: getCuisineFromRestaurantId"
		print error

	finally:
		cursor.close()
		conn.close()


def getCuisineIdFromName(cuisine_name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT cuisine_id from cuisine WHERE cuisine_name = '" + cuisine_name + "'"

		cursor.execute(query)
		row = cursor.fetchone()
		if row == None:
			return -1
		return str(row[0])

	except Error as error:
		print "Error: getCuisineIdFromName"
		print error

	finally:
		cursor.close()
		conn.close()

# ================================================== #
def existRestaurantCuisine(restaurant_id,cuisine_id):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT cuisine_id from cuisine_restaurant WHERE cuisine_id = '" + str(cuisine_id) + "' and restaurant_id = '" + str(restaurant_id) + "'"

		cursor.execute(query)
		row = cursor.fetchone()
		if row != None:
			return 1
		return 0

	except Error as error:
		print "Error: existRestaurantCuisine"
		print error

	finally:
		cursor.close()
		conn.close()

def insertRestaurantCuisines(restaurant_id,cuisines):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		for cuisine in cuisines:
			cuisine = normalizeName(cuisine)
			cuisine_id = getCuisineIdFromName(cuisine)

			if not existRestaurantCuisine(restaurant_id,cuisine_id):
				query = "INSERT INTO cuisine_restaurant (restaurant_id,cuisine_id) " \
					"VALUES (%s,%s)"

				args = [str(restaurant_id),str(cuisine_id)]

				cursor.execute(query, args)
			else:
				print "Cuisine exists"
		conn.commit()

	except Error as error:
		print "Error: insertRestaurantCuisines"
		print error

	finally:
		cursor.close()
		conn.close()
# ================================================== #


def getAllCuisine(db_name):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT cuisine_name from cuisine"

		cursor.execute(query)

		rows = cursor.fetchall()
		if rows == None:
			rows = []
		return rows

	except Error as error:
		print "Error: getAllCuisine"
		print error

	finally:
		cursor.close()
		conn.close()


# ================================================== #
def existCuisine(cuisine_name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT cuisine_id from cuisine WHERE cuisine_name = '" + cuisine_name + "'"

		cursor.execute(query)
		row = cursor.fetchone()
		if row != None:
			return 1
		return 0

	except Error as error:
		print "Error: existCuisine"
		print error

	finally:
		cursor.close()
		conn.close()


def normalizeName(name):
	name = sub(r"\(.*?\)","",name)
	tokens = name.split(",")
	name = tokens [0]
	strip_string = ''.join(e for e in name if e.isalnum() or e.isspace())
	strip_string = strip_string.strip()
	strip_string = strip_string.lower()
	return strip_string

def insertCuisine(cuisines):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()

		for cuisine in cuisines:
			cuisine = normalizeName(str(cuisine[0]))
			if not existCuisine(cuisine):
				query = "INSERT INTO cuisine (cuisine_name) " \
					"VALUES (%s)"
				args = [cuisine]
				cursor.execute(query, args)
				conn.commit()

	except Error as error:
		print "Error: insertCuisine"
		print error

	finally:
		cursor.close()
		conn.close()

# ================================================== #
