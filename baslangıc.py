ogrenciler = []
for i in range(0, 2):
    ogrenci = {}
    isim = input("Öğrencinin İsmi:")
    soyisim = input("Öğrencinin Soyismi:")
    numara = input("Öğrencinin Numarası:")
    dersSayisi = input("Ders sayısı:")
    notlar = []
    toplam = 0
    dersSayisi = int(dersSayisi)
    gecenler = []
    kalanlar = []
    for i in range(0, dersSayisi):
        notu = input(str(i + 1) + ". Ders Notu:")
        toplam += int(notu)
        notlar.append(notu)
        gecti = input(str(i + 1) + ". Dersi Gecti mi? [Gecti/Kaldi]")
        if gecti == "Gecti":
            gecenler.append(i+1)
        elif gecti == "Kaldi":
            kalanlar.append(i+1)
    ortalama = toplam / dersSayisi

    ogrenci['isim'] = isim
    ogrenci['soyisim'] = soyisim
    ogrenci['dersSayisi'] = dersSayisi
    ogrenci['notlar'] = notlar
    ogrenci['ortalama'] = ortalama
    ogrenci['numarasi'] = numara
    ogrenci["gecenler"] = gecenler
    ogrenci["kalanlar"] = kalanlar

    ogrenciler.append(ogrenci)

print("--- Öğrenciler ---")

toplamOrt = 0
for ogr in ogrenciler:
    print("-- OGRENCI --")
    print("İsmi:", ogr['isim'])
    print("Soyisim:", ogr['soyisim'])
    print("Numara:", ogr['numarasi'])
    print("Ders Sayısı:", ogr['dersSayisi'])
    i = 1
    for ogrNot in ogr['notlar']:
        print(str(i)+". Ders Notu:", ogrNot)
        i+=1
    print("Not Ortalaması:", ogr['ortalama'])
    for ogrGecen in ogr['gecenler']:
        print(str(ogrGecen)+". Dersini Geçti")
    for ogrKalan in ogr['kalanlar']:
        print(str(ogrKalan)+". Dersi Kaldı")
    toplamOrt += ogr['ortalama']

print("--- GENEL ---")
print("NOT ORTALAMASI", toplamOrt/len(ogrenciler))