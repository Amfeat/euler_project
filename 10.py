#сумма простых чисел до 1000000
#долгий метод
'''
s=[ 3, 5]

for i in range(7,2000000,2):
	for j in s:
		if i%j==0:
			break
	else:

		s.append(i)		
print(sum(s)+2)			
'''
from time import time
start = time()
def whattime():
	print("Time: ", time() - start)

	pass
t = 2000000
end = int(t**0.5)+1
s = [i for i in range (t)]

for j in range(2, end ):
	for u in range(j*j,t,j):
		s[u]=0
	
	
whattime()
print(sum(s)-1)
whattime()
#print(s)