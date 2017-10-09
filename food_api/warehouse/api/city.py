from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config

def getAllCities(db_name):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT city_id,name FROM city")

		row = cursor.fetchall()
		# print row
		return row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def getCityByName(db_name,city):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT city_id FROM city where name = '" + city + "'")

		row = cursor.fetchone()
		if(row == None):
			return None
		return row[0]

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
# getAllCities("zomato")
