A = [0, 1, 2, 3, 4, 5, 6, 7, 8] # 11 ekleyerek te deneye bilirsin o zaman olmadıgı için NO diyecek
B = [5, 9, 8, 1, 3, 7, 0, 4, 2, 6, -1]
OK = True
for element in A: # A daki her elemanı döndür
    try:
        index = B.index(element) # B nin içinde A nın indexinde index varmı
    except ValueError: #yoksa OK i false yap
        OK = False
if OK: # OK true ise yes yaz
    print("YES")
else:
    print("NO") # aksi halde No yaz




