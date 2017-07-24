A = [0, 1, 2, 3, 4, 5, 6, 7, 8] # 10 ekleyerek te deneye bilirsin o zaman olmadıgı için NO diyecek
B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 11] # 6 ile 5 in yerlerini değiştir gene no demesi gerekiyor çünkü sırası önemli
OK = True

for index, element in enumerate(A): #foreach A nın her elementinin indexini döndür
    if B[index] != element: # B deki elemanlar a dakilerle aynı indekste değilse
        OK = False #OK false olsun

if OK: # OK true ise yes yaz
    print("YES")
else:
    print("NO") # aksi halde No yaz




