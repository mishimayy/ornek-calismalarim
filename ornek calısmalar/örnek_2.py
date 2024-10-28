def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    
    OgrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3
    print(ortalama)

    if ortalama>=90 and ortalama<=100:
        harf  = "AA"
    elif ortalama>=85:
        harf = "BA"
    elif ortalama>65:
        harf = "CC"
    else:
        harf = "FF"
    return OgrenciAdi+ ":" +harf+ "\n"
    

def ortalamalari_oku():
    with open("sinavnotlari.txt","r",encoding="utf-8") as file: # "r"-> read 
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğrenci adi :")
    soyad = input("Öğrenci soyadi :")
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")

    with open("sinavnotlari.txt","a" ,encoding="utf-8") as file: #"w" yazsaydık diğer öğrencinin bilgilerini girince sistemi kapatıyor
        file.write(ad+ ' '+soyad+ ':'+not1+ ','+not2+ ','+not3+'\n')


def notlari_kayitet():
    with open("sinavnotlari.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for satir in liste:
                file2.write(satir)
        

while True:
    islem=input('1 - Notlari oku\n2 - Not gir\n3 - Notlari kayit et\n4 - Çikiş\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kayitet()
    else:
        break