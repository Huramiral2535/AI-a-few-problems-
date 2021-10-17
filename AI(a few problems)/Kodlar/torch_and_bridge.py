import itertools
buradakiler=[1, 2, 5, 8]
karsıdakiler=[]

Toplam=0
for i in buradakiler:
    Toplam=Toplam+i

def donen_sec(cift):
    if len(karsıdakiler)==0 :
        return min(cift)
    else:
        return min(karsıdakiler)


def cift_degerlendir(cift):
    gidis_sure = max(cift)
    donus_sure = min(cift)
    Fn=gidis_sure+(Toplam-donus_sure+donen_sec(cift)) ## F(n)=g(n)+h(n),  h(n) geride kalanlar toplamı ve karşıdaki en hızlı kişinin dönüş süresi alınarak hesaplandı.

    return [Fn,gidis_sure,donus_sure]

def cift_sec(konbinler):
    minX=9999999999999999
    min_cift=[]
    for i in konbinler:
        sonuclar=cift_degerlendir(i)
        X=sonuclar[0]
        if X<minX :
            minX=X
            min_cift=(sonuclar[1],sonuclar[2])

    print("seçilen kişiler:",min_cift)
    return min_cift


total_sure=0
while len(buradakiler)>1:

    cift_konbinasyonları= list(itertools.combinations(buradakiler, 2))
    print("Karsıya geçebilecek mümkün tüm kişi konbinasyonları:", cift_konbinasyonları)
    karsıya_gececek_cift=cift_sec(cift_konbinasyonları)
    karsıdakiler.append(karsıya_gececek_cift[0])
    karsıdakiler.append(karsıya_gececek_cift[1])
    total_sure=total_sure+(max(karsıya_gececek_cift))
    print("karşıya geçiyorlar, süre:",max(karsıya_gececek_cift),"dk")
    buradakiler.remove(karsıya_gececek_cift[0])
    buradakiler.remove(karsıya_gececek_cift[1])

    buradakiler.append(min(karsıdakiler))
    total_sure=total_sure+(min(karsıdakiler))
    print("meşalenin geri getirilme süresi:",min(karsıdakiler),"dk")
    karsıdakiler.remove(min(karsıdakiler))

    print("Şu ana kadar geçen süre:",total_sure)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


print("Son çift geçtikten sonra meşalenin geri getirilmesine gerek yoktur, bu yüzden son meşale geri getirme süresini düşüyoruz.")
total_sure=total_sure-buradakiler[0]

print("Geçişlerin tamamlandığı süre: ",total_sure)