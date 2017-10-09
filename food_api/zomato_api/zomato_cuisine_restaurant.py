from mysql.connector import MySQLConnection, Error
from zomato_dbconfig import read_db_config

def insertOneCuisine(restaurant_id, cuisine_id):
	query = "INSERT INTO cuisine_restaurant(restaurant_id, cuisine_id) " \
			"VALUES(%s, %s)"

	args = (restaurant_id, cuisine_id)

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
		print "CUISINE_RESTAURANT DATA INSERTED!!!"

def insertManyCuisinesRestaurant(cuisine_info):
	query = "INSERT INTO cuisine_restaurant(restaurant_id, cuisine_id) " \
			"VALUES(%s, %s)"

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, cuisine_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		print "CUISINE_RESTAURANT DATA INSERTED!!!"

def findCuisinesByRestaurantId(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM cuisine_restaurant where restaurant_id = " + id)

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findCuisineById(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM cuisine_restaurant WHERE cuisine_id=%s" % id)

		rows = cursor.fetchall()
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findDistinctRestaurantIds():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT DISTINCT restaurant_id FROM cuisine_restaurant")

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def findDistinctCuisineNames():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT DISTINCT cuisine_name FROM cuisine_restaurant")

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def updateCuisineId(id,cuisine_name):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "UPDATE `cuisine_restaurant` SET cuisine_id = %s WHERE cuisine_name =" % (id)
		query += "'" + cuisine_name + "'"
		print query
		cursor.execute(query)
		conn.commit()

		# rows = cursor.fetchall()
		# for row in rows:
		# 	print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()	
		print "Updated!!!"