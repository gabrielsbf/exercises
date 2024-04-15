def sorting(string: str):
	ascii_l = list()
	ascii_u = list()
	digit = list()
	for i in string:
		if ord(i) >= 65 and ord(i) <= 90:
			ascii_u.append(i)
		elif ord(i) >= 97 and ord(i)<= 122:
			ascii_l.append(i)
		else:
			digit.append(i)
	digit.sort()
	even = list()
	odd = list()
	for i in digit:
		if int(i) % 2 == 0:
			even.append(i)
	for i in digit:
		if i not in even:
			odd.append(i)
	print(odd, even)
	ascii_l.sort()
	ascii_u.sort()
	return ''.join(ascii_l + ascii_u + odd + even)



