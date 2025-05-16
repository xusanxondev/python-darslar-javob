import  pandas as pd
import  numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame

# Vazifa 1: Yo'qolgan ma'lumotlarni aniqlash
# Talaba ma'lumotlarini o'z ichiga olgan DataFrame yarating:
# isnull() usulidan foydalanib, qaysi qator va ustunlarda etishmayotgan ma'lumotlar borligini toping.

data= {
'Ism': ['Anna', 'Maksim', 'Irina', 'Oleg'],
'Yosh': [20, np.nan, 22, 21],
'Shahar': ['Moskva', 'Sankt-Peterburg','Tyumen','Kazan']
}
df= pd.DataFrame(data)
# print(df.isnull())

# Vazifa 2: Yo'qolgan ma'lumotlarni hisoblash
# 1-muammodan DataFrame bilan ishlashni davom ettirib, har bir ustundagi etishmayotgan qiymatlar sonini hisoblang.

# print(df.isnull().sum())


# Vazifa 3: Yo'qolgan ma'lumotlarni to'ldirish
# 1-muammodagi DataFrame-dan foydalanib, Yosh ustunidagi etishmayotgan qiymatlarni ushbu ustunning o('rtacha qiymatiga va
# 'shahar ustunidagi "Noma')lum" qiymatiga almashtiring. Yangilangan DataFrame-ni ekranga chop eting.
# #
# df_yoq = df.fillna({'Yosh': df['Yosh'].mean(), 'Shahar': 'Nomalum'})
# print(df_yoq)

# Vazifa 4: Ma'lumotlar etishmayotgan qatorlarni olib tashlash
# 1-topshiriqda yaratilgan DataFrame-dan qiymatlari etishmayotgan qatorlarni olib tashlang. Natijani chop eting.
#
# df_NEW = df.dropna()
# print(df_NEW)


# Vazifa 5: Ma'lumotlarni bo'lim bo'yicha guruhlash
# Xodimlar haqidagi ma'lumotlarni o'z ichiga olgan DataFrame yarating:
# Bo'lim: ['Marketing', 'Marketing', 'HR', 'HR', 'IT', 'IT']
# Xodim: ['Ivan', 'Olga', 'Elena', 'Maksim', 'Aleksey', 'Dmitriy']
# Maosh: [60000, 70000, 50000, 55000, 80000, 75000]
# Ma'lumotlarni bo'lim bo'yicha guruhlang va har bir bo'limdagi umumiy ish haqini hisoblang.
#
# data= {
# "Bo'lim": ['Marketing', 'Marketing', 'HR', 'HR', 'IT', 'IT'],
# 'Xodim': ['Ivan', 'Olga', 'Elena', 'Maksim', 'Aleksey', 'Dmitriy'],
# 'Maosh': [60000, 70000, 50000, 55000, 80000, 75000]
# }
# df1=pd.DataFrame(data)
# gruppa_yagzon = df1.groupby("Bo'lim")['Maosh'].sum()
# print(gruppa_yagzon)

# Vazifa 6: Guruhlash va bir nechta yig'ish funktsiyalari
# 5-muammodan DataFrame-dan foydalanib, ma'lumotlarni bo'limlar bo'yicha guruhlang va quyidagi funktsiyalarni qo'llang:
# ish haqi yig'indisi, o'rtacha ish haqi va maksimal ish haqi.

# gruppa_chayon = df1.groupby("Bo'lim")['Maosh'].agg(['sum', 'mean', 'max'])
# print(gruppa_chayon)

# Vazifa 7: Bir nechta ustunlar bo'yicha guruhlash
# 5-topshiriqdan DataFrame-ga Ishga olish yili ustunini qo'shing: [2015, 2018, 2020, 2019, 2017, 2016]. Ma'lumotlarni "Bo'lim" va
# "Ishga qabul qilingan yil" bo'yicha guruhlang, har bir guruh uchun o'rtacha ish haqini hisoblang.
# data= {
# "Bo'lim": ['Marketing', 'Marketing', 'HR', 'HR', 'IT', 'IT'],
# 'Xodim': ['Ivan', 'Olga', 'Elena', 'Maksim', 'Aleksey', 'Dmitriy'],
# 'Maosh': [60000, 70000, 50000, 55000, 80000, 75000]
# }
# data["Ishga qabul qilingan yil"]=[2015, 2018, 2020, 2019, 2017, 2016]
#
# df1=pd.DataFrame(data)
#
# gruppa_tursunxon = df1.groupby(["Bo'lim",'Xodim','Ishga qabul qilingan yil'])['Maosh'].sum()
# print(gruppa_tursunxon)

# Vazifa 8: Ikki DataFramni birlashtirish
# Ikkita DataFrames yarating:
# Birinchisida mahsulotlar haqidagi ma'lumotlar mavjud: ProductID va ProductName (mahsulot nomlari).
# Ikkinchisida narxlar haqida ma'lumot mavjud: ProductID va Price (mahsulot narxlari).
# ProductID ustuni bo'yicha ikkita DataFramni birlashtiring va natijani chiqaring.

# df1 = pd.DataFrame({'ProductID': [7777,6666,5555],
#                     'ProductName': ['Olma', 'Banan', 'Nok']})
# df2 = pd.DataFrame({'ProductID':[7777,6666,5555],
#                     'Price': [5000, 20000, 45000]})
# new_df = pd.merge(df1, df2, on= 'ProductID')
# print(new_df)

