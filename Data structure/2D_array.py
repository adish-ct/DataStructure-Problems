def main():
    arr = []

    for _ in range(3):
        arr.append(list(map(int, input().strip().split())))
    
    print(len(arr))
    print(arr)
    total_sum = sum([num for sublist in arr for num in sublist])
    print(total_sum)

main()