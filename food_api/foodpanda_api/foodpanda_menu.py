from mysql.connector import MySQLConnection, Error
from foodpanda_dbconfig import read_db_config

def insertOneDish(restaurant_id, dish_name, type, cost, data_resource):
	query = "INSERT INTO menus(restaurant_id, dish_name, cost, type, data_resource) " \
			"VALUES(%s, %s, %s, %s, %s)"

	args = (restaurant_id, dish_name, cost, type, data_resource)

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
	query = "INSERT INTO menus(restaurant_id, dish_name, type, cost, data_resource) " \
			"VALUES(%s, %s, %s, %s, %s)"

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
		cursor.execute("SELECT * FROM menus where dish_id = " + id)

		row = cursor.fetchone()
		print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findDishesByRestaurantId(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM menus where restaurant_id = " + id)

		rows = cursor.fetchall()
		for row in rows:
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
		cursor.execute("SELECT * FROM menus WHERE dish_name LIKE '%s'" % query)

		rows = cursor.fetchall()
		for row in rows:
			print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def findDistinctDishByName():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT DISTINCT `dish_name` FROM `menus`")

		rows = cursor.fetchall()
		# for row in rows:
		# 	print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
def updateMenuId(id,dishName):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "UPDATE `menus` SET dish_id = %s WHERE dish_name = " % (id)
		query += "'" + dishName + "'"
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