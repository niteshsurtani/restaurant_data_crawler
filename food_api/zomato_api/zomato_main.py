from city import *
from restaurant import *
from menu import *
from cuisine_list import *

insertAllCuisines()
print " ======================== Cuisines inserted ============================ "

# Inserts all cities and localities
# insertAllCitiesAndLocalities()

print " ======================== Cities and Localities inserted ============================ "

# Insert all restaurants, their localities and cuisines
insertAllRestaurants()

print " ======================== Restaurants inserted ============================ "

# Insert menus
insertMenus()