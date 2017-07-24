A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
B = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
OK = True

firstIndex = B.index(A[0]) # B de Anın 0. value si kaçıncı indiste
for index, element in enumerate(A): #foreach A nın her elementini ve indexini döndür
    if B[index + firstIndex] != element: # baslangıc indexine göre elemanlar birbirlerine uyuyor mu
        OK = False #uymuyosa OK false olsun

if OK: # OK true ise yes yaz
    print("YES")
else:
    print("NO") # aksi halde No yaz




