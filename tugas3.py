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


list_bilangan_acak = [
    17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1
]
print("List bilangan acak sebelum sorting : ", list_bilangan_acak)
list_bilangan_acak.sort()
print("List bilangan acak setelah sorting : ", list_bilangan_acak)

dicari = 72

for i in range(len(list_bilangan_acak)):
    if binary_search(list_bilangan_acak, dicari)[0]:
        print(f"Keyword : {dicari} ditemukan di index : {binary_search(list_bilangan_acak, dicari)[1]}")
        break
else:
    print(f"Keyword : {dicari} tidak ditemukan")