dictionary = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
file = open('input.txt', 'r')
only_numbers2=[]
twoDigitNumber = 0
for line in file:
	only_numbers = []
	words = ""
	for i in line:
		if i.isdigit() == True:
			only_numbers.append(i)
		words += i
		for i in dictionary:
			if i in words:
				only_numbers.append(str(dictionary.index(i)+1))
				words = words.replace(i,i[-1])
	print(only_numbers)
	twoDigitNumberStr = only_numbers[0] + only_numbers[-1]
	print(twoDigitNumberStr)
	twoDigitNumber += int(twoDigitNumberStr)
print(twoDigitNumber)