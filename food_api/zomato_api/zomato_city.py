from mysql.connector import MySQLConnection, Error
from zomato_dbconfig import read_db_config

def insertOneCity(zone_id,name):
	query = "INSERT INTO city(zone_id, name) " \
			"VALUES( %s, %s)"
	args = (zone_id, name)

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
		print "CITY DATA INSERTED!!!"

def insertManyCities(city_info):
	query = "INSERT INTO city(zone_id, name) " \
			"VALUES( %s, %s)"

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.executemany(query, city_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		print "CITY DATA INSERTED!!!"

# def updateManyCities(city_info):
# 	query = "UPDATE city set base_city_name = (%s) WHERE city_id = (%s) "

# 	try:
# 		db_config = read_db_config()
# 		conn = MySQLConnection(**db_config)
# 		cursor = conn.cursor()
# 		cursor.executemany(query, city_info)

# 		conn.commit()

# 	except Error as error:
# 		print error

# 	finally:
# 		cursor.close()
# 		conn.close()
# 		print "CITY DATA INSERTED!!!"

def findCityById(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM city WHERE city_id = " + id)

		row = cursor.fetchone()
		print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findAllCities():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM city")

		rows = cursor.fetchall()
		return rows
		# for row in rows:
		# 	print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def existCity(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM city WHERE name = '" + query + "'")

		rows = cursor.fetchone()
		if rows != None:
			return 1
		return 0

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		
def getCityByName(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM city WHERE name = '" + query + "'")

		rows = cursor.fetchone()
		if rows != None:
			return rows[0]
		return -1

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findCityIdByName(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if query: 
			query = "%" + query + "%"
		cursor.execute("SELECT city_id FROM city WHERE name LIKE '%s'" % query)

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()		

def findLastInsertedCityId():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT city_id FROM city ORDER BY city_id desc LIMIT 1")

		rows = cursor.fetchall()
		return rows
		# for row in rows:
		# 	print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

