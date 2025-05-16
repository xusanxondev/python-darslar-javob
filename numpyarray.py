import numpy as np
# 1. Quyidagi massivni NumPy yordamida yarating va elementlarga indeks orqali murojaat qiling.
#
# numpy.array() yordamida A massivini yarating.
# a = np.array([[3, 7, 2],
#               [4, 6, 1]])
# #
# # 1-qator, 2-ustundagi elementni chop eting.
# print(a[0][1])
# #
# # Oxirgi ustunning barcha elementlarini chiqaring.
# for i in a:
#     print(i[2])
#
# 2.Tasodifiy massiv yaratish (random())

# 5×5 o‘lchamli tasodifiy sonlardan iborat massiv hosil qiling.
# #
# a=np.random.randint(1, 100, (5,5))
# print(a)
# # Massivning 3-qatorini chop eting.
# print(a[2])
# # Eng katta va eng kichik elementlarini toping.
# print('Engkatta:',np.max(a))
# print('Eng kichik:' ,np.min(a))
#
# 3.for bilan massivni tahlil qilish
# b =  ([[5, 8, 9],
#       [4, 6, 1]])

# # For sikli yordamida har bir elementni ekranga chiqaring.
# for i in b:
#     for ii in i:
#         print(ii, end=' ')
# # Har bir qatorni alohida chiqaring.
# for i in b:
#     print(i)
#
# 4. .shape bilan o‘lchamni aniqlash
#
# c =  ([[5, 8, 9],
#       [4, 6, 1]])
# # .shape funksiyasidan foydalanib, massiv o‘lchamini chop eting.
# print(np.shape(c)) #size va shape
# print(np.size(c)) #size va shape
# Massivning 1-qavati va 2-qavati elementlarini chiqaring.
# print(c[0]) #1-qavat
# print(c[1]) #2-qavat

# 5. Massivlarni qo‘shish (+)

# d =  np.array([[5, 8, 9],[2, 7, 6]])
# e =  np.array([[9, 2, 4],[7, 2, 3]])
# y=d+e
# k=d*e
# d=d**e

# # D + E amalini bajaring va natijani chiqaring.
# print(y)
# # Natijaviy massivning 2-qatorini chop eting.
# print(y[1])
# #
# 6. Ikki o‘lchamli massivdan ma’lum qismini ajratib olish
#
# Quyidagi 4×4 tasodifiy massivdan 3×3 kichik massivni ajrating.
# #
# aa=np.random.randint(10, 50, (4,4))     #yordamida 4x4 tasodifiy massiv yarating.
# # Ushbu massivning 3x3 qismni (faqat 1–3-qator va 1–3-ustun) ajratib oling.
# # Natijani ekranga chiqaring.
# # print(aa)
# # b=(aa[0:3,0:3])   #3x3
# # print(b)
# # #
# # # 7. Matematika: 2ta masssivning o‘rta arifmetigini hisoblash
#
# f =  np.array([[1, 2, 4],[5, 8, 1]])
# g =  np.array([[5, 6, 2],[6, 4, 3]])
# # F va G massivlarini yarating.
# # Ushbu massivlarning o‘rta arifmetigini (ya’ni (F + G) / 2) hisoblang.
# # Natijaviy massivni ekranga chiqaring.
# print(np.mean(f+g))
#
