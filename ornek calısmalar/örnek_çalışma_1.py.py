Ad_Soyad=input("Adinizi ve Soyadinizi : ")
Dogum_yeriniz=input("Doğum yerinizi yaziniz : ")
Dogum_tarihi=input("Doğum tarihiniz (Gün-ay-yil) : ")
sifre=input("Şifre : ")

guvenli=False

while guvenli==False:

    guvenli=True
    sifreenaz6karakter=False
    if len(sifre)<6:
        print("Şifre en az 6 karakter olmali")
        guvenli=False
    if guvenli:
        enaz1adetbuyukharf=False
        for x in sifre:
            if x.isupper() and x.isalpha(): 
                enaz1adetbuyukharf=True
                guvenli=True
                break
        if enaz1adetbuyukharf==False:
            print("en az 1 adet büyük harf giriniz ")
            guvenli=False

    if guvenli:
        enaz1adetrakam=False
        for x in sifre:
            if x.isnumeric():
                enaz1adetrakam=True
                guvenli=True
                break
        if enaz1adetrakam==False:
            print("en az 1 adet rakam giriniz ")
            guvenli = False

    if guvenli:
        alphanumeric=False
        for x in sifre:
            if x.isalnum()==False:
                alphanumeric=True
                guvenli=True
                break

        if alphanumeric==False:
            print("en az 1 adet (!,?,* vb.) içermelidir.")
            guvenli=False

    if guvenli:
        arayaadsoayd=Ad_Soyad.split(" ")
        for ad in arayaadsoayd:
            if ad in sifre:
                if Ad_Soyad.upper()==False:
                    print("Şifrede ad soyad olamaz")
                    guvenli=True
                

    if guvenli:
        arayatarih=Dogum_tarihi.split(" - ")
        for ad in arayatarih:
            if ad in sifre:
                print("Şifrede doğum tarihi olamaz")
                guvenli = False

    if guvenli:
        dogumyeri=Dogum_yeriniz.split(" ")
        for ad in dogumyeri:
            if ad in sifre:
                print("Şifede doğum yeri bilgisi içermemeli ")
                guvenli=False

    if guvenli == True:
        break
    else:
        sifre=input("Şifre")

print("SİSTEME HOŞGELDİNİZ ! ")


    









            
    
    

