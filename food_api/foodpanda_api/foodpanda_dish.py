from mysql.connector import MySQLConnection, Error
from foodpanda_dbconfig import read_db_config

def insertOneDish(dish_name):
	query = "INSERT INTO dish(dish_name) " \
			"VALUES(%s)"

	args = (dish_name)

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
		print "DISHES DATA INSERTED!!!"

def insertManyDishes(menu_info):
	query = "INSERT INTO dish(dish_name) " \
			"VALUES(%s)"

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, menu_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		print "DISHES DATA INSERTED!!!"

def findDishById(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM dish where dish_id = " + id)

		row = cursor.fetchone()
		print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findDishByName(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if query: 
			query = "%" + query + "%"
		cursor.execute("SELECT * FROM dish WHERE dish_name LIKE '%s'" % query)

		rows = cursor.fetchall()
		for row in rows:
			print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def findAllDishes():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM dish")

		row = cursor.fetchall()
		return row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()	
