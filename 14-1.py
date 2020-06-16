s = 2
for i in range(1,11):
	n = (s-1)/3
	if n>1 and ((n%2) == 1) and n.is_integer():
		s=n
	else:
		s=2*s
		pass
	pass
print(s)