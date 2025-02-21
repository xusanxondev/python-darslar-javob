
# 1. Sevimli taomlariz ro’yxatini yarating.Do’stingiz sevimli taomlari ro’yxatini yarating o’zizning 
#ro’yxatingizni kopiya qilib.Har bir ro’yxatga bittadan xar xil taom qo’shib ushbu ikkita ro’yxat 
#xar xil ekanligiga amin bo’ling.Konsolga ushbu ikkita ro’yxatni chiqaring.


# taom =['osh','kabob','jaz','stake','lavaw']
# taom_dost=taom.copy()

# taom_dost.append('shorva')
# taom.append('lagmon')

# print(taom_dost)
# print(taom)


# 2. Foydalanuvchidan son qabul qiladigan user_name o’zgaruvchini yarating.    
# Sonlardan tashkil topgan ro’yxatni yarating 1 dan boshlab user_name qiymatigacha
#(user_name o’zgaruvchi qiymati ushbu ro’yxatga kirsin).Konsolga ro’yxatni chiqaring va sonlar yig’indisini.

# user_name =int(input('Son kiriting: '))

# son_royxat=list(range(user_name))
# son_royxat.append(user_name)
# y=sum(son_royxat)

# print(son_royxat)
# print(f'Sonlar yigindisi:{y} ga teng')


# 3. Ikkita sonlar ro’yxatini yarating 1 dan 100 gacha.Birinchisi faqat juft sonlardan iborat bo’ladi ikkinchisi 
#faqat toq sonlardan iborat bo’ladi.Ushbu ro’yxatlarni konsolga chiqaring va sonlar yig’indisini.

# juft=[i for i in range(0,100,2)]
# toq=[i for i in range(1,100,2)]

# print(juft)
# print(toq)
# print('yigindi juftlar:', sum(juft))
# print('yigindi toqlar:', sum(toq))

# 4. Ro’yxatdagi xar bir juft sonni konsolga chiqaradigan va son 815 ga teng bo’lganda to’xtaydigan dasturni yozing.

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 
# 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 
# 379, 843, 831, 445, 742, 717, 958,743, 527]

# juft=[]
# for i in numbers:
#     if i==815:
#         break
#     elif i%2==0:
#         juft.append(i)
# print(juft)


# 5. Sondagi raqamlar sonini sanaydigan dastur yarating.
# Masalan 75869 soni, shuning uchun raqamlar soni 5.

# s=len(input('son kiriting: '))
# print('Raqamlar soni:',s)


s=int(input('son kiriting: '))
a=s.alpha()
print(a)























