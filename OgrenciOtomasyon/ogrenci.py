ogrenciler = []
ogretmenler = []
giris = None

def baslik(deger):
    return "*"*20+" "+deger+" "+20*"*"

def durum(metin):
    return "[DURUM] "+metin

def anaMenu():
    while True:
        print(baslik("ANA MENÜ"))
        print("1) Öğrenci Kayıt")
        print("2) Öğretmen Kayıt")
        print("3) Öğrenci Giriş")
        print("4) Öğretmen Giriş")
        print("5) Çıkış Yap")

        islem = input("Seçenek: ")
        if islem == "1":
            ogrenciKayit()
        elif islem == "2":
            ogretmenKayit()
        elif islem == "3":
            ogrenciGiris()
        elif islem == "4":
            ogretmenGiris()
        elif islem == "5":
            break
        else:
            print("Lütfen geçerli bir seçenek belirtin...")

def ogrenciKayit():
    print(baslik("ÖĞRENCİ KAYIT"))

    ogrenci = {}
    ogrenci['kullaniciadi'] = input("Kullanıcı Adı: ")
    ogrenci["parola"]       = input("Parola: ")
    ogrenci["ad"]           = input("Ad: ")
    ogrenci["soyad"]        = input("Soyad: ")
    ogrenci["okul"]         = input("Okul: ")
    ogrenci["bolum"]        = input("Bölüm: ")
    ogrenci["dersler"]      = []

    ogrenciler.append(ogrenci)
    print(durum("Öğrenci kaydedildi!"))

def ogretmenKayit():
    print(baslik("ÖĞRETMEN KAYIT"))

    ogretmen = {}
    ogretmen["kullaniciadi"] = input("Kullanıcı Adı: ")
    ogretmen["parola"]       = input("Parola: ")
    ogretmenler.append(ogretmen)
    print(durum("Öğretmen kaydedildi!"))

def ogrenciGiris():
    print(baslik("ÖĞRENCİ GİRİŞ"))

    username = input("Kullanıcı Adı: ")
    password = input("Parola: ")

    girisYapildi = False

    for ogrenci in ogrenciler:
        if ogrenci['kullaniciadi'] == username and ogrenci["parola"] == password:
            girisYapildi = True
            ogrenciMenu(ogrenci)

    if not girisYapildi:
        print(durum("Kullanıcı adı veya parola hatalı!"))
        ogrenciGiris()

def ogrenciMenu(giris):
    while True:
        print(baslik("ÖĞRENCİ MENÜ"))
        print("Hoşgeldiniz, "+giris['ad']+" "+giris['soyad'])
        print("1) Derslerim")
        print("2) Notlarım")
        print("3) Ders Ekle")
        print("4) Ders Çıkart")
        print("5) Çıkış Yap")

        islem = input("Seçenek: ")
        if islem == "1":
            derslerim(giris)
        elif islem == "2":
            notlarim(giris)
        elif islem == "3":
            dersEkle(giris)
        elif islem == "4":
            dersCikart(giris)
        elif islem == "5":
            break
        else:
            print("Lütfen geçerli bir seçenek belirtin...")

def derslerim(giris):
    print("Aldığım Dersler: ")
    for ders in giris["dersler"]:
        print("- "+ders["adi"])

def notlarim(giris):
    print("Notlar: ")
    for ders in giris["dersler"]:
        if ders["not"] != None:
            print("- "+ders["adi"]+" --> "+ders["not"])
        else:
            print("- "+ders["adi"]+" dersi için not girilmedi")

def dersEkle(giris):
    ders = input("Ders? ")
    giris["dersler"].append({"adi": ders, "not": None})

def dersCikart(giris):
    print("Silmek istediğiniz ders: ")
    dersNo = 1
    for ders in giris["dersler"]:
        print(str(dersNo)+") " + ders["adi"])
        dersNo+=1
    secim = input("Seçim: ")
    del giris["dersler"][int(secim)-1]


def ogretmenMenu(giris):
    while True:
        print(baslik("ÖĞRETMEN MENÜ"))
        print("1) Öğrenciler")
        print("2) Öğrenci Ekle")
        print("3) Öğrenci Sil")
        print("4) Ders Notu Güncelle")
        print("5) Çıkış Yap")

        islem = input("Seçenek: ")
        if islem == "1":
            ogrenciListe(giris)
        elif islem == "2":
            ogrenciEkle(giris)
        elif islem == "3":
            ogrenciSil(giris)
        elif islem == "4":
            notGuncelle(giris)
        elif islem == "5":
            break
        else:
            print("Lütfen geçerli bir seçenek belirtin...")

def ogrenciListe(giris):
    print("Öğrenciler:")
    for ogrenci in ogrenciler:
        print(ogrenci["ad"]+" "+ogrenci["soyad"])

def ogrenciEkle(giris):
    ogrenci = {}
    ogrenci['kullaniciadi'] = input("Kullanıcı Adı: ")
    ogrenci["parola"] = input("Parola: ")
    ogrenci["ad"] = input("Ad: ")
    ogrenci["soyad"] = input("Soyad: ")
    ogrenci["okul"] = input("Okul: ")
    ogrenci["bolum"] = input("Bölüm: ")
    ogrenci["dersler"] = []

    ogrenciler.append(ogrenci)
    print(durum("Öğrenci kaydedildi!"))

def ogrenciSil(giris):
    print("Silmek istediğiniz öğrenci: ")
    ogrenciNo = 1
    for ogrenci in ogrenciler:
        print(str(ogrenciNo) + ") " + ogrenci["ad"])
        ogrenciNo+= 1
    secim = input("Seçim: ")
    del ogrenciler[int(secim) - 1]

def notGuncelle(giris):
    print("Öncelikle öğrenci seçiniz: ")
    ogrenciNo = 1
    for ogrenci in ogrenciler:
        print(str(ogrenciNo) + ") " + ogrenci["ad"])
        ogrenciNo += 1
    secim = input("Seçim: ")
    ogrenci = ogrenciler[int(secim) - 1]

    print(ogrenci["ad"]+" "+ogrenci["soyad"]+" kişisinin notlarını güncelle: ")
    for ders in ogrenci["dersler"]:
        eskiNot = 0
        if ders["not"] != None:
            eskiNot = ders["not"]
        print(ders["adi"]+": "+str(eskiNot))
        yeniNot = input("Yeni Not? (0 ile aynı bırakabilirsiniz)")
        if yeniNot != "0":
            ders["not"] = yeniNot

def ogretmenGiris():
    print(baslik("ÖĞRETMEN GİRİŞ"))

    username = input("Kullanıcı Adı: ")
    password = input("Parola: ")

    girisYapildi = False

    for ogretmen in ogretmenler:
        if ogretmen['kullaniciadi'] == username and ogretmen["parola"] == password:
            girisYapildi = True
            ogretmenMenu(ogretmen)

    if not girisYapildi:
        print(durum("Kullanıcı adı veya parola hatalı!"))
        ogretmenGiris()
    else:
        anaMenu()

anaMenu()