#a = 'abay'
#print("a")

#avtolar = ['audi','bmw','volvo','kia','hyundai']
#for avto in avtolar:
#    if avto == 'bmw':
#     print(avto.upper())
#    else:
#     print(avto.title())

#ism = 'Ali'
#ism.lower() == 'ali'

#ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
#if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
#else:
#    print("Salom, Ali")

#ish = "Nonvoy"
#ish.lower() == "nonvoy"

#ish = input("Nima ish qilasiz?>>>")
#if ish.lower() != "nonvoy":
#     print(f"Uzur, {ish.title()} bizga nonvoylar kerak")
#else:
#   print("Salom hamkasb")

#javob = float(input("12x6 nechiga teng?>>>"))
#if javob!=72:
#    print("Javob xato!")
#else:
#    print('javob togri')

#login = input("Yangi login tanlang:")
#if len(login)<=5: # login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart!")
##else:
#    print("togri")

#qop = int(input("nechi qop yopasiz kuniga?>>>"))
#if qop <3:
 #   print(f"siz {qop*250} ta yopasiz ekanku eng kamida 3 qop yopishiz kk bratiwka")
#else:
 #   print("qoil szga oga sz eng zorisiz islom aka")


#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 2024-yil<18: # foydalanuvchining yoshini hisoblaymiz
#    print(f"Yoshingiz {2020-yil}da ekan.")
#    print("Kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")

#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
#else:
#    print("kichkina ekansiz")

#x, y = 5, 2 # x=25 va y=50
#print("x>y") if x>y else print("x<y")


#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#   if car == 'gm':
 #    print(car.upper())
 #   else:
 #    print(car.title())

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
 #   if car != 'gm':
 #    print(car.title())
 #   else:
  #   print(car.upper())


#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
#"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" 
# matnini konsolga chiqaring.

#login = input("iltimos login kiriting/>>>")
#if login.lower() != 'admin':
 #   print(f"Xush kelibsiz,{login}!")
#else: 
#     print(input("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"))


#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting:"))
#if x==y: print(f"Sonlar teng: {x}={y}")
#else:
#4    print("xato")

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting:"))
#if x!=y:  print(f"siz tanlagan sonlar birinchi teng: {x}, ikinchi teng: {y}")
#else:
#   print("notogri sonlar bir biriga teng emas bolsin")

#Foydalanuvchidan istalgan son kiritishni so'rang.
#Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa
# "Musbat son" degan xabarni chiqaring.

#x = int(input("istalgan sonni kiriting: "))
#if x >= 0:
#    print("musbat son")
#else:
#    print("manfiy son")


#Foydalanuvchidan son kiritishni so'rang,
#agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
#Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.

# x = float(int(input("istalgan sonni kiriting: ")))
# if x>= 0:
#     print(f"axa {x}, siz tanlagan son ildizi: {x**0.5}")
# else:
#     print("musbat son kiriting: ")




# yosh= int(input('yoshingiz nechida?'))
# if yosh<=4:
#     print("sizga kirish bepul")
# elif yosh<=12:
#     print("sizga kirish 5000 som")
# elif yosh<18:
#     print("sizga kirish 8000 som")
# elif yosh>=60:
#     print("sizga kirish bepul")
# else:
#     print("sizga kirish 10000 som")

# kun = input("bugun nma kun?>>>")
# if kun.lower()=="shanba " or kun.lower()=="yakshanba":
#     print("bugun dam olish kuni")
# else:
#     print("bugun ish kuni")

# kun = input("bugun nma kun?>>>")
# harorat = float(input("havo harorati qanday? "))

# if (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat>=30:
#     print("chomilgani kettik ")
# elif (kun.lower()!="yakshanba" or kun.lower()!="shanba")  and harorat>=30:
#     print("ish kuni")
# elif (kun.lower()=="yakshanba" or "shanba") and harorat<30:
#     print("uyda dam olamiz")


# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

  
# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = 1 # mijoz choy ham oldi
# salat = 1 # mijoz salat olmadi
# non = 1

# if choy: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz
# if salat:
#     narh = narh + 7000
# if non:
#     narh= narh + 8000
# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')



# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik", "norin"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

# cars =["MERS","BMW","GM","Toyota","HONDA"]
# zakaz =['Lasetti','bmw',"mers", "GM", 'honda']

# for car in zakaz:
#     if car in cars:
#         print(f"Carsda {car} bor wepim")
#     else:
#        print(f"uzur wep {car}, yokanu")     


# Foydalanuvchidan ikita son kiritishni sorang, 
# sonlarni solishtiring va ularning 
# teng yoki katta/kichikligi haqida xabarni chiqaring



# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting:"))
# if x==y: print(f"Sonlar teng: {x}={y}")
# if x>y: print(f"{x} kottta {y} dan")
# if x<y: print(f"{y} kottayu okaxon {x} dan")



# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")


# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 
# 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda 
# bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q 
# mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas 
# ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" 
# degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." 
# degan xabarni chiqaring.




# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# print(savat)

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q:")
#    for mahsulot in mavjud_emas:
#      print(mahsulot)
     
# if bor_mahsulotlar:
#     if len(bor_mahsulotlar) == len(savat):
#        print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#     else:
#        print("ushbu mahsulotlar mavjud:")  
#        for mahsulot in bor_mahsulotlar:
#            print(mahsulot)
   
# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login.lower() in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

  
    

# numbers = [1,2,3,4]

# if numbers:
#     for number in numbers:
#         print(number)


# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


# yosh = int(input("yoshingiz necchida?: "))
# oylik = int(input("oylik daromadingiz qancha($) da ? "))
# ish_tajriba = int(input("Ish tajribangiz qancha yil? "))

# if yosh>30 and oylik>5000 and ish_tajriba>5:
#     print("Boshqaruvchiga mos keldingiz tabriklaymiz!")
# else:
#     print("Afsuski mos kelmaysiz")
    

# bir= int(input("birinchi burchak"))
# ikki = int(input("ikkinchi burchak"))
# uch = int(input("uchinchi burchak"))
# jami= bir+ikki+uch
# if  jami==180:
#     print("togri uchburchak")
# else:
#    print("xato burchaklar")     


# prices = []
# for i in range(4):
#     price = int(input(f"{i+1}-tovar narxini kiriting: "))
#     prices.append(price)

# total_price = sum(prices)

# if total_price > 10000:
#     discount = 0.3
# elif total_price > 5000:
#     discount = 0.2
# elif total_price > 1000:
#     discount = 0.1
# else:
#     discount = 0

# final_price = total_price * (1 - discount)
# print(f"Umumiy narx: {total_price}")
# print(f"Chegirma: {discount * 100}%")
# print(f"Chegirmali narx: {final_price}")

#print("hello world")

# car_0 = {'model':'ferrari','rang':'qizil'}
# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")

# talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
#talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 

# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson
#  haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili
#   va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning 
#   ismi Mavlutdin, 
# 1954-yilda, Samarqand viloyatida tug'ilgan

# otam_0 = { 
#     'ism':'maxamadjon',    
#      't_yili':1964,
#      't_shahri':'qoqon',
#      'manzili':'olmurod',
# #      'ish':'pensiya'
# #         }
# ismi = ['ism']
# t_yili=['t_yili']
# t_shahar=['t_shahri']
# manzil =['manzili']
# ish= ['ish']

# print(f"Otamning ismlari {ismi.title()}, u\
#       {t_yili}-yilda,{t_shahar.title()}\
#       shaharida tug'ilgan {manzil.title} qishlog'ida yashaydi, hozirda\
#       {ish}da")

# otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
# tyil = otam['tyil']
# vil = otam['viloyat']
# print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")


# Oila a'zolaringizning sevimli taomlari lug'atini tuzing.
#  Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining 
#  sevimli taomini konsolga chiqaring: Alining sevimli taomi osh


# oila ={
#        'dadam':'osh',
#        'onam':'manti',
#        'akam':'xonim',
#        'apam':'shashlik'
#        }
# dadam = oila['dadam']
# onam = oila['onam']
# akam= oila['akam']
# apam= oila['apam']

# #print(f"Dadamning sevimlim taomi {dadam.title()},\
#       # Onamning sevimli taomi {onam.title()},\
#       # Akamning sevimli taomi {akam.title()},\
#       # Apamning sevimli taomi {apam.title()}")

# print(f" Maqtanishmasu abetga {apam.title()} yedim ")


# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     'husan':"mastava",
#     'olim':"somsa"
#     }

# taom = taomlar['ali']
# print(f"Alining sevimli taomi {taom}")


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# print(savat)

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q:")
#    for mahsulot in mavjud_emas:
#      print(mahsulot)
     
# if bor_mahsulotlar:
#     if len(bor_mahsulotlar) == len(savat):
#        print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#     else:
#        print("ushbu mahsulotlar mavjud:")  
#        for mahsulot in bor_mahsulotlar:
#            print(mahsulot)



# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning 
# tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa,
#  "Bunda so'z mavjud emas" degan xabarni chiqaring.


# uz_en ={
#         'non':'bread',
#         'olma':'apple',
#         'qizil':'red',
#         'nonvoy':'baker'
#         }

# soz = input("biror soz yozing tarjima qilib beraman!>>> ").lower()
# print(uz_en.get(soz,"bunday soz mavjud emas!"))

# soz = input("biror soz yozing tarjima qilib beraman!>>> ").lower()
# tarjima= uz_en.get(soz)
# if tarjima==None:
#     print("bunday soz yoq!")
# else:
#     print(f"{soz.title()} sozi {tarjima} deyiladiku brat")


# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    

# poytaxtlar={
#    'uzbekiston':'tashkent',
#    'aqsh':'washington',
#     'japan':'tokyo',
#    'kazahstan':'astana'
#     }
# mamlakat=input("mamlakat nomini kiriting!.")

# print(poytaxtlar.get(mamlakat,"bu mamlakat yoq"))



# # Lug‘atga fanlar va o‘qituvchilarni kiritish
# subjects = {
#     "Matematika": "Akbarov",
#     "Fizika": "Rahimova",
#     "Ingliz tili": "Johnson",
#     "Tarix": "Karimov",
#     "Biologiya": "Nazarova"
# }

# # Foydalanuvchidan fan nomini so‘rash
# subject_name = input("Fan nomini kiriting: ").title()

# # Lug‘atda mavjudligini tekshirish
# if subject_name in subjects:
#     print(f"O‘qituvchi: {subjects[subject_name]}")
# else:
#     print("Bu fan bo‘yicha ma'lumot yo'q.")




# # Mamlakatlar va poytaxtlar lug'ati
# mamlakat_poytaxt = {
#     "O'zbekiston": "Toshkent",
#     "Rossiya": "Moskva",
#     "AQSh": "Vashington",
#     "Xitoy": "Pekin",
#     "Fransiya": "Parij",
#     "Yaponiya": "Tokio",
#     "Braziliya": "Brasilia",
#     "Misr": "Qohira",
#     "Germaniya": "Berlin",
#     "Kanada": "Ottava"
# }

# # Foydalanuvchidan mamlakat nomini so'rash
# mamlakat_nomi = input("Mamlakat ismini kiriting: ").title()

# # Mamlakatning poytaxtini chiqarish
# if mamlakat_nomi in mamlakat_poytaxt:
#     print(f"{mamlakat_nomi}ning poytaxti {mamlakat_poytaxt[mamlakat_nomi]}")
# else:
#     print("Bunday mamlakat mavjud emas.")




# ism_taom = {
#     "Maxamadjon":"osh",
#     "Bogidagul":"manti",
#     "Mirolimjon":"shashlik",
#     "Xusnidaxon":"norin",
#     "Xusanxon":"xonim",
#     "Zikrillox":"xonim",
#     "Frdavsxon":"osh yonida soki bilan yeysiz"
#     }

# ism= input("Menga ismingizni yozing va siz yoqtirgan taomni aytaman! ").title()
# taom= ism_taom.get(ism)#"bunday ism yoq")

# if ism in ism_taom:
#     print(f"{ism} siz yoqtirgan taom {taom.title()}")
# else:
#     print("Bunday ismli oiala azosi yoq")


# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
#  Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.


# foydalanuvchilar =['xasan','xusan','asad','sobir','suxrob']

# login=input("Yangi login tanlang!> ")

# if login in foydalanuvchilar:
#     print("Bunday login mavjud boshqa tanlang!" )
# else:
#     print("Xush kelibsiz, foydalanuvchi!")
    

# mahsulotlar degan ro'yxat yarating va kamida 5 ta turli mahsulotni kiriting.
#  Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida
#  4 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring 
#  va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
#  "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q
#  mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
#  "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa 
#  "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.





# mahsulotlar=['olma','banan''kola','fanta','non','choy','salat','sut','tuz''karam','behi']
# savat=[]

# for n in range(4):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulot =[]
# yoq_mahsulot=[]
        
# for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#         bor_mahsulot.append(mahsulot)
#    else:
#         yoq_mahsulot.append(mahsulot)

# if yoq_mahsulot:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in yoq_mahsulot:
#     print(mahsulot) 
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
 


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# if bor_mahsulotlar:
#   print("bular esa bor") 
#   for mahsulot in bor_mahsulotlar :
#       print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    




# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# # print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")
  

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")



# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# # print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())


# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")





# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")    
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())


# print(telefonlar.values())

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }
# # 
# # print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# # for tel in telefonlar.values():
# #     print(tel)

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)


# toys = {'ball',"cars","lolo","cars"}
# print(type(toys))


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# for k, q in sorted(telefonlar.items()):
    
#     print(f"ismi: {k.title()}")
    
#     print(f"telefoni: {q} \n")



# mamlakat_poytaxt = {
#     "O'zbekiston": "Toshkent",
#     "Rossiya": "Moskva",
#     "AQSh": "Vashington",
#     "Xitoy": "Pekin",
#     "Fransiya": "Parij",
#     "Yaponiya": "Tokio",
#     "Braziliya": "Brasilia",
#     "Misr": "Qohira",
#     "Germaniya": "Berlin",
#     "Kanada": "Ottava"
#        }
# #for mamlakat in mamlakat_poytaxt:
# #print(mamlakat_poytaxt.keys())

# for k,q in sorted(mamlakat_poytaxt.items()):
#     print(f"Davlat: {k}")
#     print(f"Poytaxti: {q} \n")



# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini 
# konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.


# mamlakat_poytaxt = {
#     "O'zbekiston": "Toshkent",
#     "Rossiya": "Moskva",
#     "AQSh": "Vashington",
#     "Xitoy": "Pekin",
#     "Fransiya": "Parij",
#     "Yaponiya": "Tokio",
#     "Braziliya": "Brasilia",
#     "Misr": "Qohira",
#     "Germaniya": "Berlin",
#     "Kanada": "Ottava"
#        }

# mamlakat= input("mamlakatni kiriting!: ").title()
# if mamlakat in mamlakat_poytaxt:
#    print(f"{mamlakat} poytaxti: {mamlakat_poytaxt[mamlakat]}")
# else:
    # print(f"Bunday {mamlakat} dgani yo'q shepim")



# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
#  Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
#  taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
#  aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

# menu_narx={
#     'non':5000,
#     'choy':2000,
#     'qiyma':7000,
#     'jaz':12000,
#     'salat':10000,
#     'qatiq':4000,
#     'limonchoy':8000,
#     'patir':8000,
#     'chuchvara':25000,
#     'lag\'mon':20000,
#     'lavash':30000,
#     'pitsa':25000,
#     'xotdog':15000,
#     'osh':
#     }
# print('3 ta taom buyurtma bering.')
# taom=[]

# for n in range(3):
#     taom.append(input(f"Marhamat {n+1}-zakazni bering: "))
    
# print(taom)    
   
# for zakaz in taom:
#    if zakaz in menu_narx:
#        print(f"Bu {zakaz} narxi: {menu_narx[zakaz]} so'm")
       
# for zakaz in taom:
#     if zakaz not in menu_narx:
#         print(f"Bizda bunday {zakaz} yo'q")
       
       
       
# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")
       
       
# ona_bola = {
#     'Xusnidaxon':'Zikrillox',
#     'Mirolimjon':'Firdavsxon'
#     }
# ism = input("Ismizni yozing!: ")
# print(f"Sizning farzandingiz: {ona_bola[ism]} ")
 


# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta 
# mashxur shaxlar haqidagi ma'lumotlarni lug'at
# ko'rinishida saqlang. Lug'atlarni bitta
# ro'yxatga joylang, va har bir shaxs haqidagi
# ma'lumotni konsolga chiqaring.

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# adabiyotchilar= [buxoriy,qodiriy,vohidov,navoiy]

# #for adib in adabiyotchilar:
# #print(f"{adabiyotchilar[1]['ism']}  {adabiyotchilar[0]['tyil]}-yilda ") 

# print(f"{adabiyotchilar[0]['ism']} {adabiyotchilar[0]['tyil']}-yilda,"
#       f" {adabiyotchilar[0]['tjoy']} shahrida tug'ildi,"
#       f" {adabiyotchilar[0]['vyil']}-yilda vafot etdi.")


# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }


# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)


# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
#     Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida 
#     lug'artga saqlang. Natijani konsolga chiqaring.

# dost_kinolari={
#     "hasan":"[]",
#     "husan":"[]",
#     "fotima":"[]"
#     }
# print("3ta kino yozing")
# for n in range(3):
#     dost_kinolari.append(input(f"{n+1}-yoqtirgan kinoni yozing: "))


# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }
# for ism, kinolar in kinolar.items():
#    print(f"\n{ism.title()}ning sevimli kinolari:") 
#    for kino in kinolar:
#        print(kino)


# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)


# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
# ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni
#  konsolga chiqaring.


# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
    # }
# for davlat, malumotlar in davlatlar.items():
#     print(f"\n{davlat.upper()} haqida qisqachha:")
#     for malumot in malumotlar:
#         print(f"{malumot.title()}: {malumotlar[malumot]}")

# *******





# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]


# # Har bir shaxs haqida ma'lumot chiqarish
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tugilgan_yil = shaxs['tyil']
#     vafot_yil = shaxs['vyil']
#     tugilgan_joy = shaxs['tjoy']
#     yosh = vafot_yil - tugilgan_yil
    
#     print(f"{ism} {tugilgan_yil}-yilda {tugilgan_joy}da tug‘ilgan. "
#           f"{vafot_yil}-yilda vafot etgan. Umri {yosh} yil bo‘lgan.")






# ******




# # shaxs = input("adib nomini kiriting?:")

# # #if shaxs in shaxslar:
# # if shaxs == shaxslar[0]:
# #     print(f"{shaxs['ism']} {shaxs['tyil']}-yilda "
# #           f"{shaxs['tjoy']}da tugilgan va "
# #           f"{shaxs['vyil']}-yilda vafot etgan")
# # else:
# #     print('xato')
            


# *******


# Adiblar haqida ma'lumotlar
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil', 'tyil':810, 'vyil':870, 'tjoy':'Buxoro'}
# qodiriy = {'ism':'Abdulla Qodiriy', 'tyil':1894, 'vyil':1938, 'tjoy':'Toshkent'}
# vohidov = {'ism':'Erkin Vohidov', 'tyil':1936, 'vyil':2016, 'tjoy':"Farg'ona"}
# navoiy = {'ism':'Alisher Navoiy', 'tyil':1441, 'vyil':1501, 'tjoy':"Xirot"}

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# # Foydalanuvchidan adib nomini so‘rash
# adib_nomi = input("Biror adib nomini kiriting: ")

# # Adib haqida ma'lumot topish
# topildi = False
# for shaxs in shaxslar:
#     if adib_nomi.lower() in shaxs['ism'].lower():
#         topildi = True
#         ism = shaxs['ism']
#         tugilgan_yil = shaxs['tyil']
#         vafot_yil = shaxs['vyil']
#         tugilgan_joy = shaxs['tjoy']
#         yosh = vafot_yil - tugilgan_yil
        
#         print(f"{ism} {tugilgan_yil}-yilda {tugilgan_joy}da tug‘ilgan. "
#               f"{vafot_yil}-yilda vafot etgan. Umri {yosh} yil bo‘lgan.")
#         break

# if not topildi:
#     print("Kechirasiz, siz kiritgan adib haqida ma'lumot topilmadi.")



# # Adiblar haqida ma'lumotlar
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil', 'tyil':810, 'vyil':870, 'tjoy':'Buxoro'}
# qodiriy = {'ism':'Abdulla Qodiriy', 'tyil':1894, 'vyil':1938, 'tjoy':'Toshkent'}
# vohidov = {'ism':'Erkin Vohidov', 'tyil':1936, 'vyil':2016, 'tjoy':"Farg'ona"}
# navoiy = {'ism':'Alisher Navoiy', 'tyil':1441, 'vyil':1501, 'tjoy':"Xirot"}

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# # Foydalanuvchidan adib nomini so‘rash
# adib_nomi = input("Biror adib nomini kiriting: ")

# # Adib haqida ma'lumot topish
# topildi = False
# for shaxs in shaxslar:
#     if adib_nomi.lower() in shaxs['ism'].lower():
#         topildi = True
#         ism = shaxs['ism']
#         tugilgan_yil = shaxs['tyil']
#         vafot_yil = shaxs['vyil']
#         tugilgan_joy = shaxs['tjoy']
#         yosh = vafot_yil - tugilgan_yil
        
#         print(f"{ism} {tugilgan_yil}-yilda {tugilgan_joy}da tug‘ilgan. "
#               f"{vafot_yil}-yilda vafot etgan. Umri {yosh} yil bo‘lgan.")
#         break

# if not topildi:
#     print("Kechirasiz, siz kiritgan adib haqida ma'lumot topilmadi.")




# # Adiblar haqida ma'lumotlar
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil', 'tyil':810, 'vyil':870, 'tjoy':'Buxoro'}
# qodiriy = {'ism':'Abdulla Qodiriy', 'tyil':1894, 'vyil':1938, 'tjoy':'Toshkent'}
# vohidov = {'ism':'Erkin Vohidov', 'tyil':1936, 'vyil':2016, 'tjoy':"Farg'ona"}
# navoiy = {'ism':'Alisher Navoiy', 'tyil':1441, 'vyil':1501, 'tjoy':"Xirot"}

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# # Foydalanuvchidan adib nomini so‘rash
# adib_nomi = input("Biror adib nomini kiriting: ")

# # Adib haqida ma'lumot topish
# topildi = False
# for shaxs in shaxslar:
#     if adib_nomi.lower() in shaxs['ism'].lower():
#         topildi = True
#         ism = shaxs['ism']
#         tugilgan_yil = shaxs['tyil']
#         vafot_yil = shaxs['vyil']
#         tugilgan_joy = shaxs['tjoy']
#         yosh = vafot_yil - tugilgan_yil
        
#         print(f"{ism} {tugilgan_yil}-yilda {tugilgan_joy}da tug‘ilgan. "
#               f"{vafot_yil}-yilda vafot etgan. Umri {yosh} yil bo‘lgan.")
#         break

# if not topildi:
#     print("Kechirasiz, siz kiritgan adib haqida ma'lumot topilmadi.")


# # Adiblar haqida ma'lumotlar
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil', 'tyil':810, 'vyil':870, 'tjoy':'Buxoro'}
# qodiriy = {'ism':'Abdulla Qodiriy', 'tyil':1894, 'vyil':1938, 'tjoy':'Toshkent'}
# vohidov = {'ism':'Erkin Vohidov', 'tyil':1936, 'vyil':2016, 'tjoy':"Farg'ona"}
# navoiy = {'ism':'Alisher Navoiy', 'tyil':1441, 'vyil':1501, 'tjoy':"Xirot"}

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# # Foydalanuvchidan adib nomini so‘rash
# adib_nomi = input("Biror adib nomini kiriting: ").lower()

# # Adib haqida ma'lumot topish
# topildi = False
# for shaxs in shaxslar:
#     # Ismni to'liq ismdan oxirgi bo'lakni olish orqali tekshirish
#     if adib_nomi in shaxs['ism'].lower().split()[-1]:
#         topildi = True
#         ism = shaxs['ism']
#         tugilgan_yil = shaxs['tyil']
#         vafot_yil = shaxs['vyil']
#         tugilgan_joy = shaxs['tjoy']
#         yosh = vafot_yil - tugilgan_yil
        
#         print(f"{ism} {tugilgan_yil}-yilda {tugilgan_joy}da tug‘ilgan. "
#               f"{vafot_yil}-yilda vafot etgan. Umri {yosh} yil bo‘lgan.")
#         break

# if not topildi:
#     print("Kechirasiz, siz kiritgan adib haqida ma'lumot topilmadi.")


# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }




# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]

# shaxs =input("adib kiriting:")
# info = shaxslar[shaxs]
# if shaxs in shaxslar:
# #    info == shaxslar[shaxs]
#     if info == shaxslar.get:
#         print(f"{info['ism']} {info['tyil']}-yilda "
#          f"{info['tjoy']}da tugilgan va "
#         f"{info['vyil']}-yilda vafot etgan")
#     else:
#         print('xato')
#======================================================================

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#             'tyil':810,
#             'vyil':870,
#             'tjoy':'Buxoro',
#             'nomi':'buxoriy'
#             }

# qodiriy = {'ism':'Abdulla Qodiriy',
#             'tyil':1894,
#             'vyil':1938,
#             'tjoy':'Toshkent',
#             'nomi':'qodiriy'
#             }

# vohidov = {'ism':'Erkin Vohidov',
#             'tyil':1936,
#             'vyil':2016,
#             'tjoy':"Farg'ona",
#             'nomi':'vohidov'
#             }

# navoiy = {'ism':'Alisher Navoiy',
#             'tyil':1441,
#             'vyil':1501,
#             'tjoy':"Xirot",
#             'nomi':'navoiy'
#             }

# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]

# shaxs= input("adabiyotchilardan birini yozing: ")
# for info in shaxslar:
#    if shaxs==info['nomi']:
#     print(f"{info['ism']} {info['tyil']}-yilda "
#                 f"{info['tjoy']}da tugilgan va "
#                 f"{info['vyil']}-yilda vafot etgan")

#==========================================================================


# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())



# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]

# shaxs= input("adabiyotchilardan birini yozing: ")

# for shaxs in shaxslar:
#    if shaxs==shaxslar[3]:
#       print(f"{shaxs['ism']} {shaxs['tyil']}-yilda "
#           f"{shaxs['tjoy']}da tugilgan va "
#           f"{shaxs['vyil']}-yilda vafot etgan")




# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#             'tyil':810,
#             'vyil':870,
#             'tjoy':'Buxoro'
#             }

# qodiriy = {'ism':'Abdulla Qodiriy',
#             'tyil':1894,
#             'vyil':1938,
#             'tjoy':'Toshkent'
#             }

# vohidov = {'ism':'Erkin Vohidov',
#             'tyil':1936,
#             'vyil':2016,
#             'tjoy':"Farg'ona"
#             }

# navoiy = {'ism':'Alisher Navoiy',
#             'tyil':1441,
#             'vyil':1501,
#             'tjoy':"Xirot"
#             }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# shaxs_nomi = input("Adabiyotchilardan birini yozing: ")


# topildi = False
# for shaxs in shaxslar:
#     if shaxs_nomi in shaxslar[0:]:
#         print(f"{shaxs['ism']} {shaxs['tyil']}-yilda {shaxs['tjoy']}da tug'ilgan va {shaxs['vyil']}-yilda vafot etgan.")
#         topildi = True
#         break

# if not topildi:
#     print("Kiritilgan adib haqida ma'lumot topilmadi.")



# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#             'tyil':810,
#             'vyil':870,
#             'tjoy':'Buxoro'
#             }

# qodiriy = {'ism':'Abdulla Qodiriy',
#             'tyil':1894,
#             'vyil':1938,
#             'tjoy':'Toshkent'
#             }

# vohidov = {'ism':'Erkin Vohidov',
#             'tyil':1936,
#             'vyil':2016,
#             'tjoy':"Farg'ona"
#             }

# navoiy = {'ism':'Alisher Navoiy',
#             'tyil':1441,
#             'vyil':1501,
#             'tjoy':"Xirot"
#             }

# shaxslar = {
#     "buxoriy": buxoriy,
#     "qodiriy": qodiriy,
#     "vohidov": vohidov,
#     "navoiy": navoiy
# }


# shaxs_nomi = input("Adabiyotchilardan birini yozing: ").lower()


# if shaxs_nomi in shaxslar:
#     shaxs = shaxslar[shaxs_nomi] 
#     print(f"{shaxs['ism']} {shaxs['tyil']}-yilda {shaxs['tjoy']}da tug'ilgan va {shaxs['vyil']}-yilda vafot etgan.")
# else:
#     print("Kiritilgan adib haqida ma'lumot topilmadi.")



# buxoriy = {'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil': 810,
#            'vyil': 870,
#            'tjoy': 'Buxoro'}

# qodiriy = {'ism': 'Abdulla Qodiriy',
#            'tyil': 1894,
#            'vyil': 1938,
#            'tjoy': 'Toshkent'}

# vohidov = {'ism': 'Erkin Vohidov',
#            'tyil': 1936,
#            'vyil': 2016,
#            'tjoy': "Farg'ona"}

# navoiy = {'ism': 'Alisher Navoiy',
#           'tyil': 1441,
#           'vyil': 1501,
#           'tjoy': "Xirot"}

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# ism_input = input("Adabiyotchilardan birini yozing: ").lower()

# indexes = []
# for index, shaxs in enumerate(shaxslar):
#     if ism_input in shaxs['ism'].lower():
#         indexes.append(index)

# if indexes:
#     for index in indexes:
#         data = shaxslar[index]
#         print(f"Data: {data}")





# buxoriy = {'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil': 810,
#            'vyil': 870,
#            'tjoy': 'Buxoro'}

# qodiriy = {'ism': 'Abdulla Qodiriy',
#            'tyil': 1894,
#            'vyil': 1938,
#            'tjoy': 'Toshkent'}

# vohidov = {'ism': 'Erkin Vohidov',
#            'tyil': 1936,
#            'vyil': 2016,
#            'tjoy': "Farg'ona"}

# navoiy = {'ism': 'Alisher Navoiy',
#           'tyil': 1441,
#           'vyil': 1501,
#           'tjoy': "Xirot"}

# shaxslar = ['buxoriy', 'qodiriy', 'vohidov', 'navoiy']

# #shaxslar_names = ['buxoriy', 'qodiriy', 'vohidov', 'navoiy']

# ism_input = input("Adabiyotchilardan birini yozing; ").lower()

# if ism_input in shaxslar:
#     index = shaxslar.index(ism_input)
#     data = shaxslar[index]

#     print(f"\n Topilgan ma'lumot: ")
#     print(f"Ism: {data['ism']}")
#     print(f"Tug'ilgan yili: {data['tyil']}")
#     print(f"Vafot etgan yili: {data['vyil']}")
#     print(f"Tug'ilgan joyi: {data['tjoy']}")
#print(shaxslar[0])



# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# for malibu in malibus[6:]:
#     malibu['korobka']='mexanika'
#     malibu['rang']= 'qora'
# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
# for malibu in malibus:
#     if malibu['korobka']=='mexanika':
#         malibu['narh']=35000
# for malibu in malibus:
#     print(malibu)


# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f'{til.upper()} ', end='')

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(f'{til.upper()} ', end ='')
#######################################################################################



# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':['Otkan kunlar','Mehrobdan Chayon','Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# #Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# # ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
# #va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

# for shaxs in shaxslar:
#     print(f"\n"
#           f"\n{shaxs['ism']} {shaxs['tyil']}-da {shaxs['tjoy']}da tug'ildi "
#           f"va {shaxs['vyil']}-da vafot etdi "
#           f"\nUning mashhur asarlari: ", end='')
#     for asar in shaxs['asarlar']:
#         print(f'{asar}, ' ,end='')
    

###################################################

# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# ism_input = input("Ismizni yozing: ")
# #for ism_input in kinolar:
# if ism_input in kinolar:
#     kino=kinolar[ism_input]
#     print(f"{ism_input.title()} siznining sevimli kinoingiz:")
#     for k in kino:
#         print(f"{k} ", end='')
# else:
#     print("Notog'ri ism yozdingiz!")
 ################
#         # for ism ,kinolar in kinolar.items():
#         #     print(f"\n {ism.title()}ning sevimli kinolari:", end='')
#         #     for kino in kinolar:
#         #         print(f'{kino} ', end ='')
   
#####################################################

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# davlat_input= input("Davlat nomini kiriting: ")

# if davlat_input in davlatlar:
#     info=davlatlar[davlat_input]
#     if davlat_input=='aqsh':
#         print(f"\n{davlat_input.upper()}ning poytaxti {info['poytaxt'].title()} shahri."
#           f" Maydoni {info['maydon']} kv.km aholisi {info['aholi']} kishi"
#           f" pul birligi: '{info['pul birligi']}'")
#     else:
#         print(f"\n{davlat_input.title()}ning poytaxti {info['poytaxt'].title()} shahri."
#           f" Maydoni {info['maydon']} kv.km aholisi {info['aholi']} kishi"
#           f" pul birligi: '{info['pul birligi']}'")
# else:
#     print("Bunday davlat nomi yo'q")



# # for davlat in davlatlar:
# #     info=davlatlar[davlat]
# #     print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()} shahri."
# #          f" Maydoni {info['maydon']} kv.km aholisi {info['aholi']} kishi"
# #           f" pul birligi: '{info['pul birligi']}'")



# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz
# print(height)




#################------WHILE------###########################
# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
   

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
    


# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")



# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")



# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)





# savol ="\n Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = int(input(savol))
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


####################---MASALA-(1)--################################
# Foydalanuvchiidan yaxshi ko'rgan kitoblarini kiritishni 
# so'rang. Foydalanuvchi stop so'zini yozishi bilan 
# dasturni to'xtating

# savol = "\nSevgan kitobingizni kiriting:"
# savol+="(barcha kitoblarni kititib bo'lgach 'stop' deb yozing)"

# kitoblar=[]
# kitob=''
# while True:
#     kitob =input(savol)
#     if kitob !='stop':
#        kitoblar.append(kitob)
#     if kitob=='stop':
#         break
    
# print(f"siz yoqtirgan kitoblar: {kitoblar} ")
######################################

# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!')

#############################--MASALA_(2)---#####################

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm,
# 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while 
# tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).


# savol = "Yoshingizni kiriting: "
# yosh=''
# while True:
#     yosh= input(savol)
#     if yosh =='exit' or yosh=='quit':
#       break
#     if int(yosh)<=7:
#         narx=2000
# #        print(f"Sizga kirish {narx} so'm")
#     elif int(yosh)<18:
#         narx=3000
# #        print(f"Sizga kirish {narx} so'm")
#     elif int(yosh)<65:    
#         narx =10000
# #        print(f"Sizga kirish {narx} so'm")
#     elif int(yosh)>65:
#         narx=0
# #        print(f"Sizga kirish bepul")
#     if narx==0:
#         print("Sizga bepul")
#     else:
#         print(f"Sizga kirish {narx} so'm")
        
# print("Raxmat Sog' bo'ling")
        

#################----WHILE_LUGAT---########################

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("\nYana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Yaqin do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print( f"{ism.title() }" , end='')



# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
   
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# #########--MASALA-1--########################
# 1. Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# mahsulotlar={}
# savol="Marhamat mahsulot qo'shing: "
# #savol+=("yana buyurtma kerakmi")
# while True:
#     mahsulot=input(savol)
#     narx=input(f"{mahsulot.title()} narxini yozing: ")
#     mahsulotlar[mahsulot]=int(narx)
#     javob = input("\nYana mahsulot qo'shamizmi? (ha/yo'q)")
#     if javob=='ha':
#         continue
#     else:
#         break
# print("Siz qilgan Menyu:")    
# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot.title()}ning narxi:{narx} so'm")


###################-MASALA-2--######################3

# Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi 
# mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda 
# "Bizda bu mahsulot yo'q" degan xabarni kor'sating.


# buyurtmalar =[]
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}
# savol="Marhamat buyurtma bering: "

# while True:
#     buyurtma=input(savol)
#     buyurtmalar.append(buyurtma)
    
#     if buyurtma not in mahsulotlar:
#         print("Bizda bu mahsulot yo'q")
#         continue
#     elif buyurtma in mahsulotlar:
#         narx=mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} narxi: {narx} so'm")
        
#         javob = input("\nYana mahsulot qo'shamizmi? (ha/yo'q)")
#     if javob=='ha':
#          continue
#     else:
#          break
# print('Raxmat!')    
    
    
 #################################   
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")
    
   ################FUNKISIYA####################################################3 
    
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
        
#salom_ber()


# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('hasan')


# salom_ber()

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")


# # toliq_ism('xusan', 'nabiyev')


# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2025-tugilgan_yil} yoshda")

# # yosh_hisobla('xusan', 2003)

# yosh_hisobla(tugilgan_yil=1997, ism='olim')

# toliq_ism(familiya='hakimov',ism='olim')


# def yosh_hisobla(tugilgan_yil, joriy_yil=2025): # joriy yil uchun st.qiymat 2020
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(2003,)


# def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)


############################################

#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

# ism= input("Ismingizni kiriting: ")

# def salom_ber(ism):
#     """ismni qabul qilib salom beradigan funksiyade"""
#     print(f"Assalomu alaykum hurmatli {ism.title()}!")
    
# salom_ber(ism)
# yosh = int(input(f"{ism.title()} tug'ilgan yilingizni yozing: "))

# def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
#      """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#      print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(yosh)     
     
######################################

# ism= input("Ismingizni kiriting: ")
# yosh = int(input(f"{ism.title()} tug'ilgan yilingizni yozing: "))

# def tyiltop(ism, yosh):
#     print(f"{ism.title()} {2020-yosh} yoshda")

# tyiltop(ism, yosh)

#######################
# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# son=int(input("Istalgan sonni kiriting va men sizga uning kvadrati va kubini hissoblab beraman:"))

# def kv_kub_top(son):
#     """sonning kvadrati va kubini hisoblaydi"""
#     print(f"{son} sonining kvadrati:{son**2}"
#           f"\n{son} sonining kubi:{son**3}")
# kv_kub_top(son)

############################################################## 
#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# son=int(input("Son kiriting:"))

# def juftmi(son):
#     """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2:   #toq son topish
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")

# juftmi(son)
################################################
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring 
# son_1=int(input("Birinchi sonnni kiriting:"))
# son_2=int(input("Ikkinchi sonni kiritiing:"))


##################################################
# def kattani_top(son_1,son_2):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya."""
#     if son_1>son_2:
#         print(f"Birinchi son katta: \n {son_1}>{son_2}")
#     elif son_1==son_2:
#         print(f"Sonlar teng!  \n {son_1}={son_2}")
#     else:
#         print(f"Ikkinchi son katta: \n {son_2}>{son_1}") 
 
# kattani_top(son_1,son_2)  
################################################  
     
# # Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.
# def daraja(x,y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")



# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini 
#tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

# son=int(input("Sonni kiriting: "))
# def bolinish_alomati(son):
#     """Son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for n in range(2,11):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
            
# bolinish_alomati(son)
##################FUNKSIYA(2)##########################333

# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

##################################################

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


###################################################

def oraliq(min,max, step=''):
    sonlar = [] # bo'sh ro'yxat
    ## while min<max:
    ##     sonlar.append(min)
    ##     min += 1
    ##     continue
    if step!='':
        while min<max:
            sonlar.append(min)
            min+=int(step)
    else:
        while min<max:
            sonlar.append(min)
            min += 1   
    return sonlar
print(oraliq(0,10,3))

########################################33
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[]     # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    
     # avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
    
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh= 'nomalum'
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi :{narh}")
            
#   #######################################3      
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili 
# va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy
#  qiling (masalan, tel.raqam, el.manzil)

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
# ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2025-int(tyil),
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz
# mijozlar=[]
# print("Mijozlar malumotlarni tuzamiz:")
# while True:
#     ism=input("Ismingizni kiriting ")
#     familiya=input("Familiyangizni kiriting ")
#     tyil=input("Tug'ilgan yilingizni kiriting ")
#     tjoy=input("Tug'ilgan joyingizni kiriting ")
#     email=input("Email manzil kiriting ")
#     tel=input("Telefon nomeringiz ")

#     mijozlar.append(mijoz_info(ism,familiya,tyil,tjoy,email,tel))
    
#     javob =input("Yana mijoz qo'shasizmi? (ha\yo'q")
#     if javob=='ha':
#         continue
#     else:
#         break
# print("\nBizdagi Mijozlar malumoti (ismi):")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()}")
    
###################--masala(2)--##############################
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va 
# yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

# def aylana_parametrlari(radius,pi=3.1415):
#     aylana={"radius":radius,
#        "diametiri":2*radius,
#        'uzunligi':2*pi*radius,
#        'yuzi':pi*radius**2}
#     return aylana

# aylana_parametrlari(5)

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va 
# # o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# # Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni 
# # qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng 
# # bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb 
# # olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))

# ###############################################################
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)


#############################################
# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta 
# harfga o'zgatiruvchi funksiya yozing.

# Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib 
# o'zgartiring

# def katta_harf(matnlar):
#     k_ismlar=[]
#     for i in range(len(matnlar)):
#             matn=matnlar[i]
#             k_ismlar.append(matn.title())
#     return k_ismlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# k_ismlar=katta_harf(ismlar[:])
# print(ismlar)
# print(k_ismlar)


# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga 
# o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.


# def bahola(ismlar):
#     baholar = {}
#     for i in range(len(ismlar)):
#         ism = ismlar[i]
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)


######################-misollar-##################################

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)


# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)


#1-misol-Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     if sonlar:
#         kopaytma=1
#         for son in sonlar:
#             kopaytma*= son
#     else:
#        kopaytma=[]
#     return kopaytma

# print(summa())

##############################################

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy 
# ko'rinishda istalgancha berilishi mumkin bo'lsin.

# def malumot(ism ,familiya,**malumotlar):
#     malumotlar['ism']=ism
#     malumotlar['familiya']=familiya
#     return malumotlar

# malumot=malumot('xusanxon', "Nabiyev", manzil='qoqon', maktab=33, yoshi=22,malimoti='oliy')

# print(f"Talaba:{malumot['ism'].title()} {malumot['familiya']}" )




