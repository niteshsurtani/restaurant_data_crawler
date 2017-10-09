from zomato_cuisine_restaurant import findDistinctCuisineNames,updateCuisineId,findCuisineByName,findCuisinesByRestaurantId
from zomato_cuisine import findAllCuisines

listOfCuisineNames = findDistinctCuisineNames()
listOfCuisnieId = findAllCuisines()

for i in listOfCuisnieId:
 	listOfResId = []
 	for j in findCuisineByName(i[1]): 		
 		updateCuisineId(i[0],j[0])
 		break
# for cuisine in listOfCuisineNames:
# 	insertManyCuisines([cuisine])