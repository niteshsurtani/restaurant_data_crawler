from mysql.connector import MySQLConnection, Error
from zomato_dbconfig import read_db_config

def insertOneDish(menu,restaurant_id):
	query = "INSERT INTO menus(menu,restaurant_id) " \
			"VALUES(%s, %s)"

	args = (menu,restaurant_id)

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
	query = "INSERT INTO menus(menu,restaurant_id) " \
			"VALUES(%s, %s)"

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
'''
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
'''

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

def findDistinctRestaurantIds():
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT DISTINCT restaurant_id FROM menus")

		rows = cursor.fetchall()
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
'''
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

		conn.close()'''	