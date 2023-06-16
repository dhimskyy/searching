def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1

data = [23, 4, 62, 12, 77, 51, 2, 32]
keyword =  input("Input Keyword: ")
linear_search(keyword, data)

