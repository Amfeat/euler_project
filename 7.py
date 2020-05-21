#hello
print("sukka")
s = [1, 2]
a = 3
d = []
e = 0
while len(s)<10002:
    
    for b in s:
        if a%b==0:
            d.append(b)
        #print(a, d)
    if len(d) <= 1:
        s.append(a)
       # print(888888888, len(d))
    d = []
    a+=2
print(s[10001])
