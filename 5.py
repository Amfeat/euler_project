# 10 20 19 17 15 14 13 12 11
b = 0
n = 0
e = 0
while e == 0:
	b +=46189
	
	for a in  [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]:
		c = b%a
		if c!=0:
			#print('sosat')
			n = 0
			break
		else:
			n +=1
			if n >= 8:
				print(str(n) + "        " + str(b))
			if n == 10:
				e = 1
				print(b)
		

  

