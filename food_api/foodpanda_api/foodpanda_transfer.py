from foodpanda_menu import findDishesByRestaurantId,findDishById
from foodpanda_menu_transfer import insertManyDishes,insertOneDish

dish_id = 0
while(1):
	data = findDishById(dish_id)
	if data:
		for dish in data:
			print dish_id
			insertOneDish(dish[1],dish[2],dish[3],dish[4],dish[5],)
		dish_id += 1000
	else:
		break
	