def reverse_number(x):
	crab = ' '
	for chicken in x:
		crab = chicken + crab
	print(crab)

reverse_number("123456")