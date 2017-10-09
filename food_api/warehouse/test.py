from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config

def getCityMappingByName(db_name,city):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT word FROM city_mapping where mapping = '"+city+"'")

		row = cursor.fetchall()
		# print row
		return row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def getMappingCityLocalities(db_name,city_id,localities):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT locality_id, name FROM locality where city_id = '"+ str(city_id) +"'")

		rows = cursor.fetchall()
		for row in rows:
			localities[row[0]] = str(row[1])
		# print row
		return rows

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
# getAllCities("zomato")

def getLocalityById(db_name,locality_id):
	try:
		db_config = read_db_config()
		db_config['database'] = db_name
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM locality where locality_id = '" + locality_id + "'")

		row = cursor.fetchone()
		if(row == None):
			return None
		return row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
# getAllCities("zomato")

def insertLocality(name,city_id,lat,lon):
	print "here 1"
	query = "INSERT INTO locality (name, city_id, latitude, longitude) " \
			"VALUES(%s,%d,%f,%f)"

	args = (name, city_id, lat, lon)

	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)
		print "here 2"
		cursor = conn.cursor()
		print "here 3"
		cursor.execute(query, args)
		print "here 4"
		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

insertLocality("a",1,3.3,343.2)

def findLastInsertedLocalityId():
	try:
		db_config = read_db_config()
		db_config['database'] = "warehouse"
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT locality_id FROM locality ORDER BY locality_id desc LIMIT 1")

		rows = cursor.fetchone()
		return row[0]
		# for row in rows:
		# 	print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
