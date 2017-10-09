from urllib2 import Request, urlopen, URLError
import re
# from errorhandler import typec

# def restaurantInfo():
#
# from zomato_cuisine_restaurant import *

from zomato_cuisine import *
import subprocess
import os
import ast
from pprint import pprint
import json

def insertAllCuisines():
	try:
		curlCall = "curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v1/cuisines.json'"
		cuisineData = subprocess.check_output(curlCall,shell=True)
		cuisineData = json.loads(cuisineData)

		cuisines = cuisineData['cuisines']
		for cuisine in cuisines:
			cuisineTuple = (cuisine['cuisine']['cuisine_id'],cuisine['cuisine']['cuisine_name'],)

			insertManyCuisines((cuisineTuple,))
	except:
		print "error"
