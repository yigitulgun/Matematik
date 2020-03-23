def math(ops):
    if ops not in ("1),2),3),4),5),6),7),8)"):
        return "Birini seçmek zorundasın :"
while True: 
    string = [" ","1)Hesap Makinesi", "2)Üçgenin Alanı", "3)Hipotenüs", "4)Hipotenüsün Eğimi" , "5)Çemberin Alanı", "6)Çemberin Çevresi" ,"7)Km'yi Mil'e Çevirme","8)Boy'u Feet'e Çevirme"]
    for i in string:
        print(i)
    ops = (input("Seçiniz:"))
    print(math(ops))
    if ops == "1":
        def calc(o,p,s):
            if s not in "+-*/":
                return "Only +-?/"
            if s == "+":
                return(str(o) + " " + s + " " + str(p) + " = " + str(o+p))
            elif s == "-":
                return(str(o) + " " + s + " " + str(p) + " = " + str(o-p))
            elif s == "*":
                return(str(o) + " " + s + " " + str(p) + " = " + str(o*p))
            elif s == "/":
                return(str(o) + " " + s + " " + str(p) + " = " + str(o/p))
        try:
            o = int(input("1. Sayı: "))
        except:
            print("1. Sayı!!!: ")  
        try:
            p = int(input("2. Sayı: "))
        except:
            print("2. Sayı!!!: ")
        s = input("İşlem Seçiniz +-*/ : ")
        print(calc(o,p,s))
    if ops == "2":
            try:
                h = int(input("Yukseklik: "))
            except:
                print("Yukseklik!!!: ")
                continue
            try:
                x = int(input("Taban Alani: "))
            except:
                print("Taban Alani!!!: ")
                continue
            y = (h*x/2)
            print("Üçgenin Alanı = " + str(y))
            
    if ops == "3":
        try:
            x = int(input("1. Sayı: "))
        except:
            print("1. Sayı!!!: ")
            continue
        try:
            y = int(input( "2. Sayı: "))
        except:
            print =("2. Sayı!!!: ")
            continue
        z = (x**2) + (y**2)
        print("Hipotenüs = " + "√¯" + str(z) )
    if ops == "4":
        try:
            x = int(input("Dik Kenar: "))
        except:
            print("Dik Kenar!!! ")
        try:
            y = int(input("Yatay Kenar: "))
        except:
            print("Yatay Kenar !!!: ")
        z = (x / y)
        print("Hipotenüsün Eğimi = " + str(z))
            
        
    if ops == "5":
        try:
            r = int(input("R Kaçtır: "))
        except:
            print("R kaçtır!!!: ")
        pi = 3.14
        print("Cevap = " + str((pi*r**2)))
        
    if ops == "6":
        try:
            r = int(input("R Kaçtır: "))
        except:
            print("R kaçtır!!!: ")
        pi =3.14
        a = 2
        z = (pi * a * r)
        print("Çemberin Çevresi = " + str(z))
            
    if ops == "7":
        try:
            x = int(input("Kaç kilometre ? "))
        except:
            print("kaç kilometre !!! ") 
        mil = 0.621371192
        kmil = x * mil
        print(str(x) + " Km = " +str(kmil) + " Mil" )
    
    if ops == "8":
        feet = 30.48
        try:
            x = int(input("Boyunuz : "))
        except:
            print("Boyunuz !!! ")
        feetx = (x / feet)
        print(str(x)+ " Cm = " + str(feetx) + " Feet")
            
            
            
            
            
            
            
            
            
            
            