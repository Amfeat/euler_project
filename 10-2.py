s=[ 3, 5]

for i in range(7,int(2000000**0.5),2):
	for j in s:
		if i%j==0:
			break
	else:

		s.append(i)		
print(sum(s)+2)			