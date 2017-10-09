from foodpanda_menu import findDistinctDishByName,updateMenuId
from foodpanda_dish  import insertManyDishes,findAllDishes
# from foodpanda_menu import updateMenuId

# for i in findDistinctDishByName():
# 	insertManyDishes([i])
for i in findAllDishes():
	if i[0]>6300:
		updateMenuId(i[0],str(i[1]))
