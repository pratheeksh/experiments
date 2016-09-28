def find_boundary(inputArray):
	l = len(inputArray)

	for i in xrange(len(inputArray)):
		if inputArray[0] >= 0:
			return 0
		if i < l - 1:
			if inputArray[i] < 0 and inputArray [i+1] >=0:
				return i+1


	return l
def merge(a1, a2):
	new_array = [0] * (len(a1) + len(a2))
	j = k = 0
	for i in xrange(len(a1) + len(a2)):
		if j < len(a1) and k < len(a2):
			if a1[j] < a2[k]:
				new_array[i] = a1[j]
				j+= 1
			else:
				new_array[i] = a2[k]
				k+= 1
		elif j < len(a1):
			new_array[i] = a1[j]
			j+= 1
		elif k < len(a2):
			new_array[i] = a2[k]
			k+= 1
	return new_array

def main():
	inputArray = [-6, -4, -2, 0, 1, 5, 13]
	#inputArray = [1, 3, 4, 5, 6, 19]
	#inputArray = [-10, -7, -9, -1]
	index = find_boundary(inputArray)
	print index
	if index < len(inputArray):
		first_half = inputArray[:index]
		second_half = inputArray[index:]
		first_half.reverse()
		print first_half, second_half
		first_sorted_array = map((lambda x: x**2), first_half)

		second_sorted_array = map((lambda x: x**2), second_half)
		print first_sorted_array, second_sorted_array
		merged_array = merge(first_sorted_array, second_sorted_array)
		print merged_array
	else:
		inputArray.reverse()
		print map((lambda x: x**2), inputArray)



main()