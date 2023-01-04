arr = [27, 5, 24, 2, 3, 1]
print(arr)

for border in range(0, len(arr)-1):
    for i in range(border, len(arr)):
        if arr[i] < arr[border]:
            arr[border], arr[i] = arr[i], arr[border]
    border += 1
    print(arr)
print(arr)
