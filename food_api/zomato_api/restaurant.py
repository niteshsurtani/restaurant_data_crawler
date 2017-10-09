# from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re
# from errorhandler import typec

# def restaurantInfo():
#
from zomato_cuisine import *
from zomato_cuisine_restaurant import *
from zomato_locality import *
from zomato_restaurant import *
from zomato_location_restaurant import *
import subprocess
import os
import ast
from pprint import pprint
import json


def assignValueToAttributesOfRestaurants(restaurantData,id):

	try:
		resId = restaurantData["restaurant"]["id"]

	except:
		resId = "0"
	
	try:
		name = str(restaurantData["restaurant"]["name"])
	except:
		name = "0"
    
	try:
		url = str(restaurantData["restaurant"]["url"])
	except:
		url = "0"
    
	try:
		address = str(restaurantData["restaurant"]["location"]["address"])
	except:
		address = "0"
	
	try:
		latitude = float(restaurantData["restaurant"]["location"]["latitude"])
	except:
		latitude = "0"
	
	try:
		longitude = float(restaurantData["restaurant"]["location"]["longitude"])
	except:
		longitude = "0"

	try:
		rating = float(restaurantData["restaurant"]["user_rating"]["aggregate_rating"])
	except:
		rating = "0"
	
	try:
		country_id = restaurantData["restaurant"]["location"]["country_id"]
	except:
		country_id = "0"
    
	try:
		phone = str(restaurantData["restaurant"]["phone"])
	except:
		phone = "0"

	try:
		if mobile_phone_display not in phone:
			phone += ","+ str(restaurantData["restaurant"]["mobile_phone_display"])
	except:
		mobile_phone_display = "0"

	try:
		if mobile_phone not in phone:
			phone += "," + str(restaurantData["restaurant"]["mobile_phone"])
	except:
		mobile_phone = "0"
    
	try:
		timings = str(restaurantData["restaurant"]["timings"])
	except:
		timings = "0"
    
	try:
		average_cost_for_two = float(restaurantData["restaurant"]["average_cost_for_two"])
	except:
		average_cost_for_two = "0"
    
	try:
		is_pure_veg = str(restaurantData["restaurant"]["is_pure_veg"])
	except:
		is_pure_veg = "0"
	

	try:
		sports_bar_flag = str(restaurantData["restaurant"]["sports_bar_flag"])
	except:
		sports_bar_flag = "0"
	
	try:
		has_bar = str(restaurantData["restaurant"]["has_bar"])
	except:
		has_bar = "0"
	
	try:
		has_ac = str(restaurantData["restaurant"]["has_ac"])
	except:
		has_ac = "0"
	
	try:
		has_dine_in = str(restaurantData["restaurant"]["has_dine_in"])
	except:
		has_dine_in = "0"
	
	try:
		has_delivery = str(restaurantData["restaurant"]["has_delivery"])
	except:
		has_delivery = "0"
	
	try:
		takeaway_flag = str(restaurantData["restaurant"]["takeaway_flag"])
	except:
		takeaway_flag = "0"

	try:
		accepts_credit_cards = str(restaurantData["restaurant"]["accepts_credit_cards"])
	except:
		accepts_credit_cards = "0" 
    
	try:
		accepts_debit_cards = str(restaurantData["restaurant"]["accepts_debit_cards"])
	except:
		accepts_debit_cards = "0"
    
	try:
		sheesha_flag = str(restaurantData["restaurant"]["sheesha_flag"])
	except:
		sheesha_flag = "0"
    
	try:
		halal_flag = str(restaurantData["restaurant"]["halal_flag"])
	except:
		halal_flag = "0"
    
	try:
		has_wifi = str(restaurantData["restaurant"]["has_wifi"])
	except:
		has_wifi = "0"

	try:
		has_live_music = str(restaurantData["restaurant"]["has_live_music"])
	except:
		has_live_music = "0"
    
	try:
		nightlife_flag = str(restaurantData["restaurant"]["nightlife_flag"])
	except:
		nightlife_flag = "0"
    
	try:
		stag_entry_flag = str(restaurantData["restaurant"]["stag_entry_flag"])
	except:
		stag_entry_flag = "0"
    
	try:
		entry_fee = str(restaurantData["restaurant"]["takeaway_flag"])
	except:
		entry_fee = "0"

	try:
		has_online_delivery = str(restaurantData["restaurant"]["has_online_delivery"])
	except:
		has_online_delivery = "0"
	
	try:
		min_order = str(restaurantData["restaurant"]["min_order"])
	except:
		min_order = "0"
	
	try:
		average_delivery_time = str(restaurantData["restaurant"]["average_delivery_time"])
	except:
		average_delivery_time = "0"
	
	try:
		delivery_charge = str(restaurantData["restaurant"]["delivery_charge"])
	except:
		delivery_charge = "0"
	
	try:
		accepts_online_payment = str(restaurantData["restaurant"]["accepts_online_payment"])
	except:
		accepts_online_payment = "0"

	return (resId,name,url,address,latitude,longitude,rating,country_id,phone,timings,average_cost_for_two,is_pure_veg,\
			sports_bar_flag,has_bar,has_ac,has_dine_in,has_delivery,takeaway_flag,accepts_credit_cards,accepts_debit_cards,\
			sheesha_flag,halal_flag,has_wifi,has_live_music,nightlife_flag,stag_entry_flag,entry_fee,has_online_delivery,\
			min_order,average_delivery_time,delivery_charge,accepts_online_payment,)

def insertAllRestaurants():
	count = 0

	cuisine_list = loadAllCuisines()
	for id in getAllIdsOfLocality():
		# if (id[0],) not in getAllRestaurantsLocalityId() and id[0]>299:
		start = 0
		curlCall = "curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v2/search.json?subzone_id=%s'" % (id[0])
		restaurantData = subprocess.check_output(curlCall,shell=True) 

		try:

			dictRestaurantData = json.loads(restaurantData)
			results_found = dictRestaurantData['results_found']
			while start<results_found:
				curlCall = "curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v2/search.json?subzone_id=%s&start=%s&count=50'" % (id[0],start)
				restaurantData = subprocess.check_output(curlCall,shell=True)
				dictRestaurantData = json.loads(restaurantData)
				listOfRestraunt = (dictRestaurantData['restaurants'])
					
				start += 50
				for restaurant in listOfRestraunt:
					if not existRestaurant(restaurant["restaurant"]["id"]):
						insertManyRestaurants([assignValueToAttributesOfRestaurants(restaurant,id)])

					print "restaurant insert"
					if not existRestaurantLocality(id[0],str(restaurant["restaurant"]["id"]),):
						insertManyLocalityRestaurants([(id[0],restaurant["restaurant"]["id"],)])
					print "restaurant locality insert"
					
					cuisines = restaurant["restaurant"]["cuisines"].split(",")
					for cuisine in cuisines:
						if cuisine != '':
							insertManyCuisinesRestaurant([(restaurant["restaurant"]["id"],cuisine_list[cuisine.strip()],)])
					print "restaurant cuisine insert"
			        
			        # listOfCuisines.append(restaurant["restaurant"]["cuisines"])
				count += 1
				# print len(listOfRestrauntDetails)
				# print len(listOfCuisines)
				# for cuisineDetail in listOfCuisines:
				# 	print cuisineDetail
				# 	insertManyCuisines([cuisineDetail])
				# for resDetails in listOfRestrauntDetails:
				# 	print [resDetails]
				# 	insertManyRestaurants([resDetails])
				# for locationAndRestaurantId in listOfRestrauntAndLocalityIds:
				# 	print [locationAndRestaurantId]
				# 	insertManyLocalityRestaurants([locationAndRestaurantId])
					
		except Error as error:
			print error
