from restaurant_url import crawlRestaurants
from zomato_restaurant import getAllRestaurantsIdAndUrl,getAllRestaurantsLocalityId
from zomato_menu import insertManyDishes,findDistinctRestaurantIds
from zomato_locality import getAllIdsOfLocality

def insertMenus():
	listOfAllRestaurantUrlAndId =  getAllRestaurantsIdAndUrl()
	listOfMenus = {}

	for resId in listOfAllRestaurantUrlAndId:
		if resId[1] != '0':
			if (resId[0],) not in findDistinctRestaurantIds():
				for menu in crawlRestaurants(resId[1]):
					insertManyDishes([(menu,resId[0],)])
