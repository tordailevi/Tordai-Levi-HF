import math
import random
def feladat1():
    szam:int=1
    while not(szam>=200 and szam<=920):
        szam:int=int(input("Kérem adjon meg egy számot 200 és 920 között! : "))
        if(szam>=200 and szam<=920):
            elsoszam = str(szam)[0]
            print(f"{elsoszam}")
        else:
            print("ERROR")

#def feladat2():
    #szam:int=100
    #while not (szam>=1 and szam<=9):
        #szam:int=int(input("Adja meg a tanóra számát: "))
    #return szam
def feladat2_kiir(szam:int):
    if (szam==0):
        print("Be se jövök!")
    elif (szam==1):
        print(f"Még 90%-on vagyunk")
    elif (szam==2 or szam==3):
        print("Még bírjuk (60%)")
    elif (szam==4 or szam==5 or szam==6 or szam==7):
        print("Progit tanulunk, töltődünk! 70%")
    elif (szam==8 or szam==9):
        print("Lassan nem bírjuk tovább! 50%")
    else:
        print("Olyan fáradt vagy, hogy azt se tudod milyen órán vagy kiskrapek, próbáld újra!")
    
def feladat3(nap:str, ora:str):
    if(nap=="hétfő"):
        print("Márti alszik!")
    elif(nap=="kedd" and ora=="hittan"):
        print("Márti figyel!")
    elif(nap=="szerda" and ora=="programozás"):
        print("Márti dolgozik!")
    elif(nap=="csütörtök"):
        print("Márti figyel!")
    elif(nap=="péntek"):
        print("Márti félig figyel, a hétvégéről ábrándozik!")
    else:
        print("Nincs info!")

def feladat4():
    szam:float=float(input("Adjon meg egy számot: "))
    if szam>=0:
        gyok=math.sqrt(szam)
        print("A szám négyzetgyöke:",gyok)
    else:
        print("Hiba: Negatív számot adtál meg!")

def feladat5():
    a:float=float(input("Add meg a téglalap egyik oldalának hosszát: "))
    b:float=float(input("Add meg a téglalap másik oldalának hosszát: "))
    if a > 0 and b > 0:
        kerulet = 2 * (a + b)
        terulet = a * b    
        print(f"Téglalap kerülete: {kerulet:.2f}")
        print(f"Téglalap területe: {terulet:.2f}")
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")

'''def randomszamok():
    lista=[]
    i:int=1
    while(i<=13):
        szam:int=int(random.random()*17)-5
        lista.append(szam)
        i+=1
    return lista'''

def szorzotabla():
    i:int=0
    j:int=0
    print("10x10-es szorzótábla:")
    for i in range (1, 11):
        for j in range (1, 11):
            print(f"{i * j:2}", end=" ")
        print()
        #i+=1
        #j+=1

