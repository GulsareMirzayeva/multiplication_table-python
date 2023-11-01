# Task1
# def vurma(a, b):
#     return a * b

# def cixma(a, b):
#     return a - b

# def toplama(a, b):
#     return a + b

# def bolme(a, b):
#     if b == 0:
#         return "0-a bölünmə qarşıdır"
#     return a / b

# while True:
#     print("Daxil Edin")
#     print("Vurma (1), Çıxma (2), Toplama (3), Bölmə (4),")

#     emeliyyat = input("Daxil edildi: ")


#     if emeliyyat not in ['1', '2', '3', '4']:
#         print("Xəta! Yalnız vurma çıxma toplama və bölmə əməliyyatlarını seçə bilərsiniz.")
#         continue

#     a = float(input("Ədəd daxil edin: "))
#     b = float(input("Ədəd daxil edin: "))

#     if emeliyyat == '1':
#         netice = vurma(a, b)
#         print(f"Cavab: {a} * {b} = {netice}")
#     elif emeliyyat == '2':
#         netice = cixma(a, b)
#         print(f"Cavab: {a} - {b} = {netice}")
#     elif emeliyyat == '3':
#         netice = toplama(a, b)
#         print(f"Cavab: {a} + {b} = {netice}")
#     elif emeliyyat == '4':
#         if b == 0:
#             print("Xəta! 0-a bölmək əməliyyatı mümkün deyil.")
#         else:
#             netice = bolme(a, b)
#             print(f"Cavab: {a} / {b} = {netice}")




# Task2

# i = 1  
# while i <= 10:  
#     e = 1  
#     while e <= 10:  
#         vurma = i * e  
#         print(f"{i} * {e} = {vurma}")  
#         e += 1 
#     i += 1  
