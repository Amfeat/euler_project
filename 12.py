def deliteli(x):
	n=0
	p = x**0.5
	z=0
	if p == int(p):
		z=1
	#print(z)
	for i in range(2,int(p)):
		
		if x%i==0:
			n+=1
		#print('28  :  '+str(i) + " " +str(int(p)) + " " +str(n))
	return ((n*2)+z+2)
print(deliteli(28))
u=8
a=28
while deliteli(a) <=500:
	a+=u
	
	u+=1
	
print(u)
print(a)
print(deliteli(a))

