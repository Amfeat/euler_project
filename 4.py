a=10000
otv = 0
otva = 0
otvb = 0
while a>990:
	b=10000
	while b>990:
		c = a*b
	#	print("wwwwwwwwww" + str(b))
		if str(c) == str(c)[::-1]:
			if c>otv:
				otv = c
				otva = a
				otvb = b
			break
		b-=1
		
	a-=1
print("ответ: " + str(otv) + "=" + str(otva) + "*" + str(otvb))
