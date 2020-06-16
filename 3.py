a = 600851475143
b = 2
bold = 1
dli = "Делители: "
while a != 1 :
	pass
	while a%b != 0:
		b += 1
	dli = dli + str(b) + " "
	a = a/b
	bold = b
print(dli)