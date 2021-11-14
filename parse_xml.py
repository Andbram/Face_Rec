import re

inpt = "labels_ibug_300W_test.xml"
outpt = "labels_ibug_300W_test_38point.xml"

LANDMARKS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60}

PART = re.compile("part name='[0-9]+'")

rows = open(inpt).read().strip().split("\n")
output = open(outpt, "w")

for row in rows:
	parts = re.findall(PART, row)
	if len(parts) == 0:
		output.write("{}\n".format(row))
	else:
		attr = "name='"
		i = row.find(attr)
		j = row.find("'", i + len(attr) + 1)
		name = int(row[i + len(attr):j])
		if name in LANDMARKS:
			output.write("{}\n".format(row))
output.close()
