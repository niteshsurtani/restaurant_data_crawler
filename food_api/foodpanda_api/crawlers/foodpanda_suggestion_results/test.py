cityid= 11
comb = "ac"
f= open("c","w")
# combinations = []
# temp = f.read().strip().split('\n')
# temp.pop(0)
# for item in temp:
# 	item = item.split(" ")
# 	if int(item[1]) >= 10:
# 		combinations.append(item[0])
# f.close()
# print combinations
f.write("cityId: %s, " % (cityid))
f.write("combination: %s\n" % (comb))
f.close()