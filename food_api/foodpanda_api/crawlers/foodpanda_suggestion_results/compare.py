import operator

files = ['pune','bangalore','chennai','delhi']
total = {}
c = 0
for file in files:
	fr = open(file,'r')
	lines = fr.readlines()
	for line in lines:
		t = line.split(":")
		word = t[0].strip()
		count = t[1].strip()
		count = int(count)
		if word in total:
			total[word] += count
		else:
			total[word] = count
		c += count

sorted_total = sorted(total.items(), key=operator.itemgetter(1))

print c

for v in sorted_total:
	print str(v[0]) + " " + str(v[1])
