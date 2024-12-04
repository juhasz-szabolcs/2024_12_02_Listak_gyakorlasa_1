"""
Generáljunk le 50 db, -60 és 100 közötti véletlen számot (az input txt-hez hasonlóan, de természetesen listába rakva),
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát! 
1. Mennyi a sorozatban található számok szorzata? 
2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét! 
3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét! 
4. Igaz-e, hogy minden szám negatív? 
5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik? 
6. Hány 18-cal osztható szám található a sorozatban? 
7. Mennyi a sorozatban található egyik legkisebb szám indexe? 
8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét! 
9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?
11. Válogassuk ki két listába a páros és a páratlan számokat!
"""

# 0
import random

numbers = []
for number in range(50):
    numbers.append(random.randint(-60, 100))
print("Generált számok", numbers)

# 1. Mennyi a sorozatban található számok szorzata?
product = 1
for num in numbers:
    product *= num

print("A számok szorzata: ", product)

# 2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét! 
last_index_div_5_7 = None
for i in range(len(numbers)):
    if numbers[i] % 5 == 0 or numbers[i] % 7 == 0:
        last_index_div_5_7 = i
print("Az utolsó 5-tel/ 7-tel osztható szám: ", last_index_div_5_7)

# 3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
last_index_div_3_7 = None
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 7 == 0:
        last_index_div_5_7 = i
        break
print("3. Az első 3-mal/ 7-tel osztható szám: ", last_index_div_3_7)

# 4. Igaz-e, hogy minden szám negatív? 
all_negative = True
for num in numbers:
    if num >= 0:
        all_negative = False
        break
print("Minden szám negativ: ", all_negative)

minden_negativ = all(szam < 0 for szam in numbers)
print(minden_negativ)

# 5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik? 
number_between_1_10 = any(1 <= num <= 10 for num in numbers)
print("5. Van-e szám 1 és 10 között: ",number_between_1_10)