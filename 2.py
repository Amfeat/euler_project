a = 1
a1 = 1
a2 = 0
n = 0
b = 0
string = "числа "
string2 = "числа B "
while a < 4000000:
    n += 1
    a = a1 + a2
    a2 = a1
    a1 = a
    string = string + str(a) + " "
    if n%2 == 0:
        b += a
        string2 = string2 + str(b) + " "
print(string)
print(string2)
print(b)
