#==== I plan the code====

# this program will make a 6 digit pin, made of 3 blocks of two-character strings each containing two numbers
# the numbers will have easy to remember qualities 
 	#one will end in a 0 
 	#one wlil be double digits 
 			#eventually, it will be cool to randomize the order each of these three integers comes in, but let's not get ahead of ourselves
 	#one will be two either odd or even sequential numbers, like '57'		
	
#!!! the first two functions can be the same function, taking the start digit (10 or 11) as an argument 


	#the first function takes an argument, start.  It'll either be 10 or 11.
	#creates a list with range start, 100, 10.  This will make a list counting by 10.
		#i'll probably give it default argument of 10
	#creating an integer for a random index.... 
		#lastIndex = len(countList) - 1
			#randomIndex = random.randint(0, lastIndex)
		#then I pick a random number from that list and save it, STRINGIFIED, to pinBitA. 
			#return str(countList[randomIndex])
	#save the two calls to this function as pinBit A and pinBitB, respectively

	#the third function, hrm....
		#can do a random 0 or 1 to decide if odd or even
		#then it creates a list that increments by +2 using list(range(startInt, 9, 2)
		#then it randomizes list length - 2. (because the list will range 0-3 if even and 0-5 if odd)
			#not -1, because the first digit can't be last item on the list, because it's gotta be two consecutive numbers
		#then it saves list[x] and list[x+1], stringified, in pinBitC

#===I done plan the code===


import random

#this function does not work
def generateIncrements(start):
	countList = list(start, 100, 10)
	lastIndex = len(countList) - 1 
	randomIndex = random.randint(0, lastIndex)
	return countList[randomIndex]
"""Traceback (most recent call last):
  File "C:\\Users\\eilee\\OneDrive\\Documents\\My_code\\pinRandomizer.py", line 72, in <module>
    pinBitA = generateIncrements(10)
  File "C:\\Users\\eilee\\OneDrive\\Documents\\My_code\\pinRandomizer.py", line 34, in generateIncrements
    countList = list(start, 100, 10)
TypeError: list expected at most 1 argument, got 3"""

#ok why? why is it assuming my 3 arguments while generating countList also need to be put into the functino aRGH??

#this function works like a charm, to my great amazement. 
def generateConsecutive():

	evenOrOdd = random.randint(0,1)
	#could i just avoid using evenOrOdd and do 'if random.randint(0,1) == 0?' We'll find out later. 
	if evenOrOdd == 0:
		#even 
		#I wanna start it at 2 because "02" isn't as an intuitive pattern as "24"
		startInt = 2
	else: 
		#odd
		startInt = 1

 
	consecuList = list(range(startInt, 10, 2))
	print(consecuList)
	#check the syntax for using .len to grab the final index number.  len - 1
		#!!! but we want to make it -2 because we are also going to include the next consecutive bit!!!
			#by which i mean there will be index, index + 1	
	lastIndex = len(consecuList) - 2
	#picks the index of a random number on the list
	randomIndex = random.randint(0, lastIndex)

	digitOne = consecuList[randomIndex]
	digitTwo = consecuList[randomIndex + 1]

	return str(digitOne) + str(digitTwo)

pinBitC = generateConsecutive()
print(pinBitC)

pinBitA = generateIncrements(10)
pinBitB = generateIncrements(11)

print(f'Your pin number is {pinBitA}{pinBitB}{pinBitC}')

#how would I write a function that takes three strings and puts them together in a random order?
#by just... having six different elifs, cuz there's only 6 possible combos
	#but that's not very elegant... is there a randomization thing that would work better for that??
		#it would be fun to solve!!!

""" 
#GETTING THE LAST NUMBER(index) IN A LIST:
#print(sampleList[len(sampleList) - 1]) 