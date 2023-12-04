file = open('input.txt', 'r')
twoDigitNumber = 0
for line in file:
	only_numbers =[]
	for i in line:
		if i.isdigit():
			only_numbers.append(i)
	first_digit = only_numbers[0]
	last_digit = only_numbers[-1]
	twoDigitNumberStr = first_digit + last_digit
	twoDigitNumber += int(twoDigitNumberStr)
print(twoDigitNumber)