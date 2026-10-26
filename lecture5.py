# Въвеждане на броя оценки
n = int(input("Въведете броя на оценките: "))

suma = 0

# Въвеждане на оценките
for i in range(n):
    ocenka = float(input(f"Въведете оценка {i + 1}: "))
    suma += ocenka

# Изчисляване на средния успех
sreden_uspeh = suma / n

# Извеждане на резултата
print(f"Средният успех на студента е: {sreden_uspeh:.2f}")