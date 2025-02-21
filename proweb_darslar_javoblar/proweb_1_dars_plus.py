# 1. 
# Foydalanuvchi ismini so’raydigan va unga salom beradigan dastur yozing. 

# ism =input('Ismingizni kiriting :')
# print(f'Assalomu alaykum  {ism.title()}')


# 2. 
# Foydalanuvchidan 3 ta son so’raydigan va ularning yig’indisini chop etadigan dastur yozing.

# # print('Istalgan 3ta son kiriting ularning yigindisini hissoblab beraman:')
# son1= int(input('Birinchi sonni kiriting:'))
# son2= int(input('Ikkininchi sonni kiriting:'))
# son3= int(input('Uchinchi sonni kiriting:'))
# yigindi= son1+son2+son3
# print(f'Siz kiritgan sonlar yigindisi: {yigindi} ga teng!')


# 3. 
# 6 ta maktab o’quvchilari 50 ta olmani teng taqsimlashdi. Bo’linmaydigan qoldiq savatda qoldi.
# Har bir o’quvchi nechta olma oladi? Savatda nechta olma qoladi? Istalgan miqdordagi o’quvchilar 
# va olmalar uchun topshiriqni bajaring.

# qoldiq = (50%6)
# olma_soni= (50//6)
# print(f'Savatda {qoldiq} ta olma qoldi!')
# print(f'Har bir bola: {olma_soni}tadan olma olishadi!')

# #95ta olma va 12ta o'quvchi uchun:
# qoldiq = (95%12)
# olma_soni= (95//12)
# print(f'Savatda {qoldiq} ta olma qoldi!')
# print(f'Har bir bola: {olma_soni}tadan olma olishadi!')


# 4. Foydalanuvchidan raqam so'raydigan va shu raqamdan oldingi va keyingi sonni chop etadigan dastur yozing:
# Misol
# Raqamni kiriting: 1345
# Keyingi raqam: 1346
# Oldingi raqam: 1344

# son =int(input("Raqam kiriting:"))
# print(f"Keyingi raqam:{son+1}")
# print(f"Oldingi raqam:{son-1}")


# 5. Matnni biriktirilgan fayldagi kabi formatda chiqaradigan dastur tuzing.

#print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t\t\tUp above the world so high,\n\t\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are")


# 6. Quyidagi uchta o'zgaruvchini kutilgan natijaga ko'ra formatlash usulini qo'llash dasturini yozing.

# Pul = 1200
# Soni = 3
# Narxi = 400

# Kutilayotgan natija:
# Menda 1200 dollar bor, shuning uchun 400 dollarga 3 ta futbol to'pini sotib olaman.

# pul = 1200
# soni = 3
# narxi = 400
# print(f"Menda {pul} dollar bor, shuning uchun {narxi} dollarga {soni} ta futbol to'pini sotib olaman.")


#7.
# Harorat konvertori:
# Foydalanuvchidan haroratni Selsiy bo'yicha kiritish va uni Farengeytga aylantirishni so'raydigan dastur 
# yarating (formuladan foydalaning

# F=C×9/5+32

# c= int(input('Haroratni kititing C`:'))
# f=(c*9/5)+32
# print(f'Harorat:{f} F`')

# 8.
# Birlik konvertori:
# Muayyan kilometrlarni milga aylantiradigan dastur yarating. Kilometrlar soni foydalanuvchi 
# tomonidan input() orqali kiritilishi kerak.
# Foydalanuvchi kiritgan ma'lumotlarni saqlash va uni milga aylantirish uchun to'g'ri ma'lumot 
# turidan foydalaning (1 kilometr taxminan 0,621371 milya ekanligini unutmang).
# O'tkazish natijasini formatlangan satrlar yordamida tavsif bilan chop eting.

# print('Menga kilometr kiriting men sizga milya da olchab beraman.')
# km=int(input('kilometr:'))
# milya1 = 0.621371
# print(f'{km}km = {km*milya1}mil')


# 9.
# Foydalanuvchiga ikkita tamsayı a va b ni taklif qiladigan dastur yarating va keyin 
# quyidagi matematik amallarning natijalarini ko'rsating:

# a va b yig'indisi;
# a va b o'rtasidagi farq;
# a va b ning kopaaytmasi;
# a ning b ga bo'lingani;
# a ga b bo'linganda qoldiq;
# a sonining b darajasiga ko'tarilishi natijasi

# a = int(input("Birinchi butun sonni kiriting: "))
# b = int(input("Ikkinchi butun sonni kiriting: "))
# print(f"{a} + {b} = {a + b}")  
# print(f"{a} - {b} = {a - b}")  
# print(f"{a} * {b} = {a * b}") 
# print(f"{a} / {b} = {a / b}")  
# print(f"{a} % {b} = {a % b}") 
# print(f"{a} ** {b} = {a ** b}") 


# 10.
# Foydalanuvchidan raqam so‘raydigan va 1 dan kirishgacha bo‘lgan musbat natural sonlar 
# yig‘indisini hisoblaydigan dastur tuzing.foydalanuvchi qiymatlari. Birinchi n musbat sonlarning yig'indisini 
# quyidagi formula yordamida hisoblash mumkin:
    
# n=int(input('Son kititing va men sizga 1 dan songacha bolgan musbat natural sonlar yigindisini hisoblab beraman '))
# s=sum = ((n)*(n-1))/2
# print(s)















