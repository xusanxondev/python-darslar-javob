# import  matplotlib.pyplot as plt
#
#
# # dev_y =[21,22,23,24,25,26,27]
# # dev_yy =[65,68,61,84,97,32,54]
# # dev_x =[15,88,11,620,88,3,300]
# # dev_xx =[200,300,400,500,600,700,800]
# #
# # plt.plot(dev_y, dev_x, color='g', marker='o', markerfacecolor='y', linewidth='3',label='All language')
# # plt.plot(dev_yy, dev_xx, color='b', marker='v', markerfacecolor='r', linewidth='5',label='Python')
# # plt.legend()
# # plt.title('Qondayyee')
# # plt.show()
#
# # fig= plt.figure()
# # print(fig.axes)
# # ax1= fig.add_subplot(2,2,1)
#
# Uy vazifasi 1: Ish haqi trendlarini vizualizatsiya qilish
# Uch xil dasturlash tili (Python, JavaScript va Java) uchun 7 yil (2018-2024) davomidagi ish haqi trendlarini ko'rsatuvchi chiziqli grafik yarating. Quyidagilarni ta'minlang:
#
# Har bir chiziq uchun turli ranglardan foydalaning
# Markerlarni turli ranglar bilan qo'shing
# Chiziq qalinligini to'g'ri belgilang
# Legendani qo'shing
# Sarlavha, x o'qi (Yil) va y o'qi (O'rtacha ish haqi, $) qo'shing
# Grafikni yanada o'qilishi uchun to'r chiziqlarini qo'shing
#
# Uy vazifasi 2: Aholi taqsimotini tahlil qilish
# 1×2 joylashuvda 2 ta subplot bilan rasm yarating:
#
# Aholi namunasidagi yoshlar taqsimotini ko'rsatuvchi gistogramma (tasodifiy ma'lumotlar yarating)
# Xuddi shu ma'lumotlar uchun quti-diagramma (box plot)
#
# Ikkala diagramma uchun:
#
# Mos sarlavha va yorliqlar qo'shing
# Maxsus ranglardan foydalaning
# To'r chiziqlarini qo'shing
# fig.suptitle() yordamida rasm darajasidagi sarlavha qo'shing
#
# Uy vazifasi 3: Sotuv ko'rsatkichlari dashbordi
# Sotuvning turli jihatlarini ko'rsatuvchi 2×2 joylashuvda 4 ta subplot bilan rasm yarating:
#
# Chiziqli grafik: O'tgan yil davomidagi oylik sotuvlar
# Bar grafik: Choraklik sotuvlarni solishtirish (joriy yil va o'tgan yil)
# Doira diagramma: Mahsulot toifalari bo'yicha sotuvlar taqsimoti
# Sochma diagramma: Reklama xarajatlari va sotuvlar o'rtasidagi munosabat
#
# Har bir subplot uchun:
#
# Mos sarlavhalar
# Aniq yorliqlar
# Maxsus ranglar
# Barcha grafiklar uchun yagona dizayn
#
# Uy vazifasi 4: Subplotlar yordamida ma'lumotlarni solishtirish
# Ikkita ma'lumotlar to'plamini (masalan, ikki shahar uchun harorat ma'lumotlari) solishtiruvchi vizualizatsiya yarating:
#
# Vertikal joylashuvda (3×1) 3 ta subplot bilan rasm
# Birinchi subplot: 1-ma'lumotlar to'plami uchun chiziqli grafik
# Ikkinchi subplot: 2-ma'lumotlar to'plami uchun chiziqli grafik
# Uchinchi subplot: To'g'ridan-to'g'ri solishtirish uchun bir xil koordinata o'qlarida ikkala ma'lumotlar to'plami
#
# Talablar:
#
# Barcha grafiklar bo'ylab x o'qi masshtablarini sinxronlashtiring
# fig.supxlabel() yordamida umumiy x o'qi yorlig'ini qo'shing
# Ma'lumotlar to'plamlarini farqlash uchun markerlar va chiziq uslublarini sozlang
# Makondan optimal foydalanish uchun zichroq joylashuvni qo'shing (tight_layout)
#
# Uy vazifasi 5: Interaktiv vizualizatsiya loyihasi
# O'quvchilar natijalari ma'lumotlarining keng qamrovli vizualizatsiyasini yarating:
#
# 2×2 joylashuvda 4 ta subplot bilan asosiy rasm
# Birinchi subplot: Vaqt davomida o'rtacha ballarni ko'rsatuvchi chiziqli grafik
# Ikkinchi subplot: Turli fanlar bo'yicha natijalarni taqqoslovchi bar grafik
# Uchinchi subplot: O'qish soatlari va ballar o'rtasidagi bog'liqlikni ko'rsatuvchi sochma diagramma
# To'rtinchi subplot: Turli faoliyatlar uchun vaqt taqsimotini ko'rsatuvchi doira diagramma
