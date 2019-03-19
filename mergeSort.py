#!/usr/bin/python3.6

totalComparisions = 0

def mergeSort(myArray) :

	if len(myArray) > 1 :  # recursion condition

		midSize = len(myArray) // 2

		# Divide Section - O(1)
		leftArray = myArray[:midSize]
		rightArray = myArray[midSize:]

		# Conquer Section
		# recursively sorting 2 sub arrays of size n/2
		mergeSort(leftArray) # 2 * T(cn/4) => T(cn/2)
		mergeSort(rightArray)  # 2 * T(cn/4) => T(cn/2)

		# Merging (Sorting) Time for all the Subproblems at Each Level = 2^i * (cN / 2^i) = cN
		# Total Merging Time of All Subproblems from Each Level = Sum of Merging Times For All Levels
		#		Total MergeSort = (total # of levels) * (merge time at each level)
		#					    = (log(N) + 1) * (cN)
		#		Total MergeSort	= O(Nlog(N))

		# Combine Section - O(N) 
		merge(myArray, leftArray, rightArray)



def merge(myArray, lArray, rArray) :
	global totalComparisions
	indexL = indexR = myIndex = 0
	# doing the sorting part
	while indexL < len(lArray) and indexR < len(rArray) :
		if lArray[indexL] <= rArray[indexR] :
			# now adjusting the input array to be sorted
			myArray[myIndex] = lArray[indexL]
			indexL += 1 

		else :
			myArray[myIndex] = rArray[indexR] 
			indexR += 1

		myIndex += 1
		totalComparisions += 1

	# handling any left overs
	while indexL < len(lArray) :
		myArray[myIndex] = lArray[indexL]
		indexL += 1
		myIndex += 1

	while indexR < len(rArray) :
		myArray[myIndex] = rArray[indexR]
		indexR += 1
		myIndex += 1



def printArray(myArray) :
	for i in myArray :
		print(i, end = " ")
	
	print()
	print()


if __name__ == "__main__" :

	myArray = [32, 42, 3, 4, 66, 98, 102, 54, 12, 18, 23, 43, 3, 28, 91]

	print("Initial Array: ")
	printArray(myArray)

	mergeSort(myArray)
	print("Sorted Array: ")
	printArray(myArray)

	print("Total Number of Comparisions: " + str(totalComparisions))


