from foodpanda_cuisine_restaurant import findDistinctCuisineNames,updateCuisineId,findCuisineByName
from foodpanda_cuisine import insertManyCuisines,findAllCuisines

listOfCuisineNames = findDistinctCuisineNames()
listOfCuisnieId = findAllCuisines()

for i in listOfCuisnieId:
 	listOfResId = []
 	for j in findCuisineByName(i[1]):
 		print j[1]
 		updateCuisineId(i[0],j[1])
 		break
# for cuisine in listOfCuisineNames:
# 	insertManyCuisines([cuisine])