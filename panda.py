# import  pandas as pd
# import  numpy as np
#
# #
# # s2= pd,Series([10,20,30,40])
# # print(s2)
#
# data ={
#     'ismlar': ['xasan','xusan'],
#     'yoshi': [23,22],
#     'shaxarlar':['Bogdod','Qoqon']
# }
#
# df1=pd.DataFrame(data)
#
# print(df1)
# filter_age= df1[df1['yoshi']<22]
# print(filter_age)
#############################################################################################
import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame

# 1-vazifa: Series yaratish
# 1. Mevalar nomlaridan iborat ro'yxat yarating: ['Olma', 'Banan', 'Uzum', 'Nok', 'Anor']
# 2. Bu ro'yxatdan Series yarating
# 3. Series elementlarini chop eting

# s1= pd.Series(['Olma', 'Banan', 'Uzum', 'Nok', 'Anor'])
# print(s1)

# 2-vazifa: Narxlar bilan Series
# 1. Quyidagi narxlar bilan Series yarating: 5000, 8000, 12000, 7000, 15000
# 2. Bu seriesning o'rtacha qiymatini toping va chop eting
# 3. Eng yuqori va eng past narxlarni chop eting
# Raqamli qiymatlardan Series yaratish
# O'rtacha qiymatni topish
# Eng katta va eng kichik qiymatlarni topish

# s2 =pd.Series([5000, 8000, 12000, 7000, 15000])
# print('eng katta',s2.max())
# print('eng kichik',s2.min())
# print('ortacha',s2.mean())

#
# 3-vazifa: Oddiy DataFrame yaratish
#
# O'quvchilar haqida ma'lumotli DataFrame yaratish
# Birinchi qatorlarni ko'rsatish
# Ustun bo'yicha o'rtacha qiymatni hisoblash
#
# 1. O'quvchilar haqida ma'lumotli DataFrame yarating:
#    - Ismlar: ['Ali', 'Vali', 'Guli', 'Salim', 'Lola']
#    - Yoshi: [12, 10, 11, 12, 10]
# 2. DataFrame ning birinchi 3ta qatorini ko'rsating
# 3. 'Yoshi' ustunidagi o'rtacha yoshni hisoblang
#
# data ={
#     'Ismlar': ['Ali', 'Vali', 'Guli', 'Salim', 'Lola'],
#     'Yoshi': [12, 10, 11, 12, 10]
# }
# df1=pd.DataFrame(data)
# print(df1[:3])
# print('ortacha yosh',df1['Yoshi'].mean())

#
# 4-vazifa: DataFrame saralash
#
# 1. Quyidagi ma'lumotlar bilan yangi DataFrame yarating:
#    - Mahsulot: ['Non', 'Sut', 'Tuxum', 'Guruch', 'Go\'sht']
#    - Narx: [2000, 8000, 15000, 12000, 60000]
#    - Miqdor: [5, 2, 10, 1, 3]
# 2. Mahsulotlarni narx bo'yicha (o'sish tartibida) saralang
# 3. Jami summani hisoblash uchun 'Summa' ustunini qo'shing (Narx * Miqdor)
#
# data={
#     'Mahsulot': ['Non', 'Sut', 'Tuxum', 'Guruch', 'Go\'sht'],
#     'Narx': [2000, 8000, 15000, 12000, 60000],
#     'Miqdor': [5, 2, 10, 1, 3]
# }
#
# df1=pd.DataFrame(data, index=[1,2,3,4,5])
#
# print(df1['Narx'].sort_values())    # --> narx bo'yicha (o'sish tartibida)
# df1['Summa']=df1['Narx']*df1['Miqdor']
# print(df1)

# 5-vazifa: Oddiy filtrlash
#
# 1. 4-vazifadagi mahsulotlar DataFrame-idan foydalaning
# 2. Narxi 10000 so'mdan yuqori bo'lgan mahsulotlarni filtrlang va ko'rsating
# 3. Jami summasi 50000 dan yuqori bo'lgan mahsulotlarni filtrlang
#
# data={
#     'Mahsulot': ['Non', 'Sut', 'Tuxum', 'Guruch', 'Go\'sht'],
#     'Narx': [2000, 8000, 15000, 12000, 60000],
#     'Miqdor': [5, 2, 10, 1, 3]
# }
# 
# df1=pd.DataFrame(data)
# df1['Summa']=df1['Narx']*df1['Miqdor']
#
# s2=pd.Series(data['Narx'])
# s3=pd.Series(df1['Summa'])
#
# print(f'{s2[s2>10000]}')
# print(f'{s3[s3>50000]}')





