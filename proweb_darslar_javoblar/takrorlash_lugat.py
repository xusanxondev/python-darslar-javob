#takrorlash lugatdan
# talabalar = {
#     'Ali': 'S001',
#     'Vali': 'S002',
#     'Sami': 'S003',
#     'Laylo': 'S004',
# }

# talab_fanlar = {
#     'S001': [
#         {'fan': 'Matematika', 'baho': 85},
#         {'fan': 'Fizika', 'baho': 90},
#     ],
#     'S002': [
#         {'fan': 'Matematika', 'baho': 78},
#         {'fan': 'Kimyo', 'baho': 92},
#     ],
#     'S003': [
#         {'fan': 'Biologiya', 'baho': 88},
#         {'fan': 'Fizika', 'baho': 95},
#     ],
#     'S004': [
#         {'fan': 'Kimyo', 'baho': 85},
#         {'fan': 'Matematika', 'baho': 80},
#     ],
# }
# # Har bir talaba uchun o‘rtacha bahosini hisoblash va chiqarish.

# for talaba,kod in talabalar.items():
#     baholar=0
#     for fanbaho in talab_fanlar[kod]:
#         baholar+=fanbaho['baho']
#     print(f'{talaba}ning ortacha bahosi: {baholar/2}')    


# avtomobillar = {
#     'Nexia': 'A001',
#     'Matiz': 'A002',
#     'Lacetti': 'A003',
#     'Cobalt': 'A004',
# }

# avtomobil_xususiyatlari = {
#     'A001': [
#         {'xususiyat': 'Motor hajmi','qiymat': 1.5},
#         {'xususiyat': 'Maksimal tezlik', 'qiymat': 180},
#         {'xususiyat': 'Yadro turi', 'qiymat': 'Benzin'},
#     ],
#     'A002': [
#         {'xususiyat': 'Motor hajmi', 'qiymat': 1.0},
#         {'xususiyat': 'Maksimal tezlik', 'qiymat': 160},
#         {'xususiyat': 'Yadro turi', 'qiymat': 'Benzin'},
#     ],
#     'A003': [
#         {'xususiyat': 'Motor hajmi', 'qiymat': 1.8},
#         {'xususiyat': 'Maksimal tezlik', 'qiymat': 200},
#         {'xususiyat': 'Yadro turi', 'qiymat': 'Benzin'},
#     ],
#     'A004': [
#         {'xususiyat': 'Motor hajmi', 'qiymat': 1.6},
#         {'xususiyat': 'Maksimal tezlik', 'qiymat': 190},
#         {'xususiyat': 'Yadro turi', 'qiymat': 'Benzin'},
#     ],
# }

# for nomi , kodi in avtomobillar.items():
#     berilish='avtomobili xususiyatlari bilan tanishing:'
#     print(f'{nomi}-{berilish}')
#     for avtoxus in avtomobil_xususiyatlari[kodi]:
#         print(avtoxus['xususiyat'],avtoxus['qiymat'])


# kitoblar = {
#     'Alisher Navoiy': 'K001',
#     'Shams Tabrizi': 'K002',
#     'Jaloliddin Rumi': 'K003',
#     'Hafiz Sherozi': 'K004',
# }

# kitoblar_malumotlari = {
#     'K001': [
#         {'xususiyat': 'Muallif', 'qiymat': 'Alisher Navoiy'},
#         {'xususiyat': 'Nashr yili', 'qiymat': 1499},
#         {'xususiyat': 'Sahifalar soni', 'qiymat': 320},
#     ],
#     'K002': [
#         {'xususiyat': 'Muallif', 'qiymat': 'Shams Tabrizi'},
#         {'xususiyat': 'Nashr yili', 'qiymat': 1250},
#         {'xususiyat': 'Sahifalar soni', 'qiymat': 210},
#     ],
#     'K003': [
#         {'xususiyat': 'Muallif', 'qiymat': 'Jaloliddin Rumi'},
#         {'xususiyat': 'Nashr yili', 'qiymat': 1270},
#         {'xususiyat': 'Sahifalar soni', 'qiymat': 400},
#     ],
#     'K004': [
#         {'xususiyat': 'Muallif', 'qiymat': 'Hafiz Sherozi'},
#         {'xususiyat': 'Nashr yili', 'qiymat': 1320},
#         {'xususiyat': 'Sahifalar soni', 'qiymat': 280},
#     ],
# }

# for nomi , kodi in kitoblar.items():
#     berilish='avtomobili xususiyatlari bilan tanishing:'
#     print(f'{nomi}-{berilish}')
#     for avtoxus in kitoblar_malumotlari[kodi]:
#         print(avtoxus['xususiyat'],avtoxus['qiymat'])
































