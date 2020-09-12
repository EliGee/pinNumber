import random

def generateIncrements(start):
	countList = list(range(start, 100, start))
	lastIndex = len(countList) - 1 
	randomIndex = random.randint(0, lastIndex)
	return countList[randomIndex]
  
def generateConsecutive():
	evenOrOdd = random.randint(0,1)
	if evenOrOdd == 0:
		#I wanna start it at 2 because "02" isn't as an intuitive pattern as "24"
		startInt = 2
	else: 
		startInt = 1 
	consecuList = list(range(startInt, 10, 2))
	lastIndex = len(consecuList) - 2
	randomIndex = random.randint(0, lastIndex)
	
	digitOne = consecuList[randomIndex]
	digitTwo = consecuList[randomIndex + 1]
	return str(digitOne) + str(digitTwo)

pinBitA = generateIncrements(10)
pinBitB = generateIncrements(11)
pinBitC = generateConsecutive()

#randomizing the order of the two-digit strings.
#this isn't an elegant solution, but it's what I've got... for now.
pinOrder = random.randint(0, 5)
if pinOrder == 0:
	print(f'Your pin number is {pinBitA}{pinBitB}{pinBitC}')
elif pinOrder == 1:
	print(f'Your pin number is {pinBitA}{pinBitC}{pinBitB}')
elif pinOrder == 2: 
	print(f'Your pin number is {pinBitB}{pinBitA}{pinBitC}')
elif pinOrder == 3:
	print(f'Your pin number is {pinBitB}{pinBitC}{pinBitA}')
elif pinOrder == 4: 
	print(f'Your pin number is {pinBitC}{pinBitA}{pinBitB}')
else: 
	print(f'Your pin number is {pinBitC}{pinBitB}{pinBitA}')
