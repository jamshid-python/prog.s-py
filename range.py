# def kk(ism, t_yil, yil=2022):    # Funsksiya yaratamiz.
# 	"""tug'ulgan yilini hisoblab beruvchi dastur"""
# 	print(f"Hurmatli {ism.title()} siz {yil - t_yil} yoshdasiz!")

# kk(input('Ismingizni Kiriting: '), int(input("Tugulgan yilingizni Kiriting: ")))



# # # # # # # #
# def math1(son):
# 	"""Kvadrati va kubini chiqaruvchi dastur"""
# 	print(f"Siz bergan soning kvadrati {son**2}\n"
# 		f"Shu sonningning kubi {son**3}")

# math1(int(input("Istalgan Sonni Kiriting: ")))





# def juft(son):
# 	"""Juft yoki toqligini chiqaruvchi funksiya"""
# 	while True:
# 		if son % 2 == 0:
# 			print(f"{son} son juft son")
# 		if son % 2 != 0:
# 			print("Toq son!")

# juft(int(input("Son Kiriting: ")))




# def katta(f_son, s_son):
# 	"""Taqqoslaovchi funksiya"""
# 	if f_son < s_son:
# 		print(f"{s_son} son katta!")
# 	if f_son > s_son:
# 		print(f"{f_son} son katta!")
# 	if f_son == s_son:
# 		print("Ikki son ham teng")

# katta(int(input("Birinchi sonni kiriting: ")), int(input("Ikkinchi sonni kiriting: ")))





# def xy(x, y):
# 	"""x ning y darajasini hisoblab beruvchi dastur"""
# 	print(x,"ning",y,"inchi darajasi", x**y, "ga teng")

# xy(int(input("x=")), int(input("y=")))




# def yy(x):
# 	""""Siz kiritgan soning kvadrati yoki 4-darjasini hisoblab beruvchi dastur"""
# 	print(x,"ning kvadrati", x**2,"ga teng")
# 	print(x,"ning 4-darajasi", x**4,"ga teng")

# yy(int(input("Sonni kiriting; ")))




# def qoldiq(x):
# 	"""Qaysilarga qoldiqsiz bo'linishini tekshiruvchi dastur"""
# 	if x % 2 == 0:
# 		print("2")
# 	if x % 3 == 0:
# 		print("3")
# 	if x % 4 == 0:
# 		print("4")
# 	if x % 5 == 0:
# 		print("5")
# 	if x % 6 == 0:
# 		print("6")
# 	if x % 7 == 0:
# 		print("7")
# 	if x % 8 == 0:
# 		print("8")
# 	if x % 9 == 0:
# 		print("9")

# qoldiq(int(input("Sonni kiriting: ")))




# def tarif(ism, fam, t_j, t_y, tel, mail):
# 	"""Malumotlarini saqlovchi funksiya"""
# 	print("Siz haqingizdagi malumotlarni saqlaymiz!")

# tarif(input("Ismingin kiriting: "), input("Familyangizni kiriting: "), input("Tug'ulgan joyingizni kiritng: "), 
# 	 input("Tug'ulgan yilingizni kiriting: "), int(input("Telefon Raqamingizni kiriting: ")),
# 	 input("Murojaat uchun Gmail manzilingizni kiriting: "))
# print("Foydalanuvchi", ism.title(), fam.title(),":", t_y,"-yilda", t_j.title(), "da tug'ulgan")
# print("Telefon raqami", tel, "Gmail manzili", mail)





# def return_value(name, surname, birth_date, birth_place, phone_number, gmail):
# 	data = {
# 		"Name": name,
# 		"Surname": surname,
# 		"Birth Date": birth_date,
# 		"Birth Place": birth_place,
# 		"Phone Number": phone_number,
# 		"Gmail": gmail,
# 	}

# 	return data


# first_person = return_value(input("Ismingin kiriting: "), input("Familyangizni kiriting: "), input("Tug'ulgan joyingizni kiritng: "), 
# 	 input("Tug'ulgan yilingizni kiriting: "), int(input("Telefon Raqamingizni kiriting: ")),
# 	 input("Murojaat uchun Gmail manzilingizni kiriting: "))

# print(first_person["Name"])




# def qoldiq1(number):
# 	"""Qaysilarga qoldiqsiz bo'inishni tekshiruvchi dastur"""
	
# 	if number > 10:
# 		for b in range(1, 11):
# 			if number % b == 0:
# 				print(b)
# 	else:
# 		print("Number > 10  <==")

# qoldiq1(int(input("enter a number: ")))




# def voice(number1):
# 	"""Ko'paytuvchilarini aniqlab beruvchi dastur"""
# 	if number1 < 1000:
# 		for a in range(1, 1001):
# 			if a % number1 == 0:
# 				print(a)
# 	else:
# 		print("Number < 1000 <<<<!")

# voice(int(input("Enter a number: ")))



# # # # # # # # # # #
# def jadval(number):
# 	"""Karra jadavali dasturi"""
# 	while True:
# 		n = 1
# 		print(number * n)
# 		n += 1
# 		if n > 9:
# 			break

# 	if number < 10:
# 		print("number < 10")

# jadval(int(input("Enter a nuber: ")))




# number = int(input("Enter a Number: "))
# if number < 10:
# 	for a in range(1, 11):
# 		print(number, "X", a, "=", a * number)
# else:
# 	print("wrong input")




# def taqqosla(x, y, z):
# 	"""Kattasini qaytaruvchi funksiya"""
# 	while True:	
# 		if x > y > z or x > z > y or x > y == z:
# 			print(x, "is big!")
# 		if y > x > z or y > z > x or y > x == z:
# 			print(y, "is big")
# 		if z > x > y or z > y > x or z > y == x:
# 			print(z, "is big")
# 		else:
# 			print("Draw")


# taqqosla(int(input("Enter a first number: ")),
# 	int(input("Enter a second number: ")),
# 	int(input("Enter a third number: ")),
# 	)



# def doira_info(radius, PI = 3.14):
# 	"""Doira ma'lumotlarini saqlovchi funksiya"""
# 	doira = {
# 	"radius" : radius,
# 	"diametr" : radius * 2,
# 	"Uzunligi" : radius * PI * 2,
# 	"Yuzi" : 2 * PI * radius ** 2,
# 	}

# 	return doira



# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_son




# def multi(*sonlar):
# 	"""Ko'paytmani qaytaruvchi funksiya"""
# 	son = 1
# 	for son1 in sonlar:
# 		son *= son1
# 	return son

# print(multi(4, 2, 3))



# def talaba_info(ism, familya, **info1):
# 	"""Talaba tajribasin qaydi qiluvchi funksiya"""
# 	info1["Talaba ismi; "] = ism
# 	info1["Talaba familyasi; "] = familya
# 	return info1

# talaba = talaba_info("Jamshid", "Ahmadov", yosh = 14, tugulgan_joyi = "Qashqadaryo")
# print(talaba)


# import random as rand 

# while True:
	# a = rand.randint(1, 500)
	# b = rand.randint(1, 400)

	# que = int(input(f"{a} + {b} =" ))
	# if que == a + b:
	# 	print("True")
	# else:
	# 	print("False")


# # # # # # # # # #
# import random 
# while True:
# 	b = ["010", "101", "110", "001"]
# 	ac = random.choice(b)
# 	print(ac)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# import random													  #
# while True:													  #
# 	key = ["+", "-", "*", "/"]									  #
# 	key_a = random.choice(key)									  #
# 	number1 = random.randint(1, 501)							  #
# 	number2 = random.randint(1, 100)							  #
# 	if key_a == "+":											  #
# 		que = int(input(f"{number1} + {number2} = "))		      #
# 		if que == number1 + number2:                              # 
# 			print("True")										  # 
# 		else:													  #
# 			print("False")										  #
# 	if key_a == "-":											  #
# 		que1 = int(input(f"{number1} - {number2} = "))			  #
# 		if que1 == number1 - number2:							  #
# 			print("True")										  #
# 		else:													  #
# 			print("False")										  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  

# from turtle import Turtle, Screen
# oyna = Screen()
# oyna.title('Asab Chiqganida')
# chiziq = Turtle()
# chiziq.color('blue')
# chiziq.pensize(4)
# chiziq.speed(0)
# chiziq.hideturtle()
# chiziq.up()
# chiziq.goto(300, 300)
# chiziq.down()
# chiziq.goto(300, -300)
# chiziq.goto(-300, -300)
# chiziq.goto(-300, 300)
# chiziq.goto(300, 300)
# koptok = Turtle()
# koptok.shape('circle')
# koptok.color('blue')
# koptok.up()
# koptok.goto(0, 0)
# koptok.speed(-1)
# koptok1 = Turtle()
# koptok1.shape('circle')
# koptok1.color('red')
# koptok1.up()
# koptok1.goto(0, 0)
# koptok1.speed(-1)
# qadam = 3
# qadam2 = 3
# qadam_1 = -3
# qadam_2 = -3

# while True:
# 	x, y = koptok.position()

# 	if x + qadam >=300 or x + qadam <= -300:
# 		qadam = -qadam
# 	if y + qadam2 >=300 or y + qadam2 <= -300:
# 		qadam2 = -qadam2

# 	koptok.goto(x + qadam, y + qadam2)

# 	x1, y1 = koptok1.position()
# 	if x1 + qadam_1 >=300 or x1 + qadam_1 <= -300:
# 		qadam_1 = -qadam_2
# 	if y1 + qadam_2 >=300 or y1 + qadam_2 <= -300:
# 		qadam_2 = -qadam_2

# 	koptok1.goto(x1 + qadam_1, y1 + qadam_2)


# oyna.mainloop()


# while True:
# 	voice = int(input("Enter a number: "))	
# 	a = range(1, voice)
# 	for b in a:
# 		if voice % b == 0:
# 			print(b)
# 	print(voice)	






# import random

# def sontop(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end="")
#         elif taxmin>tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end="")
#         else:
#             break
        
#     print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
#     return taxminlar
    

# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         if quyi != yuqori:
#             taxmin = random.randint(quyi,yuqori)
#         else:
#             taxmin = quyi
#         javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
#                       f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {taxminlar} ta taxmin bilan topdim!")
#     return taxminlar

# def play(x=10):
#     yana = True
#     while yana:
#         taxminlar_user = sontop(x)
#         taxminlar_pc = sontop_pc(x)
        
#         if taxminlar_user>taxminlar_pc:
#             print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
#         elif taxminlar_user<taxminlar_pc:
#             print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
#         else:
#             print("Durrang!")
#         yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
# play()




# import math

# numbers = range(1, 11)
# def kvadrati(x):
# 	"""Listning har birining kvadaratini qaytaruvchi funksiya"""
# 	return x**2

# kvadrat = list(map(kvadrati, numbers))
# print(kvadrat)

# from turtle import Turtle, Screen
# oyna = Screen()
# oyna.title('Asab Chiqganida')
# koptok1 = Turtle()
# koptok = koptok1
# koptok.shape('circle')
# koptok.color('blue')
# koptok.up()
# koptok.goto(0, 0)
# koptok.speed(-1)

# koptok1 = Turtle()
# koptok1 = Turtle()
# koptok1.shape('circle')
# koptok1.color('red')
# koptok1.up()
# koptok1.goto(0, 0)
# koptok1.speed(-1)


# run1 = 3
# run_1 = 0
# run2 = -3
# run_2 = -3

# while True:
# 	x, y = koptok.position()

# 	if x + run1 >=50 or x + run1 <= -50:
# 		run1 = -run1
# 	if y + run_1 >=50 or y + run_1 <= -50:
# 		run_1 = -run_1

	
# 	koptok.goto(x + run1, y + run_1)

# 	if x + run1 >=50 or x + run1 <= -50:
# 		run1 = -run1
# 	if y + run_1 >=50 or y + run_1 <= -50:
# 		run_1 = -run_1

# 	x1, y1 = koptok.position()

# 	if x + run2 >=50 or x + run2 <= -50:
# 		run2 = -run2
# 	if y + run_2 >=50 or y + run_2 <= -50:
# 		run_2 = -run_2
# 	koptok1.goto(x1 + run2, y + run_2)

# oyna.mainloop()


# Boshlag'ich ko'rinishdagi Calkulyator
# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# c = int(input("Enter a third number: "))

# ans = a + b + c
# print(f"Answer is {ans}")
print(eval(input()))



