from urllib2 import Request, urlopen, URLError
import re
# from errorhandler import typec

# def restaurantInfo():
#
from zomato_cuisine_restaurant import insertManyCuisines
from zomato_locality import getAllIdsOfLocality
from zomato_restaurant import insertManyRestaurants,getAllRestaurantsLocalityId
from zomato_location_restaurant import insertManyLocalityRestaurants
import subprocess
import os
import ast
from pprint import pprint
import json


start = 0
curlCall = "curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v2/search.json?subzone_id=5401'"
restaurantData = subprocess.check_output(curlCall,shell=True) 

dictRestaurantData = json.loads(restaurantData)
results_found = dictRestaurantData['results_found']
while start<results_found:
	curlCall = "curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v2/search.json?subzone_id=5401&start=%s&count=50'" % (start)
	restaurantData = subprocess.check_output(curlCall,shell=True)
	dictRestaurantData = json.loads(restaurantData)
	listOfRestraunt = (dictRestaurantData['restaurants'])
	listOfRestrauntDetails = []
	start += 50

	for restaurant in listOfRestraunt:	

		print restaurant['restaurant']['name']