# szamologep

def adatkeres():
    szam=input("Kérek egy számot: ")
    while not szam.isnumeric():
     print("Rossz érték!!!")
        szam=input("Kérek egy számot: ")
    szam=int(szam)
    return szam

#program eleje

print("számológép")
 szam1=adatkeres():

muvelet=input("Kérem a műveleti jelet (+,-,/,*)")
while muvelet not  in ["+", "-", "/", "*"]:
    print("Nem érveényes művelet")
    muvelet = input("Kérem a műveleti jelet (+,-,/,*) ")

szam2 = input("Kérek egy számot: ")
while not szam2.isnumeric():
    print("Rossz érték")
    szam2 = input("Kérek egy számot: ")
szam2 = int(szam2)

eredmeny=0
if muvelet =="+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2

elif muvelet == "/":
    eredmeny = szam1 / szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2

print(str(szam1).rjust(50,"_"))
print(muvelet, end="")
print(str(szam2).rjust(49,"_"))
print("".rjust(50,"_"))
print(str(eredmeny).rjust(50,"_"))