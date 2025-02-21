

# 1 *. Raqamni (1 dan n gacha) (bu erda n foydalanuvchi kiritgan raqam) (x, x * x) ko'rinishida o'z ichiga olgan 
# lug'at yaratish va chop etish uchun Python skriptini yozing. Simple Dictionary (n = 5):

# Kutilayotgan natija: {1:1, 2:4, 3:9, 4:16, 5:25}

# n=int(input('son kiriting: '))
# kv = {son:son*son for son in range(1, n+1)}
# print(kv)

# 2. Lug'atdagi barcha qiymatlarni yig'ish va arifmetik o'rtachani chiqarish uchun Python dasturini yozing.

# n=int(input('son kiriting: '))
# kv = {son:son*son for son in range(1, n+1)} #yuqoridagi kvadratlarni(qiymat) ortacha arifmetigini topadi! (1+4+9+...+n*n)/2 
# summa=0
# for v in kv.values():
#     summa+=v
# print(summa//2) #yani 4 kiritadigan bolse: (1+4+9+16)//2=15

# #generatsiya
# y=[v for v in kv.values()]
# print(sum(y)//2)

# 3 *.Ikki roʻyxatni kalit: qiymat lugʻatiga birlashtirish uchun Python dasturini yozing. RO'YXATLAR BIR HAJIMDA 
# bo'lishi kerak [key] [values] {key, value}

# keys=['osh','kabob','manti']
# values=[25000,15000,10000]
# key_value = {}

# for i in range(len(keys)):
#     key_value[keys[i]] = values[i]

# print(key_value)


# 4.Shaharlar koordinatalari lug'ati mavjud. 
# cities = {
#     'Moscow': [550, 370],
#     'London': [510, 510],
#     'Paris': [480, 480],
# }

# # Quydagi formuladan foydalanib, ular orasidagi masofalarning lug'atlarini tuzing:
# # ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# distances = {}
# moscow = cities['Moscow']
# london = cities['London']
# paris = cities['Paris']

# distances['Moscow-London'] = ((london[0] - moscow[0])**2 + (london[1] - moscow[1])**2)**0.5
# distances['Moscow-Paris'] = ((paris[0] - moscow[0])**2 + (paris[1] - moscow[1])**2)**0.5
# distances['London-Paris'] = ((paris[0] - london[0])**2 + (paris[1] - london[1])**2)**0.5

# print(distances)

# 5 **. Mahsulot kodlari lug'ati va stokdagi tovarlar miqdori lug'ati mavjud.
# Har bir mahsulot toifasining umumiy narxini ko'rsating
# goods = {
#    'Lampa': '12345',
#     'Stol': '23456',
#     'Divan': '34567',
#     'Stul': '45678',
#     }

# store = {
#     '12345': [
#         {
#             'quantity': 27,
#             'price': 42
#             },
#         ],
#     '23456': [
#         {
#             'quantity': 22,
#             'price': 510
#             },
#         {
#             'quantity': 32,
#             'price': 520
#             },
#         ],
#     '34567': [
#         {
#             'quantity': 2,
#             'price': 1200
#             },
#         {
#             'quantity': 1,
#             'price': 1150
#                 },
#         ],
#     '45678': [
#         {
#             'quantity': 50,
#             'price': 100
#             },
#         {
#             'quantity': 12,
#             'price': 95
#             },
#         {    
#             'quantity': 43,
#             'price': 97
#             },
#         ],
#     }

# for mahsulot, kodi in goods.items():
#     soni=0
#     narxi=0
#     for summa in store[kodi]:
#         soni+=summa['quantity']
#         narxi+=summa['quantity']*summa['price']
        
#     print(f'{mahsulot} soni: {soni} umumiy qiymati: {narxi}' )


# 6. Ikki lug'atni uchinchi lug'atga birlashtirish   {dic1} {dict2}    {dict3} 
# from pprint import pprint

# goods = {
#     'Lampa': '12345',
#     'Stol': '23456',
#     'Divan': '34567',
#     'Stul': '45678',
# }

# cities = {
#     'Moscow': [550, 370],
#     'London': [510, 510],
#     'Paris': [480, 480],
# }


# universal_dict= cities | goods
# pprint(universal_dict)









