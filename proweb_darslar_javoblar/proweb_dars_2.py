



# 1. Dastur foydalanuvchidan yoshini so’rashi kerak:
#     a. Agar yoshi 18 dan kam yoki unga teng bo'lsa, u holda chiqish: "Siz o'qishingiz kerak."
#     b. Agar yoshi 18 dan katta bo'lsa, lekin 50 dan kam yoki unga teng bo'lsa - "Siz ishlashingiz kerak"
#     c. Agar yoshi 50 dan katta bo'lsa, lekin 59 dan kam yoki unga teng bo'lsa - "Siz yaqinda nafaqaga chiqasiz"
#     d. Agar yoshdan 59 katta bo'lsa, lekin 90 dan kam - "Siz pensionersiz".
#     e.Agar foydalanuvchi haqiqiy bo'lmagan yoshga kirsa, nima ko'rsatilishi kerakligini ham o'ylab ko'ring. Masalan, 100.

# yosh = int(input('Yoshingizni kiruting: '))

# if yosh <=18:
#     print('Siz oqishingiz kerak')
# elif 18<yosh<=50:
#     print('Siz ishlashingiz kerak')
# elif 50<yosh<=59:
#     print('Siz yaqinda nafaqaga chiqasiz')
# elif 59<yosh<=90:
#     print('Siz pensionersiz')
# else:
#     print('Haliyam tirikmisiz e!')


# 2. Foydalanuvchidan butun sonni qabul qiladigan 1 dan 12 gacha shu oyga mos oy nomi  va kunlar sonini qaytaradigan dastur yozing.
# Misol: 
# Oy nomerini kiriting: 2
# Oy nomi: Fevral. Kunlar soni: 28.

# son =int(input('Oy nomerini kiriting: '))
# k1= 'Kunlar soni: 31.'
# k0='Kunlar soni: 30.'
# k='Kunlar soni: 28.'
# if son ==1:
#     print(f'Oy nomi:Yanvar. {k1}')
# elif son==2:
#     print(f'Oy nomi:Fevral. {k}')
# elif son ==3:
#     print(f'Oy nomi:Mart. {k1}')    
# elif son ==4:
#     print(f'Oy nomi:Aprel. {k0}')
# elif son ==5:
#     print(f'Oy nomi:May. {k1}')
# elif son ==6:
#     print(f'Oy nomi:Iyun. {k0}') 
# elif son ==7:
#     print(f'Oy nomi:iyul. {k1}')   
# elif son ==8:
#     print(f'Oy nomi:Avgust. {k1}')    
# elif son ==9:
#     print(f'Oy nomi:Sentyabr. {k0}')    
# elif son ==10:
#     print(f'Oy nomi:Oktyabr. {k1}')
# elif son ==11:
#     print(f'Oy nomi:Noyabr. {k0}')
# elif son==12:
#     print(f'Oy nomi:Dekabr. {k1}')  
# if 13<=son:
#     print('Notogri son kiritdingiz!') 
    
# 3. Foydalanuvchidan uchta sonni so’raydigan va mos keluvchi sonlar sonini chiqaruvchi dasturni yozing.
# Misol
# Birinchi sonni kiriting: 2 
# Ikkinchi sonni kiriting: 2
# Uchinchi sonni kiriting: 5
# Mos keluvchilar soni: 2         

# son1=int(input('Birinchi sonni kiriting:'))
# son2=int(input('Ikkinchi sonni kiriting:'))
# son3=int(input('Uchinchi sonni kiriting:'))

# if son1==son2==son3:
#     print('Mos keluvchilar soni: 3')
# elif son1==son2 or son1==son3 or son2==son3:
#     print('Mos keluvchilar soni: 2')
# else:
#     print('Hech biri mos emas!')

# 4 *. Foydalanuvchidan ikkita son so’raydigan agar ulani ko’paytmasi 1000 dan katta bo’lmasa ko’paytmani aks 
# holda ularni yig’indisini qaytaradigan dasturni yozing.

# son1=int(input('Birinchi sonni kiriting:'))
# son2=int(input('Ikkinchi sonni kiriting:'))

# yigindi= son1+son2
# kopaytma = son1*son2
# if kopaytma<=1000:
#     print(f'Ikki son kopaytmasi {kopaytma}ga teng')
# else:
#     print(f'Sonlar yigindisi:{yigindi}ga teng')

# 5 *. Agar foydalanuvchi tergan son 5 ga qoldiqsiz bo’linsa “Hello” yozuvini konsolga chiqaradigan aks holda
# “Bye” yozuvini chiqaradigan dastur yozing.

# son = int(input('Sonni kiriting:'))
# if son%5==0:
#     print('Hello ')
# else:
#     print('Bye')

# 6 **. Foydalanuvchidan yil terilishini so’raydigan yil kabisa ekanligini aniqlaydigan dasturni yozing.
# Grigorian kalendarga ko’ra yil kabisa hisoblanadi agar yil 4 ga qoldiqsiz bo’linsa va 100 ga bo’linmasa 
# yoki 400 ga qoldiqsiz bo’linsa.

# yil = int(input('Yilni kiriting: '))
# if yil%4==0 and yil%100!=0 or yil%400==0:
#     print(f"{yil}-yil Kabisa yili")
# else:
#     print('Yashasa boladigan yil')   
    
# # 7 **. Shokoladka to’g’ri to’rtburchak shaklga ega va kengligi x uzunligi bolgan to’rtburchak shakllarga bo’lingan.
# Shokoladni bir martta to’g’ri chiziq bo’yicha ikki qismga sindirsa bo’ladi.Aynan x bo’lakdan iborat shokolad bo’lagini
#  shu tarzda sindirish mumkinligini aniglang.Dastur kirish sifatida uchta sonni qabul qiladi: kenglik, uzunlik, qismlar
#  va YES yoki NO yozuvini konsolga chiqarish kerак.

# x= int(input('Kengligini kiriting:'))
# y= int(input('Uzunligini kiriting:'))

# qism= int(input('Nechta qismdan iborat: '))

# if qism==x*y:
#     print('YES')
# else:
#     print('NO')






































































