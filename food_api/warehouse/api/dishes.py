from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config
from re import sub

def getDishesFromRestaurantId(db_name,rest_id):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT DISTINCT dish_name, cost, type FROM menu WHERE restaurant_id = '" + str(rest_id) + "'")

		rows = cursor.fetchall()
		return rows

	except Error as error:
		print "Error: getDishesFromRestaurantId"
		print error

	finally:
		cursor.close()
		conn.close()


def getDishIdFromName(dish_name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT dish_id from dish WHERE dish_name = '" + dish_name + "'"

		cursor.execute(query)
		row = cursor.fetchone()
		return row[0]

	except Error as error:
		print "Error: getDishIdFromName"
		print error

	finally:
		cursor.close()
		conn.close()

def getAllDish(db_name):
	if db_name == "foodpanda":
		try:
			db_config = read_db_config()
			db_config['database'] = db_name
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			query = "SELECT dish_name from dish"

			cursor.execute(query)
			
			rows = cursor.fetchall()
			if rows == None:
				rows = []
			return rows

		except Error as error:
			print "Error: getAllDish"
			print error

		finally:
			cursor.close()
			conn.close()
	else:
		return []

def existDish(dish_name):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT dish_id from dish WHERE dish_name = '" + dish_name + "'"

		cursor.execute(query)
		row = cursor.fetchone()
		if row != None:
			return 1
		return 0

	except Error as error:
		print "Error: existDish"
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

def insertDish(dishes):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()

		for dish in dishes:
			dish = normalizeName(str(dish[0]))
			if not existDish(dish):
				query = "INSERT INTO dish (dish_name) " \
					"VALUES (%s)"
				args = [dish]
				cursor.execute(query, args)
				conn.commit()

	except Error as error:
		print "Error: insertDish"
		print error

	finally:
		cursor.close()
		conn.close()

def existMenu(restaurant_id,dish_id):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		query = "SELECT dish_id from menu WHERE dish_id = '" + str(dish_id) + "' and restaurant_id = '" + str(restaurant_id) + "'"

		cursor.execute(query)
		row = cursor.fetchone()
		if row != None:
			return 1
		return 0

	except Error as error:
		print "Error: existMenu"
		print error

	finally:
		cursor.close()
		conn.close()

def insertDishes(restaurant_id,dishes):
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		for dish in dishes:
			dish_name = str(dish[0])
			dish_cost = str(dish[1])
			dish_type = str(dish[2])

			dish_name = normalizeName(dish_name)
			dish_id = getDishIdFromName(dish_name)
			if not existMenu(restaurant_id,dish_id):
				# Insert Menu
				query = "INSERT INTO menu (restaurant_id,dish_id,cost,type) " \
					"VALUES (%s,%s,%s,%s)"

				args = [restaurant_id,dish_id,dish_cost,dish_type]
				cursor.execute(query, args)
			else:
				# Update Menu
				query = "UPDATE menu set cost = " + dish_cost + " and type = '" + dish_type + "' where restaurant_id =%s and dish_id =%s"
				args = [str(restaurant_id),str(dish_id)]
				cursor.execute(query, args)
				
		conn.commit()

	except Error as error:
		print "Error: insertDishes"
		print error

	finally:
		cursor.close()
		conn.close()
