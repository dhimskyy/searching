def binary_search(arr, x):
    arr = [str(i) for i in arr]
    x = str(x)
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True, mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False, False


array_nim_mahasiswa = [
    20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 
    20103011, 20103003, 20103009, 20103021, 20103006, 20103015, 20103013, 20103007
]
print("List nim mahasiswa sebelum sorting : ", array_nim_mahasiswa)
array_nim_mahasiswa.sort()
print("List nim mahasiswa setelah sorting : ", array_nim_mahasiswa)

nim = 20103015

for i in range(len(array_nim_mahasiswa)):
    if binary_search(array_nim_mahasiswa, nim)[0]:
        print(f"Keyword : {nim} ditemukan di index : {binary_search(array_nim_mahasiswa, nim)[1]}")
        break
else:
    print(f"Keyword : {nim} tidak ditemukan")
