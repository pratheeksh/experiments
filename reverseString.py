def revString(str_to_reverse):
	if len(str_to_reverse) == 1:
		return str_to_reverse
	return  revString(str_to_reverse[1:]) + str_to_reverse[0]

print revString("Hello world")