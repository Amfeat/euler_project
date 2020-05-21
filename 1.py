end = 1
while end == 1:
    string = "Числа "
    endcicle = input("Введи число: ")
    if endcicle == "end":
        print("poka!")
        break
    a = 1
    b = 0
  #  c= 0
    while a < int(endcicle):
        c = a % 5
        if c == 0:
            b += a
          #  print(a)
            string = string + " " + str(a)

        else:
       
            c = a % 3
            if c == 0:
                b += a
            #    print(a)
                string = string + " " + str(a)
        a += 1
        
       # string = string + " "
    print(string)
    print("Сумма кратных 3 и 5: "+ str(b))
