sample_random=[3,1,2,4,7,5,6,"_",8]
perfect=["_",1,2,3,4,5,6,7,8]



def mutlak_deger(x):
    if x>=0:
        return x
    else:
        return -1*(x)

def tahta_yazdır(list):
    print("|-------|")
    print("|",list[0], list[1], list[2],"|")
    print("|",list[3], list[4], list[5],"|")
    print("|",list[6], list[7], list[8],"|")
    print("|-------|")

tahta_yazdır(sample_random)
##tahta_yazdır(perfect)

def hamle(yön):
    pozisyon=sample_random.index("_")

    L=gidilebilecek_yönleri_belirle(sample_random)
    if yön in L:
        if yön == "sağ":
            sample_random[pozisyon] = sample_random[pozisyon + 1]
            sample_random[pozisyon + 1] = "_"
        elif yön == "sol":
            sample_random[pozisyon] = sample_random[pozisyon - 1]
            sample_random[pozisyon - 1] = "_"
        elif yön == "aşağı":
            sample_random[pozisyon] = sample_random[pozisyon + 3]
            sample_random[pozisyon + 3] = "_"
        elif yön == "yukarı":

            sample_random[pozisyon] = sample_random[pozisyon - 3]
            sample_random[pozisyon - 3] = "_"

    else :
        print("bu yöne şu an gidemez.")


def kontrol(sample_random,perfect):
   kriter=0
   for i in range (0,9):
       if sample_random[i]==perfect[i]:
           kriter=kriter-1
       else:
           kriter=kriter+mutlak_deger(i-perfect.index(sample_random[i]))

   return kriter


def gidilebilecek_yönleri_belirle(list):
    yönler=["sol","sağ","yukarı","aşağı"]

    if list.index("_")==0 or list.index("_")==1 or list.index("_")==2 :
        yönler.remove("yukarı")

    if list.index("_")==6 or list.index("_")==7 or list.index("_")==8 :
        yönler.remove("aşağı")

    if list.index("_")==0 or list.index("_")==3 or list.index("_")==6 :
        yönler.remove("sol")

    if list.index("_")==2 or list.index("_")==5 or list.index("_")==8 :
        yönler.remove("sağ")

    return yönler


def jenerasyondan_sec():
    yönler=gidilebilecek_yönleri_belirle(sample_random)
    degerler=[]
    for i in yönler:
        hamle(i)
        degerler.append(kontrol(sample_random,perfect))
        hamle_geri_al(i)

    return yönler[degerler.index(min(degerler))]

def hamle_geri_al(move):
    hamle(yön_tersini_bul(move))

def yön_tersini_bul(yön):
    if yön == "sağ":
        return ("sol")

    elif yön == "sol":
        return ("sağ")

    elif yön == "yukarı":
        return ("aşağı")

    elif yön == "aşağı":
        return ("yukarı")


print(kontrol(sample_random,perfect))

##hamle("yukarı")
##print(kontrol(sample_random,perfect))
tahta_yazdır(sample_random)

önceki_hamle="1"
while kontrol(sample_random,perfect)>-9 and önceki_hamle!=yön_tersini_bul(jenerasyondan_sec()):
    print(jenerasyondan_sec(), "yönüne gidilmeli.")
    önceki_hamle = jenerasyondan_sec()
    hamle(jenerasyondan_sec())
    tahta_yazdır(sample_random)

    if (kontrol(sample_random, perfect))!=-9:
        print(kontrol(sample_random, perfect))
    elif (kontrol(sample_random, perfect))==-9:
        print("Çözüldü.")




