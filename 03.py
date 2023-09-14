#Jövedelemszámítás
print("Jövedelemszámítás\n")

kor=int(input("Hány éves vagy?"))
if kor>25:
    gyerek=""
    gyerek=input("Van 3 gyereked és nő vagy?----->(Igen/Nem)")
    while gyerek not in ["Igen", "igen", "I", "i","N","n","Nem", "nem"]:
           gyerek = input("Hiba!!!" "Van 3 gyereked és nő vagy?----->(Igen/Nem)")
    brutto=int(input("Mennyi a bruttód :"))
if kor<=25 or gyerek in ["Igen", "igen", "I", "i"]:
    if brutto>500000:
        szja= (brutto-500000) *0.15
    else:
        szja=0

else:
    szja = brutto * 0.15
print("valld be".center(40,"*"))
print(f"SZJA:".ljust(30,"_"), str(int(szja)).rjust(10,"_"),sep="")
print(f"Nyugdíj:".ljust(30,"_"), str(int(brutto*0.1)).rjust(10,"_"),sep="")
print(f"TB:".ljust(30,"_"), str(int(brutto*0.07)).rjust(10,"_"),sep="")
print(f"Mnelkivul:".ljust(30,"_"), str(int(brutto*0.015)).rjust(10,"_"),sep="")
print("")
print(f"Netto:".ljust(30,"_"), str(int(brutto-brutto*0.0185-szja)).rjust(10,"_"),sep="")



