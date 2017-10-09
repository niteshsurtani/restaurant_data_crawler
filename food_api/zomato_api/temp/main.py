import subprocess
import os
import ast

# x = subprocess.check_output("curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v1/subzones.json?city_id=34'",shell=True)
# y = ast.literal_eval(x)
# # for i in y["results"]:
# # 	print i
# for i in y['subzones']:
# 	print i
locationData = subprocess.check_output("curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v1/subzones.json?city_id=34'",shell=True)
dictLocationData = ast.literal_eval(locationData)
# for i in y["results"]:
# 	print i
for subzones in dictLocationData['subzones']:
	# print ast.literal_eval(subzones["subzone"])
	print subzones['subzone']['name']
