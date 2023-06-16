def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
        else:
            return False


array_plat = [
    ["R 2477 SR"], ["R 1234 DJ"], ["R 7015 LP"], ["R 0201 RR"], ["R 3304 DA"],
    ["R 2401 SK"], ["R 2103 RT"], ["R 1708 RI"], ["R 1111 SR"], ["R 4987 LH"]
]
print("List plat : ", array_plat)
cari = input("Masukkan plat lengkap: ")
for i in range(len(array_plat)):
    if sequential_search(array_plat[i], cari):
        print(f"Keyword : {cari} found at index : {i}")
        break
else:
    print(f"Keyword : {cari} plat tidak ditemukan dalam database")
    
