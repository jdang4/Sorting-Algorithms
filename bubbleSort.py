#!/usr/bin/python3.6

myArray = [12, 34, 1, 31, 75, 98, 65, 18, 21]  
myArray2 = [1, 12, 18, 31, 34, 21, 98, 65, 75]

numOfComparisions_lazy = 0
numOfComparisions_condition = 0
swapFlag = False

def swap(fromIndex, toIndex, version) :

	if version == 1 :
		tempValue = myArray[toIndex]
		myArray[toIndex] = myArray[fromIndex]
		myArray[fromIndex] = tempValue

	elif version == 2 :
		tempValue = myArray2[toIndex]
		myArray2[toIndex] = myArray2[fromIndex]
		myArray2[fromIndex] = tempValue


def lazyBubbleSort(round) :
	global numOfComparisions_lazy
	end = len(myArray) - round

	for i in range(0, end, 1) :
		nextIndex = i + 1
		if round != (len(myArray) - 1) :
			numOfComparisions_lazy += 1
		if nextIndex < end :
			if myArray[i] > myArray[i + 1] :
				swap(i, (i+1), 1)


def conditionBubbleSort(round) :
	global numOfComparisions_condition
	global swapFlag
	end = len(myArray2) - round

	for i in range(0, end, 1) :
		nextIndex = i + 1
		if round != (len(myArray2) - 1) :
			numOfComparisions_condition += 1
		if nextIndex < end :
			if myArray2[i] > myArray2[i + 1] :
				swap(i, (i+1), 2)
				swapFlag = True


if __name__ == "__main__" :

 	for i in range(0, len(myArray), 1) :
 		round = i
 		lazyBubbleSort(round)

 	for val in myArray :
 		print(val, end = " ")
 	else:
 		print()
 		print()

 	for i in range(0, len(myArray2), 1) :
 		round = i
 		swapFlag = False
 		conditionBubbleSort(round)

 		if not swapFlag :
 			break


 	for val in myArray2 :
 		print(val, end = " ")
 	else:
 		print()
 		print()

 	print("Number of Comparisions For Lazy: " + str(numOfComparisions_lazy))
 	print("Number of Comparisions For Condition: " + str(numOfComparisions_condition)) 

'''
	Worst Case Scenario for Bubble Sort: O(N^2)
	Average Case Scenario for Bubble Sort: O(N^2)
	Best Case Scenario for Bubble Sort: O(N)
'''