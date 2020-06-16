a3 = 1
a1 = 0
a2 = 1
b = 0
n = 1
while a3<4000000:
	a3 = a1 + a2
	a1 = a2
	a2 = a3
	n += 1
	if a3%2 == 0:
		b = b + a3
print(b)	




