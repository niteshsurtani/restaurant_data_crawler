from zomato_city import *
from zomato_locality import *
from zomato_city import insertManyCities,findAllCities,findCityByName,findLastInsertedCityId,findCityIdByName
from zomato_locality import insertManyLocalities,findIdOfLocality
import subprocess
import os
import ast
from pprint import pprint


def insertAllCitiesAndLocalities():
	LocalitiesDetails = []
	CitiesDetails = []
	zoneDict = {}

	for cityId in range(1,40):
		try:
			curlCall = "curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v2/subzones.json?city_id=%s'" % (str(cityId))
			locationData = subprocess.check_output(curlCall,shell=True) 
			dictLocationData = ast.literal_eval(locationData)
			subzonesDict = dictLocationData["subzones"]

			for subzones in subzonesDict:
				cityTuple = (subzones['subzone']['city_id'],subzones['subzone']['city_name'],)	
				if not existCity(cityTuple[1]):
					insertManyCities((cityTuple,))
				
				LocaTuple = (subzones['subzone']['id'] ,subzones['subzone']['name'], getCityByName(subzones['subzone']['city_name']), subzones['subzone']['latitude'], subzones['subzone']['longitude'],)
				if not findIdOfLocality(LocaTuple[0]):
					insertManyLocalities((LocaTuple,))

		except:
			print "error"
