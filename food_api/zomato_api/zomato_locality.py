from mysql.connector import MySQLConnection, Error
from zomato_dbconfig import read_db_config

def insertOneLocality(locality_id,name, city_id, latitude, longitude):
	query = "INSERT INTO locations(locality_id,name, city_id, latitude, longitude) " \
			"VALUES(%s, %s, %s, %s, %s)"

	args = (locality_id,name, city_id, latitude, longitude)

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
		# print "LOCALITY DATA INSERTED!!!"

def insertManyLocalities(locality_info):
	# Already Exist Locality
	query = "INSERT INTO locality (locality_id,name, city_id, latitude, longitude) " \
			"VALUES(%s,%s, %s, %s, %s)"

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, locality_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		# print "LOCALITY DATA INSERTED!!!"

def findLocalityById(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM locations where locality_id = " + id)

		row = cursor.fetchone()
		# print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findLocalitiesByZoneId(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM locations where city_id = " + id)

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		
	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findLocalityByName(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if query: 
			query = "%" + query + "%"
		cursor.execute("SELECT * FROM locations WHERE name LIKE '%s'" % query)

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def getAllIdsOfLocality():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM locality")

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()


def findIdOfLocality(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM locality WHERE locality_id = '" + str(query) + "'")

		rows = cursor.fetchone()
		if rows != None:
			return 1
		return 0

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

