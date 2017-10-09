from mysql.connector import MySQLConnection, Error
from zomato_dbconfig import read_db_config

def insertOneCuisine(cuisine_name):
	query = "INSERT INTO cuisine(cuisine_name) " \
			"VALUES(%s)"

	args = (cuisine_name)

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



def insertManyCuisines(cuisine_info):
	query = "INSERT INTO cuisine (cuisine_id,cuisine_name) " \
			"VALUES (%s,%s)"

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
		# print "CUISINE_RESTAURANT DATA INSERTED!!!"



def findCuisinesByCuisineId(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM cuisine where cuisine_id = " + id)

		rows = cursor.fetchall()
		for row in rows:
			print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findCuisineByName(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if query: 
			query = "%" + query + "%"
		cursor.execute("SELECT * FROM cuisine WHERE cuisine_name LIKE '%s'" % query)

		rows = cursor.fetchall()
		for row in rows:
			print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()


def loadAllCuisines():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT cuisine_id, cuisine_name FROM cuisine")

		cuisine = {}
		rows = cursor.fetchall()
		for row in rows:
			cuisine[row[1]] = row[0]

		return cuisine
	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findAllCuisines():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM cuisine")

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
